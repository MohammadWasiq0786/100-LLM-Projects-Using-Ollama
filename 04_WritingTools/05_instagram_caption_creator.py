"""
Project 35. Instagram Caption Creator

Description:
This tool generates creative, witty, or aesthetic Instagram captions based on your photo description or vibe. 
Whether it’s a travel shot, food post, gym mirror selfie, or a moody sunset—you’ll get scroll-worthy captions in seconds.
"""

import ollama
import os
import gradio as gr
 
 
# Function to generate Instagram captions
def generate_caption(photo_description, style):
    # System prompt for a social media assistant
    messages = [
        {
            "role": "system",
            "content": (
                f"You are an Instagram caption expert. Create 3 creative, trendy, and engaging Instagram captions "
                f"based on the given description, using a {style} tone. Feel free to use emojis or hashtags when appropriate."
            )
        },
        {
            "role": "user",
            "content": f"Photo description: {photo_description}"
        }
    ]
 
    try:
        # Call Ollama
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return the list of captions
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface setup
iface = gr.Interface(
    fn=generate_caption,                                         # Core function
    inputs=[
        gr.Textbox(label="Describe Your Photo or Post"),         # Input description
        gr.Radio(["funny", "aesthetic", "inspirational", "sassy"], label="Caption Style")  # Tone choice
    ],
    outputs="text",                                              # Output captions
    title="📸 Instagram Caption Creator",
    description="Describe your post, pick a style, and get 3 fun & catchy captions ready for your feed!"
)
 
# Launch the caption generator
iface.launch()