import streamlit as st
from transformers import pipeline
from openai import OpenAI
import os
from PIL import Image


os.environ["OPENAI_API_KEY"] = "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"
img = Image.open('loveCon.png')
client = OpenAI()

st.title("러뷰!~ 연애 상담사 💗스위릐💗")

st.write("나는야 연애고수 스위릐~!!\n")
st.write("안녕!ㅇ! 나는 너의 연애 고민을 해결해줄 상담사 스위릐야💗💗\n")
st.write("나에게 너의 연애 고민을 맡겨봐 !ㅇ!")
st.write("\n\n\n")

st.image(img)
Prompt = st.text_input("먼저 너의 현재 연애 고민을 알려줘!ㅇ!")
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