"""
Project 40. Text Condenser

Description:
This tool takes long paragraphs or documents and condenses them into short, clear summaries. Ideal for students, professionals, or 
anyone who wants to shrink verbose content into key points or TL;DRs.
"""

import ollama
import os
import gradio as gr
 
# Load OpenAI API key securely
openai.api_key = os.getenv("OPENAI_API_KEY")
 
# Function to condense long text into shorter summaries
def condense_text(long_input, format_style):
    # Set assistant behavior as a summarizer
    messages = [
        {
            "role": "system",
            "content": (
                f"You are a professional summarizer. Condense the following text into a {format_style} summary. "
                "Keep the important meaning intact and use clear language."
            )
        },
        {
            "role": "user",
            "content": long_input
        }
    ]
 
    try:
        # Send to Ollama
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return the condensed summary
        return response['message']['content'].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface setup
iface = gr.Interface(
    fn=condense_text,                                         # Condense function
    inputs=[
        gr.Textbox(lines=10, label="Paste Long Text Here"),   # Input for long content
        gr.Radio(["bullet points", "short paragraph", "one-liner"], label="Summary Format")
    ],
    outputs="text",
    title="🔽 Text Condenser",
    description="Paste in any long content and get a condensed version. Choose whether you want a one-liner, bullet points, or a short summary."
)
 
# Launch the tool
iface.launch()