"""
Project 30. Restaurant Recommender

Description:
This chatbot recommends restaurants based on your cravings, location, budget, and vibe. Whether you're in the mood for sushi, 
brunch with friends, or a romantic dinner—this foodie assistant gives curated suggestions and ambiance tips too!
"""

import ollama
import os
import gradio as gr
 
# Function to generate restaurant recommendations
def recommend_restaurants(user_input):
    # System message tells the model to act like a foodie concierge
    messages = [
        {
            "role": "system",
            "content": (
                "You are a local foodie and restaurant concierge. Based on a user's cravings, budget, dietary preferences, or location, "
                "suggest restaurants with a short description for each. Include the type of cuisine, ambiance, and what to try. "
                "If the user doesn't specify a location, give general suggestions."
            )
        },
        {
            "role": "user",
            "content": f"I'm looking for a place to eat: {user_input}"
        }
    ]
 
    try:
        # Call Ollama to get dining recommendations
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return the curated restaurant picks
        return response['message']['content'].strip()
 
    except Exception as e:
        # Handle any errors during the API call
        return f"Error: {str(e)}"
 
# Gradio interface for restaurant recommendation bot
iface = gr.Interface(
    fn=recommend_restaurants,                                # Function to run
    inputs=gr.Textbox(lines=2, placeholder="e.g. I'm in NYC, craving Korean BBQ, not too pricey"), 
    outputs="text",                                           # Display restaurant list
    title="🍴 Restaurant Recommender",                        # App title
    description=(
        "Tell me what you’re in the mood for and I’ll suggest a few great restaurants. "
        "Try: 'Vegan spots in LA under $20', 'Romantic Italian dinner in Chicago', or 'Best ramen in Tokyo'."
    )
)
 
# Launch the restaurant recommender
iface.launch()