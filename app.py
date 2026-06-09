
# os나 dotenv를 사용해 .env의 API 키를 가져오는 로직 추가 가능
import streamlit as st

st.title("🤖 나만의 AI 챗봇")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("무엇이든 물어보세요!"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 여기에 AI 답변 로직(OpenAI 등)을 연동합니다.
    response = f"네, '{prompt}'라고 말씀하셨군요!" 

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})