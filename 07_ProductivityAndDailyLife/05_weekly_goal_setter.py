"""
Project 65. Weekly Goal Setter

Description:
This assistant helps you define clear goals for the week by breaking them down into SMART (Specific, Measurable, Achievable, Relevant, 
Time-bound) tasks. It also suggests a day-by-day plan and motivational prompts to stay on track.
"""

import ollama
import os
import gradio as gr
 
 
# Function to set and plan weekly goals
def create_weekly_goals(main_goals, focus_area):
    # Prompt AI to act like a weekly planning coach
    messages = [
        {
            "role": "system",
            "content": (
                "You are a goal-setting coach. Take the user's main goals and focus area, and break them into a weekly plan. "
                "For each goal:\n- Make it SMART\n- Suggest daily action steps\n- Add motivational quotes or tips\n"
                "Return everything in a clear, day-by-day outline starting from Monday."
            )
        },
        {
            "role": "user",
            "content": f"My goals: {main_goals}\nFocus area: {focus_area}"
        }
    ]
 
    try:
        # Generate goal plan with Ollama
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return the weekly plan
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface
iface = gr.Interface(
    fn=create_weekly_goals,
    inputs=[
        gr.Textbox(label="List Your Main Goals for This Week"),
        gr.Radio(["Work", "Fitness", "Health", "Learning", "Personal Growth", "Mixed"], label="Primary Focus Area")
    ],
    outputs="text",
    title="📅 Weekly Goal Setter",
    description="Set your goals and I’ll break them into a SMART action plan for the week—complete with daily steps and motivation."
)
 
# Launch the weekly planner
iface.launch()