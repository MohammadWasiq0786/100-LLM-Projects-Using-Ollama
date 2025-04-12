"""
Project 20. Twitter Thread Summarizer

Description:
This tool takes a long Twitter thread and condenses it into a short, readable summary. 
It’s especially useful for summarizing viral threads, educational explainers, or commentary across multiple tweets.
"""

import ollama
import os
import gradio as gr
 
# Function to summarize a Twitter thread
def summarize_thread(thread_text):
    # Define the assistant's role using a system prompt
    messages = [
        {
            "role": "system",
            "content": (
                "You are a Twitter thread summarizer. Your task is to take long Twitter threads and summarize them clearly. "
                "Capture the main message, key ideas, and takeaways without copying tweet-by-tweet. "
                "Format it like a TL;DR or key points list."
            )
        },
        {
            "role": "user",
            "content": f"Summarize this Twitter thread:\n\n{thread_text}"
        }
    ]
 
    try:
        # Send the conversation to Ollama's model
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Extract and return the summary
        return response["message"]["content"].strip()
 
    except Exception as e:
        # Return error message if API call fails
        return f"Error: {str(e)}"
 
# Gradio app interface
iface = gr.Interface(
    fn=summarize_thread,                           # Core summarization function
    inputs=gr.Textbox(lines=15, placeholder="Paste a full Twitter thread here..."),
    outputs="text",                                # Display summarized output
    title="🐦 Twitter Thread Summarizer",          # App title
    description=(
        "Paste a full Twitter thread (copy/paste all tweets) and get a short, easy-to-read summary. "
        "Great for educational, business, or viral threads."
    )
)
 
# Launch the app
iface.launch()
