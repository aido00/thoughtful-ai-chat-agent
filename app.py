import streamlit as st
from agent import SupportAgent

st.set_page_config(page_title="Thoughtful AI Support", page_icon="💬")

@st.cache_resource
def load_agent():
    return SupportAgent('knowledge_base.json')

agent = load_agent()

st.title("Thoughtful AI Support Agent")
st.markdown("Ask me anything about our AI automation agents!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type your question here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    response = agent.get_response(prompt)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)

with st.sidebar:
    st.header("Example Questions")
    
    example_questions = [
        "What does EVA do?",
        "Tell me about CAM",
        "How does PHIL work?",
        "What are the benefits?",
        "Tell me about Thoughtful AI's agents"
    ]
    
    for question in example_questions:
        if st.button(question, key=question):
            st.session_state.messages.append({"role": "user", "content": question})
            response = agent.get_response(question)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()
    
    st.divider()
    
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()