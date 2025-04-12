"""
Project 24. Travel Destination Recommender

Description:
This travel-savvy AI recommends destinations based on your interests, season, budget, or travel style. 
Whether you're into adventure, culture, beaches, or food—this bot curates personalized trip ideas with a flair of wanderlust.
"""

import ollama
import os
import gradio as gr
 
# Function to recommend travel destinations
def recommend_destinations(user_input):
    # Set the system's behavior as a world travel advisor
    messages = [
        {
            "role": "system",
            "content": (
                "You are an enthusiastic travel planner. Recommend travel destinations based on a user's interests, "
                "budget, season, or vibe. For each suggestion, include the destination, why it’s a good match, "
                "and 1-2 key activities to do there. Keep your tone adventurous and inspiring."
            )
        },
        {
            "role": "user",
            "content": f"I'm planning a trip and here’s what I want: {user_input}"
        }
    ]
 
    try:
        # Call the Ollama to generate a personalized travel list
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return the generated travel ideas
        return response['message']['content'].strip()
 
    except Exception as e:
        # Return any API or processing errors
        return f"Error: {str(e)}"
 
# Gradio interface for destination recommendation
iface = gr.Interface(
    fn=recommend_destinations,                          # Function to generate destination ideas
    inputs=gr.Textbox(lines=2, placeholder="e.g. I'm on a budget, I love mountains and photography. Traveling in December."),
    outputs="text",                                     # Output field for results
    title="🌍 Travel Destination Recommender",          # App title
    description=(
        "Tell me what kind of trip you’re looking for and I’ll suggest destinations around the world. "
        "Try: 'Warm beach destinations in January', 'Affordable cities for solo travelers', or 'Romantic spots for couples in spring'."
    )
)
 
# Launch the app
iface.launch()