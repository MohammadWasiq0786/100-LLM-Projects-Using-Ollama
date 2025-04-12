"""
Project 28. Workout Plan Generator

Description:
This virtual fitness coach creates personalized workout routines based on your fitness goals, available equipment, time commitment, 
and experience level. Whether you’re bulking, cutting, or just starting out—it gives you a plan that fits your lifestyle.
"""

import ollama
import os
import gradio as gr


# Function to create a personalized workout plan
def generate_workout_plan(user_input):
    # System prompt for AI to act like a fitness trainer
    messages = [
        {
            "role": "system",
            "content": (
                "You are a certified fitness trainer. Based on the user's fitness goal, experience level, available equipment, and weekly availability, "
                "create a personalized workout plan. Break it down by day, include exercises, sets, reps, and rest. "
                "Be supportive, clear, and flexible with substitutions."
            )
        },
        {
            "role": "user",
            "content": f"Here's what I need: {user_input}"
        }
    ]
 
    try:
        # Call Ollama to generate the plan
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return the workout plan
        return response["message"]["content"].strip()
 
    except Exception as e:
        # Return any error messages
        return f"Error: {str(e)}"
 
# Gradio interface for the workout plan generator
iface = gr.Interface(
    fn=generate_workout_plan,                             # Function to create workout plans
    inputs=gr.Textbox(lines=3, placeholder="e.g. I want to build muscle at home, 4 days/week, beginner level."),
    outputs="text",                                       # Output the custom workout plan
    title="🏋️ Personalized Workout Plan Generator",       # App title
    description=(
        "Tell me your fitness goals and schedule, and I’ll generate a custom plan. "
        "Try: 'Lose weight with 30-min daily workouts', 'Build muscle with dumbbells only', or 'Full body training for beginners'."
    )
)
 
# Launch the app
iface.launch()