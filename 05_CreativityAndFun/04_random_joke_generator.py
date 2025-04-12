"""
Project 44. Random Joke Generator

Description:
This cheerful little app delivers random jokes on demand—ranging from dad jokes and puns to witty one-liners and geeky humor. 
A perfect pick-me-up when you need a laugh, or a great addition to any light-hearted app!
"""

import ollama
import os
import gradio as gr
 
 
# Function to generate a random joke
def get_joke(joke_type):
    # System prompt sets the humor style
    messages = [
        {
            "role": "system",
            "content": (
                f"You are a joke-telling assistant. Tell a single funny, family-friendly joke in the style of {joke_type}. "
                "Keep it short and clean."
            )
        },
        {
            "role": "user",
            "content": "Tell me a joke!"
        }
    ]
 
    try:
        # Request a joke from Ollama
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return the joke
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface for choosing joke style
iface = gr.Interface(
    fn=get_joke,
    inputs=gr.Radio(["dad joke", "pun", "geeky", "random", "witty", "knock-knock"], label="Pick Your Joke Style"),
    outputs="text",
    title="😂 Random Joke Generator",
    description="Select your joke style and get ready to laugh. Family-friendly, AI-powered humor delivered in seconds!"
)
 
# Launch the joke app
iface.launch()