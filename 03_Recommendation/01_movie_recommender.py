"""
Project 21. Movie Recommender

Description:
This app gives users personalized movie recommendations based on their mood, favorite genres, or recent watches. 
It acts like a friendly AI film buff—perfect for date nights, weekend binges, or just finding something new to watch.
"""

import ollama
import os
import gradio as gr
 
# Function to generate personalized movie recommendations
def recommend_movies(user_input):
    # System message instructs the model to act like a film recommendation engine
    messages = [
        {
            "role": "system",
            "content": (
                "You are a friendly and knowledgeable movie recommendation engine. "
                "Based on the user's preferences, mood, genre interests, or previous favorites, suggest a few great films to watch. "
                "Include a short description for each and keep the tone fun and helpful."
            )
        },
        {
            "role": "user",
            "content": f"Here’s what I’m in the mood for: {user_input}"
        }
    ]
 
    try:
        # Make a request to the Ollama
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return movie suggestions from the assistant
        return response['message']['content'].strip()
 
    except Exception as e:
        # Handle errors gracefully
        return f"Error: {str(e)}"
 
# Gradio UI for the movie recommender
iface = gr.Interface(
    fn=recommend_movies,                            # Function to run
    inputs=gr.Textbox(lines=2, placeholder="e.g. I want a feel-good comedy or something like Interstellar."),
    outputs="text",                                 # Display recommendations
    title="🎬 Movie Recommender Bot",               # App title
    description=(
        "Tell me what you're in the mood for and I'll suggest movies! "
        "Try: 'I like sci-fi thrillers', 'Feel-good rom-coms', or 'Something like Inception'."
    )
)

# Launch the app
iface.launch()
