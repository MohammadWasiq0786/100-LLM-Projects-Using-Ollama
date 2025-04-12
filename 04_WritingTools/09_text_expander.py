"""
Project 39. Text Expander

Description:
This tool takes short ideas, phrases, or bullet points and expands them into complete, clear, and coherent paragraphs. 
Perfect for turning notes into emails, outlines into reports, or thoughts into social posts—instantly.
"""

import ollama
import os
import gradio as gr

 
# Function to expand a short idea into a paragraph
def expand_text(short_input, style):
    # System prompt to guide assistant behavior
    messages = [
        {
            "role": "system",
            "content": (
                f"You are a professional writing assistant. Take a short input and expand it into a detailed, coherent paragraph in a {style} tone. "
                "Make it flow naturally and clearly while retaining the original meaning."
            )
        },
        {
            "role": "user",
            "content": f"Short input: {short_input}"
        }
    ]
 
    try:
        # Generate expanded text from Ollama
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return expanded paragraph
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface for text expansion
iface = gr.Interface(
    fn=expand_text,
    inputs=[
        gr.Textbox(lines=3, label="Short Idea or Sentence (e.g. AI is changing how we work)"),
        gr.Radio(["formal", "casual", "inspirational", "technical"], label="Expansion Style")
    ],
    outputs="text",
    title="🧠 Text Expander",
    description="Turn your brief thoughts into full paragraphs instantly. Great for emails, essays, reports, or content writing!"
)
 
# Launch the expander app
iface.launch()