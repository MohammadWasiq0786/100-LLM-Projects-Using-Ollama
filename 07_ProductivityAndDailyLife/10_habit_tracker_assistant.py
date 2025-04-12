"""
Project 70. Habit Tracker Assistant

Description:
This assistant helps you define and track daily habits, giving reminders, motivation, and weekly summaries. 
You can input goals like “drink water,” “read 20 minutes,” or “stretch in the morning,” and 
it’ll turn them into a plan with streak-tracking potential.
"""

import ollama
import os
import gradio as gr

 
# Function to generate a habit tracking plan
def generate_habit_tracker(habits, duration_days):
    # Prompt the AI to behave like a habit coach
    messages = [
        {
            "role": "system",
            "content": (
                "You are a motivational habit tracker assistant. Based on the user's list of habits and number of days, "
                "create a clear habit tracking chart, motivational tips, and weekly summary goals. Include checkboxes or streak-style tracking suggestions."
            )
        },
        {
            "role": "user",
            "content": f"My habits: {habits}\nDuration: {duration_days} days"
        }
    ]
 
    try:
        # Call Ollama to generate the tracker
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return tracker instructions
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface
iface = gr.Interface(
    fn=generate_habit_tracker,
    inputs=[
        gr.Textbox(label="List Your Habits (e.g. Read 10 mins, Drink 2L water, Meditate)"),
        gr.Slider(7, 30, step=1, label="Tracking Duration (Days)")
    ],
    outputs="text",
    title="✅ Habit Tracker Assistant",
    description="Enter your habits and duration, and I’ll build a tracker plan with motivational suggestions and streak tracking ideas."
)
 
# Launch the habit assistant
iface.launch()