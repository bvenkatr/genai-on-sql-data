Generate the API Key in aistudio
https://aistudio.google.com/app/apikey

Steps to execute in colab python notebook
-------------------------------------------
import google.generativeai as genai

configure api key
-----------------
genai.configure(api_key='AIzaSyDS-vojA_k2vrfjwW8gdORYAT98N1dGpfow')

Install dependencies
--------------------
!pip install db-sqlite3
! pip install streamlit
!npm install localtunnel@2.0.2

Run the server using streamlit
------------------------------
!streamlit run /content/app.py & npx localtunnel --port 8501 & curl ipv4.icanhazip.com

