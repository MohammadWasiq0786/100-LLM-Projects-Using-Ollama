"""
Project 48. Story Prompt Generator

Description:
This tool sparks creativity by generating unique story prompts based on your chosen genre or theme. 
Whether you’re writing fantasy, sci-fi, horror, or romance, it gives you a starting idea to inspire your next masterpiece.
"""

import ollama
import os
import gradio as gr
 
 
# Function to generate a creative story prompt
def generate_prompt(genre):
    # System message for the AI to act as a creative writing muse
    messages = [
        {
            "role": "system",
            "content": (
                f"You are a creative writing assistant. Generate a unique and intriguing story prompt for the '{genre}' genre. "
                "Make sure it inspires curiosity and imagination, but keep it brief (2-4 sentences max)."
            )
        },
        {
            "role": "user",
            "content": f"Give me a {genre} writing prompt."
        }
    ]
 
    try:
        # Call Ollama to get a story idea
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return the story prompt
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface for story prompts
iface = gr.Interface(
    fn=generate_prompt,
    inputs=gr.Dropdown(["fantasy", "sci-fi", "romance", "mystery", "horror", "dystopian", "historical fiction", "random"], label="Choose a Genre"),
    outputs="text",
    title="📚 Story Prompt Generator",
    description="Pick a genre and I’ll generate a creative writing prompt to kickstart your next story!"
)
 
# Launch the storytelling assistant
iface.launch()