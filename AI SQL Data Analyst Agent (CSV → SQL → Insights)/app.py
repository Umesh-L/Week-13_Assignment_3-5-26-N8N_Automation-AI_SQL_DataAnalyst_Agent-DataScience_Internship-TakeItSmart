# AI SQL Data Analyst Agent (CSV → SQL → Insights)

# create environment : python -m venv myenv
# activate environment : myenv\Scripts\activate
# run app : streamlit run app.py

import streamlit as st
import pandas as pd
import sqlite3
import os
import re
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import plotly.express as px

# pip install streamlit pandas langchain-groq python-dotenv plotly

# ---------------- CONFIG ---------------- #
st.set_page_config(page_title="AI SQL Data Analyst", layout="wide")
st.title("🗄️ SQL Data Analyst Agent")

# ---------------- SESSION STATE ---------------- #
if "plot_counter" not in st.session_state:
    st.session_state.plot_counter = 0

# ---------------- SAFE PLOT FUNCTION ---------------- #
def safe_plot(fig):
    st.session_state.plot_counter += 1
    st.plotly_chart(fig, key=f"plot_{st.session_state.plot_counter}")

# ---------------- LOAD API ---------------- #
load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile"
)

# ---------------- CLEAN CODE ---------------- #
def clean_text(text):
    text = re.sub(r"```[sS][qQ][lL]", "", text)
    text = re.sub(r"```python", "", text)
    text = text.replace("```", "")
    return text.strip()

# ---------------- FILE UPLOAD ---------------- #
file = st.file_uploader("Upload CSV", type=["csv"])

if file:
    df = pd.read_csv(file)

    # create sqlite db and load data
    db_path = "database.db"
    conn = sqlite3.connect(db_path)
    df.to_sql("data_table", conn, if_exists="replace", index=False)

    st.subheader("📄 Data Preview")
    st.dataframe(df.head())

    question = st.text_input("Ask a question about your data")

    if question:
        
        st.session_state.plot_counter = 0

        # ---------------- STEP 1: SQL GENERATION ---------------- #
        schema = pd.io.sql.get_schema(df, "data_table")
        
        sql_prompt = f"""
Write ONLY a SQLite query to answer the question.

Table name: data_table
Schema:
{schema}

Question: {question}

Rules:
- No markdown formatting
- No explanation
- Return only the raw SQL text
"""
        
        sql_response = llm.invoke(sql_prompt)
        sql_query = clean_text(sql_response.content)

        st.subheader("📝 Generated SQL Query")
        st.code(sql_query, language="sql")

        # ---------------- STEP 2: EXECUTION & VIZ ---------------- #
        try:
            # execute sql against db
            res_df = pd.read_sql_query(sql_query, conn)
            
            st.subheader("🧮 Query Results")
            st.dataframe(res_df)

            # generate python code for insights and chart
            viz_prompt = f"""
Dataset context from SQL execution:
{res_df.head().to_string()}

Write ONLY Python code to:
1. Store a short, direct text answer to the user's question in a variable named 'result'
2. Use plotly.express as px to create a chart (if the data has more than 1 row/column to compare)
3. If creating a chart, call plot(fig)

Rules:
- Dataframe name is res_df
- DO NOT import anything
- No print()
- No markdown
- No explanation

Question: {question}
"""
            viz_response = llm.invoke(viz_prompt)
            py_code = clean_text(viz_response.content)
            py_code = re.sub(r"import .*", "", py_code) 

            # st.subheader("🧠 Generated Python Code")
            # st.code(py_code)

            # execution environment setup
            local_vars = {
                "res_df": res_df,
                "px": px,
                "plot": safe_plot
            }

            safe_globals = {
                "__builtins__": {
                    "len": len, "range": range, "min": min, "max": max, "sum": sum, "round": round
                }
            }

            exec(py_code, safe_globals, local_vars)

            # ---------------- RESULT ---------------- #
            if "result" in local_vars:
                st.subheader("💡 Answer")
                st.write(local_vars["result"])

        except Exception as e:
            st.error(f"Execution Error: {e}")

    # clean up db connection
    conn.close()