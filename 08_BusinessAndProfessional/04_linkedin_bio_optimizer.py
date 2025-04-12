"""
Project 74. LinkedIn Bio Optimizer

Description:
This smart assistant takes your current experience and career goals, then crafts or improves your LinkedIn bio to sound
confident, compelling, and aligned with your aspirations. Great for job seekers, freelancers, and personal branding.
"""

import ollama
import os
import gradio as gr
 
# Function to optimize or create a LinkedIn bio
def optimize_linkedin_bio(current_bio, goals, tone):
    # Prompt the AI to act like a LinkedIn profile coach
    messages = [
        {
            "role": "system",
            "content": (
                "You are a personal branding expert specializing in LinkedIn. Improve or write a new LinkedIn 'About' section "
                "based on the user's experience and career goals. Use the specified tone, keep it concise (2-3 short paragraphs), "
                "and make it sound confident and human—not robotic."
            )
        },
        {
            "role": "user",
            "content": (
                f"My current bio or background: {current_bio}\n"
                f"My goals: {goals}\n"
                f"Tone: {tone}"
            )
        }
    ]
 
    try:
        # Get optimized LinkedIn bio
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
        return response["message"]["content"].strip()
    
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface
iface = gr.Interface(
    fn=optimize_linkedin_bio,
    inputs=[
        gr.Textbox(label="Paste Your Current Bio or Describe Your Experience"),
        gr.Textbox(label="What Are Your Career Goals?"),
        gr.Radio(["Professional", "Aspirational", "Casual", "Confident"], label="Tone")
    ],
    outputs="text",
    title="💼 LinkedIn Bio Optimizer",
    description="Get a stronger, clearer, and more aligned LinkedIn bio that reflects who you are and where you're going."
)
 
# Launch the optimizer
iface.launch()