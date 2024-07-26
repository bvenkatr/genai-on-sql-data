import streamlit as st
import sqlite3
import google.generativeai as genai

# Provide your Genai api Key
genai.configure(api_key="AIzaSyDS-vojA_k2vrfjwW8gdORYAT98N1dGpfow")
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
# Types of prompts
# zero shot
# one shot
# few shot

# Below is a few shot prompt
prompt=[
    """
    The SQL database has the name employee and has the following columns - name, 
    role, dept, salary \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM employee ;
    \nExample 2 - Tell me all the employees working in OB dept?, 
    the SQL command will be something like this SELECT * FROM employee 
    where dept="OB"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """
]

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"ltc.db")
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(row)
