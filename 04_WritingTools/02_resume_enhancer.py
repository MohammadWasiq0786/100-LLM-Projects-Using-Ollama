"""
Project 32. Resume Enhancer

Description:
This tool takes plain or basic resume bullet points and rewrites them to be more impactful, professional, and tailored to the job market. 
Great for job seekers aiming to stand out with strong, action-driven language and quantifiable achievements.
"""

import ollama
import os
import gradio as gr
 
 
# Function to enhance resume content
def enhance_resume(resume_text, job_type):
    # System prompt instructs assistant to act as a resume optimizer
    messages = [
        {
            "role": "system",
            "content": (
                f"You are a professional resume writing assistant. Improve the following resume text for a {job_type} role. "
                "Use strong action verbs, quantify results if possible, and keep the tone concise, confident, and achievement-focused."
            )
        },
        {
            "role": "user",
            "content": resume_text
        }
    ]
 
    try:
        # Call Ollama
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return the improved version
        return response["message"]["content"].strip()
 
    except Exception as e:
        # Return any error messages
        return f"Error: {str(e)}"
 
# Gradio interface setup
iface = gr.Interface(
    fn=enhance_resume,                                           # Core enhancer function
    inputs=[
        gr.Textbox(lines=8, label="Paste Your Resume Text"),    # Resume input
        gr.Textbox(label="Target Job Role or Industry")          # Target job for tailoring
    ],
    outputs="text",                                              # Output improved text
    title="💼 Resume Enhancer",
    description="Paste your resume bullet points and specify your target job. Get polished, impact-driven, and tailored resume lines."
)
 
# Launch the resume enhancer
iface.launch()