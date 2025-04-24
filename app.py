import os
import sqlite3
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv




load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question, prompt):
    try:
        model = genai.GenerativeModel('gemini-1.5-pro-latest')
        full_prompt = f"{prompt}\n\nQuestion: {question}"
        response = model.generate_content(full_prompt)
        return response.text.strip()
    except Exception as e:
        st.error(f"Error while generating SQL query: {e}")
        return None



def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    curr = conn.cursor()
    curr.execute(sql)
    rows=  curr.fetchall()
    conn.close()

    for row in rows:
        print (row)
    return rows

prompt = """
You are an expert in converting natural language questions into SQL queries. 
The database is named "student" and contains the following columns: 
- NAME (TEXT) 
- CLASS (TEXT) 
- SECTION (TEXT)

Guidelines:
- Always return only the SQL query without any additional text or explanations.
- Use uppercase SQL syntax.
- Ensure the SQL query is syntactically correct and executable in SQLite.
- Do NOT use triple quotes (''') at the beginning or end of the query.

Examples:
- Input: "How many entries of records are present?"  
  Output: SELECT COUNT(*) FROM STUDENT;

- Input: "Tell me all the students' names in Data Science."  
  Output: SELECT NAME FROM STUDENT WHERE CLASS='Data Science';

- Input: "Which class is Krish in?"  
  Output: SELECT CLASS FROM STUDENT WHERE NAME='Krish';
"""



st.set_page_config(page_title="I can retrive any sql query")
st.header("Gemini App to Retrieve SQL data")

question= st.text_input("Input: ", key="input")

submit= st.button("Ask the question")


if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response= read_sql_query(response,'student.db')
    st.subheader("The response")
    st.write(response)
    for row in response:
        print(row)
        st.write(row)
