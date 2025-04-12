"""
Project 15. Meeting Notes Summarizer

Description:
This tool takes raw meeting notes or transcriptions and summarizes them into key decisions, action items, and 
major discussion points. It’s ideal for professionals who want clean summaries without reading through messy minutes or call logs.
"""


import ollama
import gradio as gr
import os

# Function to summarize raw meeting notes
def summarize_meeting_notes(notes_text):
    # System prompt that sets the AI's behavior
    messages = [
        {
            "role": "system",
            "content": (
                "You are an expert executive assistant. Read raw meeting notes or transcripts and summarize the key points, "
                "decisions made, and action items. Structure the output clearly using bullet points or sections. "
                "Be concise and formal, suitable for business documentation."
            )
        },
        {
            "role": "user",
            "content": f"Please summarize the following meeting notes:\n\n{notes_text}"
        }
    ]
 
    try:
        # Call Ollama model to generate the summary
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return the formatted summary
        return response["message"]["content"].strip()
 
    except Exception as e:
        # Return error message if something goes wrong
        return f"Error: {str(e)}"
 
# Gradio interface for pasting meeting notes
iface = gr.Interface(
    fn=summarize_meeting_notes,                      # Summarization function
    inputs=gr.Textbox(lines=15, placeholder="Paste your meeting notes or transcript here..."),
    outputs="text",                                  # Display summarized output
    title="📋 Meeting Notes Summarizer",             # App title
    description=(
        "Paste in raw meeting notes, messy bullet points, or a transcript. "
        "Get a clean summary with decisions, action items, and highlights."
    )
)
 
# Launch the app
iface.launch()
