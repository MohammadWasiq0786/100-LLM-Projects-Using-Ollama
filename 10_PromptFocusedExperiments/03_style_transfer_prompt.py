"""
Project 93. Style Transfer Prompt (e.g., rewrite as Shakespeare)

Description:
This app rewrites your input text in a completely different style—like Shakespearean drama, pirate slang, Gen Z speak, or even Yoda talk. 
It’s a fun way to experiment with tone, voice, and creative prompt engineering.
"""

import os
import ollama
import gradio as gr
  
# Function to perform style transfer
def style_transfer(text, style):
    try:
        # Prompt engineering to enforce style
        prompt = (
            f"Rewrite the following text in the style of {style}:\n\n"
            f"Original:\n{text}\n\n"
            f"{style} version:"
        )
 
        # Get styled response
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=[{"role": "user", "content": prompt}]
        )
 
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface
iface = gr.Interface(
    fn=style_transfer,
    inputs=[
        gr.Textbox(label="Text to Rewrite"),
        gr.Dropdown(
            ["Shakespeare", "Pirate", "Yoda", "Gen Z", "Old English", "Corporate Buzzwords", "Poetic", "Sci-Fi Futuristic"],
            label="Select Style"
        )
    ],
    outputs="text",
    title="🎭 Style Transfer Prompt",
    description="Rewrite any text in a creative or humorous style. Try Shakespeare, Yoda, Gen Z, and more!"
)
 
# Launch the app
iface.launch()