"""
Project 16. Legal Contract Summarizer

Description:
This tool reads long, complex legal contracts and breaks them down into simplified summaries. 
It focuses on highlighting obligations, rights, terms, and risks—perfect for non-lawyers who want to understand 
what they’re signing without reading 20 pages of legalese.
"""

import ollama
import gradio as gr
import os


# Function that summarizes legal text
def summarize_contract(legal_text):
    # System prompt sets the assistant's tone and responsibility
    messages = [
        {
            "role": "system",
            "content": (
                "You are a professional legal assistant. Read and summarize legal contracts in plain language. "
                "Highlight key clauses like payment terms, duration, obligations, rights, risks, and any legal consequences. "
                "Use simple and neutral language, suitable for non-lawyers. Do not offer legal advice."
            )
        },
        {
            "role": "user",
            "content": f"Please summarize this contract:\n\n{legal_text}"
        }
    ]
 
    try:
        
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return summarized content
        return response['message']['content'].strip()
 
    except Exception as e:
        # Error handling
        return f"Error: {str(e)}"
 
# Gradio UI for legal contract input
iface = gr.Interface(
    fn=summarize_contract,                       # Core function to summarize
    inputs=gr.Textbox(lines=20, placeholder="Paste your contract text here..."),  # Long input field
    outputs="text",                              # Output simplified summary
    title="📑 Legal Contract Summarizer",        # App title
    description=(
        "Paste a legal contract, terms of service, or agreement and receive a simple summary. "
        "Perfect for understanding obligations and clauses without the legal jargon."
    )
)
 
# Launch the app
iface.launch()