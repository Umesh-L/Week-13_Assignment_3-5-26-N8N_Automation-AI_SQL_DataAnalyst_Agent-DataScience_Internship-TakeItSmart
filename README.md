# Week-13 Internship Projects - AI News Auto-Blogger and Email Automation & AI SQL Data Analyst Agent

Take it smart (OPC) Private Limited - Data Science Internship

## Summary 📌
This repository contains two separate but related automation projects built during the internship:

- **AI News Auto-Blogger and Email Automation** - an **n8n workflow** that fetches the latest AI news, generates a blog-style summary, formats it as an email, and sends it automatically.
- **AI SQL Data Analyst Agent (CSV → SQL → Insights)** - a **Streamlit app** that turns natural language questions into SQL queries, executes them on uploaded CSV data, and returns insights with charts.

Together, these projects demonstrate practical automation using workflow orchestration, LLMs, SQL, and interactive data analysis.

## Project 1: AI News Auto-Blogger and Email Automation 🤖

This is the **n8n project** in the repository. It runs a daily workflow that collects current AI news and turns it into a polished digest email.

### Key workflow steps

- **Daily Trigger** starts the automation on a schedule.
- **AI News Fetcher** searches for the latest AI-related headlines.
- **SerpApi News Search** provides current news results from the web.
- **Groq LLM** helps transform the news into readable blog content.
- **Blog Generator** creates the article-style summary.
- **Format Email** prepares the final email body.
- **Send Email** delivers the digest automatically.

### Project highlights ✨

- Fully automated content pipeline for daily AI news digestion.
- Uses live search results instead of static content.
- Produces a blog-style summary and email-friendly output.
- Ideal for newsletter automation and content curation use cases.

### Repository structure

- `AI News Auto-Blogger and Email Automation.json`
- `Output snapshots/`
- `Screen Recording/`

### Output snapshots 🖼️
<img width="1919" height="1079" alt="n8n workflow" src="https://github.com/user-attachments/assets/5c2b66fc-b22b-4e55-8512-32ee797afe63" />

<img width="1919" height="1079" alt="result email 1 1" src="https://github.com/user-attachments/assets/1052e3e1-561b-405d-8d8d-1347d0bf12c3" />

<img width="1919" height="1079" alt="result email 1 2" src="https://github.com/user-attachments/assets/b7bfeee6-64ec-4158-9a97-ff5d6d4a97e2" />

<img width="1919" height="1079" alt="result email 1 3" src="https://github.com/user-attachments/assets/ab251491-9f0f-402b-b740-ccfa8ffd6285" />

## Project 2: AI SQL Data Analyst Agent (CSV → SQL → Insights) 📊

This project is a **Streamlit-based AI data analyst agent** that lets you upload a CSV file, ask natural language questions about the data, and receive:

- a generated **SQLite query**
- **query results** as a dataframe
- a short **text answer**
- an optional **Plotly visualization** when the result can be charted

The app uses **Groq + LangChain** to convert questions into SQL and insights, then runs the query against a local SQLite database created from the uploaded CSV.

### Project highlights ✨

- **Natural language to SQL** - asks an LLM to write a raw SQLite query for the uploaded CSV schema.
- **Local SQLite execution** - loads the dataset into `database.db` and runs SQL safely through `pandas.read_sql_query`.
- **AI-generated insights** - creates a short direct answer based on the SQL result.
- **Automated visualizations** - uses `plotly.express` to show charts when the result has enough structure.
- **Streamlit UI** - simple interface for uploading CSVs and asking follow-up questions.

### Tech stack 🧰

- Python
- Streamlit
- Pandas
- SQLite3
- LangChain Groq
- Plotly
- python-dotenv

### How it works ⚙️

1. Upload a CSV file in the Streamlit app.
2. The app saves the file into a local SQLite table named `data_table`.
3. You enter a question in plain English.
4. The LLM generates a SQLite query based on the dataframe schema.
5. The query is executed on the local database.
6. The result is shown as a dataframe, a short answer, and a chart if applicable.

### Example questions 💬

The included `test prompts.txt` file contains sample prompts such as:

- What is the total sales amount for the Furniture category?
- Show the total profit for each Region.
- What are the top 5 most profitable Sub-Categories?

### Repository structure

Top-level layout:

- `app.py`
- `.env`
- `database.db`
- `test prompts.txt`
- `Output snapshots/`
  - `code file screenshot.png`
  - `csv dataset upload.png`
  - `example prompt output 1.png`
  - `example prompt output 2.png`
  - `example prompt output 3.png`
  - `project streamlit interface.png`
  - `sqlite db file.png`
- `Screen recording/`
  - `AI SQL Data Analyst Agent.mp4`
- `.vscode/`
  - `settings.json`
- `myenv/`
  - Python virtual environment files

### Quick start 🚀

1. Create and activate a virtual environment:

```bash
python -m venv myenv
# Windows PowerShell
myenv\Scripts\Activate.ps1
```

2. Install the required libraries:

```bash
pip install streamlit pandas python-dotenv langchain-groq plotly
```

3. Add your Groq API key to `.env`:

```env
GROQ_API_KEY=your_groq_api_key_here
```

4. Run the Streamlit app:

```bash
streamlit run app.py
```

### Notes for reproducibility 📝

- The app expects a CSV upload before any question can be answered.
- The SQL query is generated from the uploaded dataframe schema, so the question should match the dataset columns.
- The app writes the uploaded data into `database.db`; you can delete it if you want to start from a clean state.
- For reliable LLM output, keep questions specific and aligned with the available columns.

### Output snapshots 🖼️

<img width="1919" height="1079" alt="code file screenshot" src="https://github.com/user-attachments/assets/76b5d241-f663-4ab8-8731-8228a4a76378" />

<img width="1919" height="1079" alt="project streamlit interface" src="https://github.com/user-attachments/assets/d1be6400-822f-4bf8-a35d-46758542eeab" />

<img width="1919" height="1079" alt="csv dataset upload" src="https://github.com/user-attachments/assets/7cdcd0f4-1d6a-41ed-a79e-edc7577a5979" />

<img width="1919" height="1078" alt="example prompt output 1" src="https://github.com/user-attachments/assets/788a79d6-f6f0-4b3c-ae33-cdf1dec3f9e1" />

<img width="1881" height="1059" alt="example prompt output 2" src="https://github.com/user-attachments/assets/bba13bb5-e1b6-42f5-8370-ece56f47b788" />

<img width="1919" height="1065" alt="example prompt output 3" src="https://github.com/user-attachments/assets/787f5743-a3f9-4b47-b88b-57b7864e1072" />

<img width="1919" height="1079" alt="sqlite db file" src="https://github.com/user-attachments/assets/379cc0c0-3a7a-4bad-a220-234ad718b95f" />


### Project explanation video 🎥

#### - AI News Auto-Blogger and Email Automation
https://github.com/user-attachments/assets/a7fe696a-8644-450e-803a-a7d8b8075465

#### - AI SQL Data Analyst Agent
https://github.com/user-attachments/assets/89135c93-0c63-42fb-a043-e8d99b62ec4f

## Overall project results ✅

- The n8n workflow automates AI news discovery, summarization, and email delivery.
- The Streamlit app converts natural language into SQL-driven analytics on uploaded CSV data.
- Both projects show end-to-end automation with LLM-assisted output generation.
