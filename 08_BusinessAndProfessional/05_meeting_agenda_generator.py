"""
Project 75. Meeting Agenda Generator

Description:
This assistant helps you craft a well-structured meeting agenda based on the purpose, attendees, and time constraints. 
It includes topics, time blocks, and action goals—perfect for keeping meetings on track and outcome-driven.
"""

import ollama
import os
import gradio as gr
 
 
# Function to generate meeting agenda
def generate_meeting_agenda(meeting_type, attendees, duration):
    # Prompt AI to act like a meeting planning assistant
    messages = [
        {
            "role": "system",
            "content": (
                "You are a meeting planning assistant. Based on the meeting type, attendee roles, and total duration, "
                "create a clear agenda. Include topic headings, estimated time blocks, a goal for the meeting, and any prep materials if relevant. "
                "Keep it organized and professional."
            )
        },
        {
            "role": "user",
            "content": (
                f"Meeting Type: {meeting_type}\n"
                f"Attendees: {attendees}\n"
                f"Total Duration: {duration} minutes"
            )
        }
    ]
 
    try:
        # Generate the agenda with Ollama
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
        return response["message"]["content"].strip()
    
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface
iface = gr.Interface(
    fn=generate_meeting_agenda,
    inputs=[
        gr.Textbox(label="Type of Meeting (e.g. Sprint Review, Product Brainstorm, Sales Sync)"),
        gr.Textbox(label="Who’s Attending? (e.g. Devs, Designers, PMs)"),
        gr.Slider(15, 120, step=5, label="Total Duration (minutes)")
    ],
    outputs="text",
    title="🗓️ Meeting Agenda Generator",
    description="Describe the meeting and attendees, and I’ll give you a structured agenda with time blocks and clear goals."
)
 
# Launch the agenda planner
iface.launch()