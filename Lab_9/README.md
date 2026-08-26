# Lab 9: Streaming Chatbot

This lab contains a Streamlit chatbot powered by LangGraph and Groq.

## Requirements

- Python 3.10 or newer
- A Groq API key

## Setup

Open a terminal in the repository root and move to the Lab 9 application folder:

```bash
cd "Lab_9/streaming_code"
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required packages:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Configure the Groq API key

The chatbot uses the `GROQ_API_KEY` value in the Python files. Replace the example value with your own Groq API key before starting the app. Do not commit or share API keys.

## Run the streaming chatbot

Start the main Streamlit application:

```bash
streamlit run streaming_frontend.py
```

Open the URL shown in the terminal, usually:

```text
http://localhost:8501
```

Use the chat box to send a message. Stop the application with `Ctrl+C` in the terminal.

## Run the simple chatbot

An alternative, non-LangGraph interface is also available:

```bash
streamlit run streamlit_chatbot.py
```

## Troubleshooting

- Run Streamlit files with `streamlit run ...`, not `python ...`.
- If port `8501` is already in use, run `streamlit run streaming_frontend.py --server.port 8502`.
- If a package is missing, activate `.venv` and run `python -m pip install -r requirements.txt` again.