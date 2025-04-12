"""
Project 61. To-Do List Generator with Priorities

Description:
This tool takes your tasks and organizes them into a to-do list with urgency and importance ranked. 
It uses Eisenhower-style logic or priority labels like High/Medium/Low to help you focus on what matters most.
"""

import ollama
import os
import gradio as gr

 
# Function to generate to-do list with priorities
def generate_todo_list(task_input, format_type):
    # Prompt the AI to act like a productivity assistant
    messages = [
        {
            "role": "system",
            "content": (
                "You are a productivity assistant. Take the user's list of tasks and organize them into a clear to-do list "
                "with priorities using the chosen format. If using Eisenhower Matrix, label each task as: "
                "'Do First', 'Schedule', 'Delegate', or 'Eliminate'. If using simple priority, rank as: 'High', 'Medium', or 'Low'."
            )
        },
        {
            "role": "user",
            "content": f"Tasks: {task_input}\nUse format: {format_type}"
        }
    ]
 
    try:
        # Call the Ollama
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return organized to-do list
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio Interface
iface = gr.Interface(
    fn=generate_todo_list,
    inputs=[
        gr.Textbox(label="List Your Tasks (separated by commas)"),
        gr.Radio(["Simple Priority (High/Med/Low)", "Eisenhower Matrix"], label="Prioritization Style")
    ],
    outputs="text",
    title="📝 To-Do List Generator with Priorities",
    description="Enter your tasks, and I’ll organize them into a prioritized to-do list using smart productivity logic."
)
 
# Launch the tool
iface.launch()