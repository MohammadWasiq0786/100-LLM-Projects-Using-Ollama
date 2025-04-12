"""
Project 29. Daily Productivity Planner

Description:
This smart planner helps you organize your day by turning your priorities, schedule, and goals into a focused daily plan. 
It includes time blocks, breaks, habits, and even motivating tips. Great for students, professionals, 
or anyone who wants to beat procrastination.
"""

import ollama
import os
import gradio as gr
 
 
# Function to generate a daily productivity plan
def create_daily_plan(user_input):
    # System prompt that shapes the assistant into a productivity coach
    messages = [
        {
            "role": "system",
            "content": (
                "You are a personal productivity coach. Based on the user's tasks, goals, focus areas, and schedule, "
                "create a well-structured daily plan. Include time blocks, breaks, and tips for staying focused. "
                "Keep it realistic, encouraging, and clear."
            )
        },
        {
            "role": "user",
            "content": f"Here’s what I need to get done today:\n{user_input}"
        }
    ]
 
    try:
        # Make request to Ollma
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return the daily schedule
        return response['message']['content'].strip()
 
    except Exception as e:
        # Return error if something goes wrong
        return f"Error: {str(e)}"
 
# Gradio interface for productivity planner
iface = gr.Interface(
    fn=create_daily_plan,                                # Function to run
    inputs=gr.Textbox(lines=4, placeholder="e.g. 3 meetings, write a report, 1 hour workout, 30 min for reading"),
    outputs="text",                                      # Output the structured day plan
    title="🧠 Daily Productivity Planner",                # App title
    description=(
        "Type your daily priorities or tasks, and I’ll generate a focused, realistic plan with breaks and blocks. "
        "Try: 'Study Python, walk dog, two meetings, and groceries' or 'Finish proposal and gym in evening'."
    )
)
 
# Launch the planner
iface.launch()