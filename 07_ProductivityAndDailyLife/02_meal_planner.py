"""
Project 62. Meal Planner

Description:
This intelligent meal planner creates daily or weekly menus based on your dietary preferences, restrictions, and goals. 
Whether you want vegetarian, high-protein, keto, or budget meals—it builds a tasty, practical plan with variety and balance.
"""

import ollama
import os
import gradio as gr
 
 
# Function to generate a meal plan
def generate_meal_plan(preferences, days, meals_per_day):
    # Prompt the AI to act like a smart nutritionist
    messages = [
        {
            "role": "system",
            "content": (
                f"You are a meal planning assistant. Create a meal plan based on the user's preferences and number of days. "
                f"Include breakfast, lunch, dinner, and snacks (if meals_per_day > 3). Suggest meals that are balanced, tasty, and easy to prepare. "
                f"List the days with meals in bullet points or table style. Include variety and avoid repeating the same dish."
            )
        },
        {
            "role": "user",
            "content": (
                f"Dietary Preferences: {preferences}\n"
                f"Number of Days: {days}\n"
                f"Meals Per Day: {meals_per_day}"
            )
        }
    ]
 
    try:
        # Call Ollama to generate the plan
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return the meal plan
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface for the meal planner
iface = gr.Interface(
    fn=generate_meal_plan,
    inputs=[
        gr.Textbox(label="Dietary Preferences (e.g. vegetarian, high protein, diabetic, budget-friendly)"),
        gr.Slider(minimum=1, maximum=14, step=1, label="Plan for How Many Days?"),
        gr.Slider(minimum=1, maximum=5, step=1, label="Meals Per Day")
    ],
    outputs="text",
    title="🥗 AI Meal Planner",
    description="Tell me your preferences and I’ll cook up a meal plan for the week—healthy, delicious, and tailored to you!"
)
 
# Launch the meal planner
iface.launch()