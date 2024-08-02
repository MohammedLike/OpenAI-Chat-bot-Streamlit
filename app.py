import os
import json
import streamlit as st
import openai

# Load configuration data
working_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(working_dir, "config.json")
with open(config_path, 'r') as config_file:
    config_data = json.load(config_file)

# Set OpenAI API key
OPENAI_API_KEY = config_data["OPEN_API_Key"]
openai.api_key = OPENAI_API_KEY

# Set Streamlit page configuration
st.set_page_config(
    page_title="Chatbot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Initialize chat history if not already present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display title
st.title("Chatbot")

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message['content'])

# User input
user_prompt = st.text_input("You:", key="user_prompt")

if user_prompt:
    # Add user's message to chat history and display it
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # Get response from OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            *st.session_state.chat_history
        ]
    )
    assistant_response = response['choices'][0]['message']['content']
    
    # Add assistant's response to chat history and display it
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
