import requests
import streamlit as st


st.set_page_config(
    page_title="Kewir Chatbot",
    page_icon="KJ"
)

st.title("Kewir Chatbot")
st.write("Ask me anything about web development,datascience or solarsystem.")


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


user_message = st.chat_input("Ask a technology question...")


if user_message:

    st.session_state.messages.append({
        "role": "user",
        "content": user_message
    })

    with st.chat_message("user"):
        st.write(user_message)

    try:
        response = requests.post(
            "http://127.0.0.1:8000/chat",
            json={"message": user_message}
        )

        if response.status_code == 200:
            answer = response.json()["response"]

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })

            with st.chat_message("assistant"):
                st.write(answer)

        else:
            st.error("The backend returned an error.")

    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the FastAPI backend.")