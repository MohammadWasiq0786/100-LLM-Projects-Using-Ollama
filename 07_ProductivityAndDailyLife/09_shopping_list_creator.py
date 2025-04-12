"""
Project 69. Shopping List Creator

Description:
This handy assistant creates a detailed shopping list based on your meal plan, dietary needs, or general preferences. 
It can categorize items (e.g. produce, dairy, pantry), estimate quantities, and even suggest budget swaps.
"""

import ollama
import os
import gradio as gr

 
# Function to generate shopping list
def generate_shopping_list(meal_ideas_or_diet, for_how_many_days):
    # Prompt to behave like a smart grocery planner
    messages = [
        {
            "role": "system",
            "content": (
                f"You are a smart shopping list generator. Based on the user's dietary preference or meal plan and the number of days, "
                f"create a shopping list categorized by type (Produce, Protein, Dairy, Grains, Snacks, Misc). "
                f"Estimate quantities needed and avoid unnecessary items."
            )
        },
        {
            "role": "user",
            "content": f"Meal Preferences or Diet: {meal_ideas_or_diet}\nShopping for: {for_how_many_days} days"
        }
    ]
 
    try:
        # Get shopping list from Ollama
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return organized shopping list
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface for the shopping list generator
iface = gr.Interface(
    fn=generate_shopping_list,
    inputs=[
        gr.Textbox(label="Meal Plan / Dietary Preference (e.g. vegetarian, weekly meals, high protein)"),
        gr.Slider(1, 14, step=1, label="Number of Days")
    ],
    outputs="text",
    title="🛍️ Shopping List Creator",
    description="Enter your meals or dietary style, and I’ll give you a categorized shopping list with smart quantity estimates."
)
 
# Launch the list builder
iface.launch()