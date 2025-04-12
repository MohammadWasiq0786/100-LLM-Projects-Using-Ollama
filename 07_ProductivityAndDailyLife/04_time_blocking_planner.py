"""
Project 64. Time Blocking Planner

Description:
This tool turns your to-do list into a time-blocked daily schedule. It helps you plan your day hour-by-hour, ensuring focused work sessions, 
buffer breaks, and smart energy use. Great for deep work, students, or busy professionals.
"""

import ollama
import os
import gradio as gr
 
 
# Function to generate time-blocked plan
def generate_time_blocks(tasks, start_hour, end_hour):
    # Prompt AI to act like a time management coach
    messages = [
        {
            "role": "system",
            "content": (
                "You are a smart scheduling assistant. Take the list of tasks and distribute them into hourly time blocks between "
                f"{start_hour}:00 and {end_hour}:00. Each task should be matched with a time slot based on its estimated effort. "
                "Include 5–10 min buffer breaks. Return the result in a clear schedule format. If time is short, suggest splitting or deferring tasks."
            )
        },
        {
            "role": "user",
            "content": f"My tasks: {tasks}"
        }
    ]
 
    try:
        # Call Ollama
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return time-blocked schedule
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio UI for input/output
iface = gr.Interface(
    fn=generate_time_blocks,
    inputs=[
        gr.Textbox(label="Tasks with durations (e.g. Write report - 1h, Check email - 30m)"),
        gr.Slider(minimum=5, maximum=12, step=1, label="Start Hour (24hr format)", value=9),
        gr.Slider(minimum=12, maximum=22, step=1, label="End Hour (24hr format)", value=17)
    ],
    outputs="text",
    title="⏰ Time Blocking Planner",
    description="Enter your tasks and available hours. I’ll break your day into focused blocks with smart scheduling."
)
 
# Launch the planner
iface.launch()