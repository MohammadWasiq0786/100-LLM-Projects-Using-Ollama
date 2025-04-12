"""
Project 60. Personalized Learning Plan Creator

Description:
This AI tool builds a customized study plan for any topic or goal—like “Learn Python in 30 days” or “Prepare for TOEFL in 4 weeks.” 
It breaks the goal into milestones, creates a weekly or daily plan, and offers tips and resources to stay on track.
"""

import ollama
import os
import gradio as gr
 

# Function to generate a personalized learning plan
def create_learning_plan(goal, duration_weeks, learning_style):
    # Prompt the AI to behave like an educational coach
    messages = [
        {
            "role": "system",
            "content": (
                "You are an expert learning coach. Based on the user's goal, available time, and preferred learning style, "
                "create a structured weekly learning plan. Include milestones, suggested topics or modules, and tips for staying on track. "
                "Be motivating and clear."
            )
        },
        {
            "role": "user",
            "content": (
                f"My goal is: {goal}\n"
                f"I have {duration_weeks} weeks to study.\n"
                f"My learning style is: {learning_style}"
            )
        }
    ]
 
    try:
        # Get plan from Ollama
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return the learning plan
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface
iface = gr.Interface(
    fn=create_learning_plan,
    inputs=[
        gr.Textbox(label="What do you want to learn? (e.g. Python, Web Dev, GRE Prep)"),
        gr.Slider(1, 24, step=1, label="How many weeks do you have?"),
        gr.Radio(["visual", "auditory", "reading/writing", "hands-on"], label="Preferred Learning Style")
    ],
    outputs="text",
    title="🎯 Personalized Learning Plan Creator",
    description="Get a custom study plan with goals, milestones, and tips tailored to your learning style and timeline."
)
 
# Launch the learning planner
iface.launch()