"""
Project 71. Cover Letter Generator

Description:
This smart assistant writes personalized, professional, and compelling cover letters tailored to the job, company, and 
your experience. Just input a job title, description, and your background—it handles the rest.
"""

import ollama
import os
import gradio as gr
 
 
# Function to generate a custom cover letter
def generate_cover_letter(job_title, job_description, user_background):
    # Prompt the AI to act like a career writing coach
    messages = [
        {
            "role": "system",
            "content": (
                "You are a professional career assistant helping write personalized cover letters. "
                "Use the job title and description to align the candidate’s background. Be concise, confident, and engaging. "
                "The letter should have an intro, skills paragraph, alignment with the role, and a call to action."
            )
        },
        {
            "role": "user",
            "content": (
                f"Job Title: {job_title}\n"
                f"Job Description: {job_description}\n"
                f"My Background: {user_background}"
            )
        }
    ]
 
    try:
        # Generate the letter using Ollama
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio UI
iface = gr.Interface(
    fn=generate_cover_letter,
    inputs=[
        gr.Textbox(label="Job Title (e.g. Software Engineer, Marketing Manager)"),
        gr.Textbox(label="Paste Job Description"),
        gr.Textbox(label="Your Background (skills, experience, achievements)")
    ],
    outputs="text",
    title="📄 Cover Letter Generator",
    description="Provide the job info and your background—I’ll generate a compelling cover letter tailored to the opportunity."
)
 
# Launch the cover letter writer
iface.launch()