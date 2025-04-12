"""
Project 10. Roleplay Bot (“Pretend You’re a Chef”)

Description:
This project creates a chatbot that roleplays as a specific character. In this example, 
the AI pretends to be a world-class chef who teaches you how to cook, gives you recipes, answers food questions, and 
shares kitchen tips—all with personality and flair. You can customize it to pretend to be anyone (doctor, pirate, wizard, etc.).
"""

import ollama
import gradio as gr
import os


# Define the chatbot function that roleplays as a chef
def chef_bot(user_input):
    # System prompt tells the AI to stay in character as a chef
    messages = [
        {
            "role": "system",
            "content": (
                "You are a passionate and slightly dramatic world-class French-Italian fusion chef named Chef Franco. "
                "You always stay in character. You give cooking tips, gourmet recipes, and food advice with flair and confidence. "
                "Use food metaphors, fun expressions, and chef-like tone in all your answers. Add a bit of sass and showbiz."
            )
        },
        {
            "role": "user",
            "content": user_input  # User can ask anything food/cooking-related
        }
    ]
 
    try:
        # Call OpenAI API to get a roleplayed response
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
        
        # Extract and return the chatbot's reply
        return response['message']['content'].strip()
 
    except Exception as e:
        # Show error if API call fails
        return f"Error: {str(e)}"
 
# Create Gradio interface to interact with the bot
iface = gr.Interface(
    fn=chef_bot,                             # Function to handle response
    inputs="text",                           # Text input from user
    outputs="text",                          # Chef Franco’s glorious reply
    title="🍝 Chef Franco – Roleplay Bot",   # App title
    description=(
        "Talk to Chef Franco, a dramatic world-class chef who answers in style. "
        "Try: 'How do I make the perfect risotto?', 'What spice goes with lamb?', or 'Chef Franco, save my bland soup!'"
    )
)
 
# Launch the app in your browser
iface.launch()