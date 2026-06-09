# 환경변수 호출
from dotenv import load_dotenv
load_dotenv()

# OpenAI API 키를 사용하여 ChatOpenAI 모델을 초기화하는 예시
from langchain_openai import ChatOpenAI #ChatOpenAI는 대화형 답변
chat_model = ChatOpenAI() 

# 질문에 대한 답변을 생성하는 예시
# chat_model_response = chat_model.invoke(subject+"에 대해 설명해줘")
# print(chat_model_response.content)

import streamlit as st

st.title("디지털 글쓰기  " + chat_model.model)
# st.title("_streamlit_is :blue[cool] :sunglasses:")
subject = st.text_input("궁금한 내용을 입력해주세요")

if st.button("질문하기", type="primary"):
    with st.spinner(text="In progress...", show_time=True):
        response = chat_model.invoke(subject+"에 대해 설명해줘")
        st.write(response.content)

