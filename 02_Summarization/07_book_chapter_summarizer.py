"""
Project 17. Book Chapter Summarizer

Description:
This tool helps readers digest entire book chapters by providing concise, easy-to-understand summaries. 
Whether you're studying, prepping for a test, or reviewing a novel, it extracts key events, themes, and 
characters from lengthy chapter text.
"""


import ollama
import gradio as gr
import os
 

# Function to summarize book chapter text
def summarize_chapter(chapter_text):
    # System prompt to guide the model like a literature teacher
    messages = [
        {
            "role": "system",
            "content": (
                "You are a book summary expert. Your task is to summarize a chapter from a novel or non-fiction book. "
                "Highlight the key events, main ideas, characters involved, and any important quotes or turning points. "
                "Be clear and educational, but keep the tone light and easy to follow."
            )
        },
        {
            "role": "user",
            "content": f"Summarize this chapter:\n\n{chapter_text}"
        }
    ]
 
    try:
        
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return the assistant’s summary
        return response["message"]["content"].strip()
 
    except Exception as e:
        # Handle any error gracefully
        return f"Error: {str(e)}"
 
# Build a Gradio interface for input/output
iface = gr.Interface(
    fn=summarize_chapter,                           # Function to run
    inputs=gr.Textbox(lines=20, placeholder="Paste a book chapter or section here..."),
    outputs="text",                                 # Summarized output
    title="📘 Book Chapter Summarizer",             # App title
    description=(
        "Paste a chapter from a novel or non-fiction book and get a clear summary. "
        "Includes key ideas, events, and characters. Great for quick reviews or studying!"
    )
)
 
# Launch the app
iface.launch()