import streamlit as st
from streaming_backend import chatbot
from langchain_core.messages import HumanMessage

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

    /* Main app */
    .stApp {
        background-color: #0e1117;
    }

    /* Header */
    .chat-header {
        text-align: center;
        padding: 20px 0 10px 0;
    }

    .chat-header h1 {
        font-size: 32px;
        margin-bottom: 5px;
    }

    .chat-header p {
        color: #9ca3af;
        font-size: 15px;
    }

    /* User message */
    [data-testid="stChatMessage"] {
        border-radius: 15px;
        padding: 10px;
        margin-bottom: 10px;
    }

    /* Chat input */
    [data-testid="stChatInput"] {
        border-radius: 20px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #111827;
    }

    .sidebar-title {
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 20px;
    }

</style>
""", unsafe_allow_html=True)


# -----------------------------
# Header
# -----------------------------
st.markdown("""
<div class="chat-header">
    <h1>🤖 AI Assistant</h1>
    <p>Powered by LangGraph + Groq</p>
</div>
""", unsafe_allow_html=True)


# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">💬 AI Chat</div>',
        unsafe_allow_html=True
    )

    st.markdown("### Conversation")

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.message_history = []
        st.rerun()

    st.divider()

    st.markdown("### Features")
    st.markdown("""
    - ⚡ Streaming responses
    - 🧠 LangGraph memory
    - 💬 Conversational AI
    - 🔄 Thread-based sessions
    """)


# -----------------------------
# Thread Configuration
# -----------------------------
config = {
    "configurable": {
        "thread_id": "abhi_1"
    }
}


# -----------------------------
# Initialize Message History
# -----------------------------
if "message_history" not in st.session_state:
    st.session_state.message_history = []


# -----------------------------
# Display Previous Messages
# -----------------------------
for message in st.session_state.message_history:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# -----------------------------
# Chat Input
# -----------------------------
user_input = st.chat_input(
    "Message your AI assistant..."
)


# -----------------------------
# Process User Input
# -----------------------------
if user_input:

    # Store user message
    st.session_state.message_history.append({
        "role": "user",
        "content": user_input
    })

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Display assistant response
    with st.chat_message("assistant"):

        ai_message = st.write_stream(
            message_chunk.content
            for message_chunk, metadata
            in chatbot.stream(
                {
                    "messages": [
                        HumanMessage(content=user_input)
                    ]
                },
                config=config,
                stream_mode="messages"
            )
        )

    # Store assistant response
    st.session_state.message_history.append({
        "role": "assistant",
        "content": ai_message
    })