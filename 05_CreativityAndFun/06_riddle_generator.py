"""
Project 46. Riddle Generator

Description:
This brainy bot generates original riddles based on themes you choose—like logic, animals, numbers, or wordplay. 
It's great for kids, quizzes, escape rooms, or just for a fun mental workout.
"""

import ollama
import os
import gradio as gr
 

# Function to generate a themed riddle
def generate_riddle(theme):
    # Prompt the AI to act like a riddle master
    messages = [
        {
            "role": "system",
            "content": (
                f"You are a clever riddle master. Create a short, original riddle based on the theme '{theme}'. "
                "The riddle should be clear, solvable, and fun. Provide the riddle first, then the answer below it."
            )
        },
        {
            "role": "user",
            "content": "Please give me a riddle."
        }
    ]
 
    try:
        # Request a riddle from Ollama
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return riddle
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface for riddle generation
iface = gr.Interface(
    fn=generate_riddle,
    inputs=gr.Radio(["logic", "math", "animal", "wordplay", "mystery", "random"], label="Choose a Riddle Theme"),
    outputs="text",
    title="🧩 Riddle Generator",
    description="Pick a theme and I’ll give you a clever riddle with its answer. Great for games, fun challenges, and brain teasers!"
)
 
# Launch the app
iface.launch()