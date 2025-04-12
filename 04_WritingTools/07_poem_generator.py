"""
Project 37. Poem Generator

Description:
This poetic AI writes original poems based on your theme, emotion, or inspiration. 
Whether it’s romantic, funny, deep, or sad—you’ll get a unique, creative poem written in the style you choose.
"""

import ollama
import os
import gradio as gr

 
# Function to generate poems based on theme and style
def generate_poem(theme, style):
    # System prompt tells AI to act as a poet
    messages = [
        {
            "role": "system",
            "content": (
                "You are a creative and thoughtful poet. Write an original poem based on the given theme and tone. "
                "The poem should have depth, flow naturally, and be emotionally engaging. Use imagery and poetic devices as appropriate."
            )
        },
        {
            "role": "user",
            "content": f"Theme: {theme}\nStyle: {style}"
        }
    ]
 
    try:
        # Request a poem from Ollama
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return the poetic piece
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface for poem generation
iface = gr.Interface(
    fn=generate_poem,
    inputs=[
        gr.Textbox(label="Theme (e.g. love, loss, nature, freedom)"),
        gr.Radio(["romantic", "sad", "funny", "deep", "haiku", "rhymed", "free verse"], label="Poem Style")
    ],
    outputs="text",
    title="🌸 Poem Generator",
    description="Enter a theme and pick a style, and I’ll craft a custom poem for you. Great for sharing, gifting, or journaling."
)
 
# Launch your poetry bot
iface.launch()