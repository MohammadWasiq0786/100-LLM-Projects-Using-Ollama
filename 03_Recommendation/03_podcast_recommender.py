"""
Project 23. Podcast Recommender

Description:
This AI assistant suggests podcast episodes or shows based on your mood, interests, or favorite creators. 
Whether you’re into tech news, mindfulness, business insights, or true crime—this bot curates great listens just for you.
"""

import ollama
import os
import gradio as gr
 
 
# Function to recommend podcasts based on user input
def recommend_podcasts(user_input):
    # System role prompt to guide the assistant
    messages = [
        {
            "role": "system",
            "content": (
                "You are a podcast curator. Recommend top-rated podcast episodes or shows based on the user's preferences. "
                "Include the show name, a standout episode (if possible), the topic/theme, and a short description for each suggestion. "
                "Be casual, informative, and enthusiastic."
            )
        },
        {
            "role": "user",
            "content": f"I'm interested in: {user_input}"
        }
    ]
 
    try:
        # Make a request to Ollama API
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return podcast suggestions
        return response["choices"][0]["message"]["content"].strip()
 
    except Exception as e:
        # Handle API or network errors
        return f"Error: {str(e)}"
 
# Gradio web UI for podcast recommendations
iface = gr.Interface(
    fn=recommend_podcasts,                          # The function that returns podcast picks
    inputs=gr.Textbox(lines=2, placeholder="e.g. I like tech news, true crime, or something about mindset."),
    outputs="text",                                 # Display the recommendations
    title="🎧 Podcast Recommender Bot",             # Title of the app
    description=(
        "Tell me what kind of podcasts you're in the mood for, and I'll suggest a few top episodes or shows. "
        "Try: 'Funny entrepreneurship podcasts', 'Short daily news recaps', or 'True crime stories like Serial'."
    )
)
 
# Launch the app
iface.launch()