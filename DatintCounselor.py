import streamlit as st
from transformers import pipeline
from openai import OpenAI
import openai
import os

#key
os.environ["OPENAI_API_KEY"] = ""

#client 불러오기
client = OpenAI()

st.title("나는야 연애고수~!! 나에게 상담을 맡겨봐 ><~!!")
Prompt = st.text_input("너의 현재 연애고민을 알려줘!ㅇ!")
st.button("click")

result = client.chat.completions.create(
  model = "gpt-4",
  messages = [
    {"role":"system",
     "content":"너는 심리상담사니까 이모티콘을 많이 쓰고 부드러운 말투를 쓰렴!!"},
    {"role":"user",
     "content":Prompt}
  ],
  temperature = 0.5
)

st.info(result.choices[0].message.content)