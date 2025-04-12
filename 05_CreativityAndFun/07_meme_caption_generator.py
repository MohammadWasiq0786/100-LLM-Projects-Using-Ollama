"""
Project 47. Meme Caption Generator

Description:
This witty little tool creates meme captions based on an image description or mood. 
Whether it’s relatable, savage, wholesome, or dark humor—you’ll get scroll-stopping lines to pair with your favorite memes.
"""

import ollama
import os
import gradio as gr
 
 
# Function to generate a meme caption
def generate_meme_caption(image_description, humor_style):
    # Prompt AI to act like a meme expert
    messages = [
        {
            "role": "system",
            "content": (
                f"You are a creative meme generator. Based on the image description, write 2-3 witty, short captions "
                f"in a {humor_style} style. Be clever, punchy, and internet-savvy."
            )
        },
        {
            "role": "user",
            "content": f"Image description: {image_description}"
        }
    ]
 
    try:
        # Request meme captions from Ollama
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return generated captions
        return response['message']['content'].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface for generating meme captions
iface = gr.Interface(
    fn=generate_meme_caption,
    inputs=[
        gr.Textbox(label="Describe the Meme Image (e.g. cat staring at laptop, dog in sunglasses)"),
        gr.Radio(["relatable", "dark humor", "wholesome", "roast", "random"], label="Humor Style")
    ],
    outputs="text",
    title="😆 Meme Caption Generator",
    description="Describe your meme pic and choose a humor style—I’ll generate funny captions ready for posting!"
)
 
# Launch the meme tool
iface.launch()