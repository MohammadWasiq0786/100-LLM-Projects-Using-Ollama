"""
Project 25. Recipe Suggestion Tool

Description:
This AI-powered tool suggests tasty recipes based on your ingredients, dietary preferences, or cravings. 
Whether you’re working with leftovers, eating vegan, or just want something quick and healthy—this bot serves up fresh ideas in seconds.
"""


import ollama
import os
import gradio as gr
 

 
# Core function to suggest recipes
def suggest_recipes(user_input):
    # Set system instructions to guide AI as a creative cook
    messages = [
        {
            "role": "system",
            "content": (
                "You are a creative recipe developer. Based on the user's input (available ingredients, cravings, or dietary preferences), "
                "suggest 2-3 recipes. For each, include the name, a short description, and key ingredients. "
                "Make the tone warm, fun, and helpful like a friendly chef!"
            )
        },
        {
            "role": "user",
            "content": f"I want to cook something with: {user_input}"
        }
    ]
 
    try:
        # Send the prompt to the Ollama
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return the recipe suggestions
        return response["message"]["content"].strip()
 
    except Exception as e:
        # Handle and display any errors
        return f"Error: {str(e)}"
 
# Gradio interface to take input and show recipes
iface = gr.Interface(
    fn=suggest_recipes,                             # Function that handles recipe generation
    inputs=gr.Textbox(lines=2, placeholder="e.g. chicken, rice, spinach | or 'I'm vegan and love spicy food'"),
    outputs="text",                                 # Output area for recipes
    title="🍽️ AI Recipe Suggestion Tool",           # App title
    description=(
        "Tell me what you have or what you're craving, and I’ll give you 2-3 recipe ideas! "
        "Try: 'I have eggs, tomatoes, and cheese' or 'Give me a gluten-free dessert'."
    )
)
 
# Launch the app
iface.launch()