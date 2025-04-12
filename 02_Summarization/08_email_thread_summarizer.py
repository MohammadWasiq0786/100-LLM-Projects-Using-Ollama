"""
Project 18. Email Thread Summarizer

Description:
This tool summarizes long, back-and-forth email threads into a concise overview—highlighting who said what, 
key decisions, and action items. It’s perfect for busy professionals who need to catch up on emails quickly without 
reading everything line by line.
"""


import ollama
import os
import gradio as gr
 
# Load the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
 
# Function to summarize an email thread
def summarize_email_thread(thread_text):
    # System prompt helps the model understand the task
    messages = [
        {
            "role": "system",
            "content": (
                "You are an executive assistant. Your job is to read an entire email thread and summarize the discussion, "
                "highlight key points, decisions made, who said what, and any action items. "
                "Be clear, concise, and professional. Use bullet points if helpful."
            )
        },
        {
            "role": "user",
            "content": f"Summarize the following email thread:\n\n{thread_text}"
        }
    ]
 
    try:
        # Send the thread to OpenAI API for summarization
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Extract and return summary
        return response['message']['content'].strip()
 
    except Exception as e:
        # Handle any exceptions
        return f"Error: {str(e)}"
 
# Create a Gradio UI for user to paste email thread
iface = gr.Interface(
    fn=summarize_email_thread,                        # The core summarizer function
    inputs=gr.Textbox(lines=15, placeholder="Paste a full email thread here..."),
    outputs="text",                                   # Output field
    title="📨 Email Thread Summarizer",               # App title
    description=(
        "Paste a long email thread and get a summary of the conversation. "
        "Highlights decisions, participants, and key points. Great for catching up fast!"
    )
)
 
# Launch the app
iface.launch()