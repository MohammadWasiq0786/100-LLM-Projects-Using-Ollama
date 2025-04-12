"""
Project 80. Job Description Enhancer

Description:
This tool takes your basic job posting and turns it into a polished, inclusive, and engaging description that 
attracts the right talent. It highlights responsibilities, qualifications, culture fit, and benefits—while keeping 
tone professional and appealing.
"""

import ollama
import os
import gradio as gr


# Function to enhance job description
def enhance_job_description(raw_description, job_title, company_name, tone):
    # Prompt the AI to act as a recruiter/content writer
    messages = [
        {
            "role": "system",
            "content": (
                "You are a professional recruiter and job ad copywriter. Take the raw job description and transform it into a polished, inclusive, and compelling listing. "
                "Include:\n- A short intro about the company\n- Key responsibilities\n- Required skills/qualifications\n- Benefits or perks\n"
                "Use the specified tone and keep it scannable and engaging."
            )
        },
        {
            "role": "user",
            "content": (
                f"Job Title: {job_title}\n"
                f"Company: {company_name}\n"
                f"Tone: {tone}\n"
                f"Raw Description: {raw_description}"
            )
        }
    ]
 
    try:
        # Generate the enhanced job description
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
        return response["message"]["content"].strip()
    
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface
iface = gr.Interface(
    fn=enhance_job_description,
    inputs=[
        gr.Textbox(label="Job Title"),
        gr.Textbox(label="Company Name"),
        gr.Textbox(label="Paste Raw Job Description"),
        gr.Radio(["Professional", "Friendly", "Inclusive", "Excited"], label="Tone")
    ],
    outputs="text",
    title="🧑‍💼 Job Description Enhancer",
    description="Upgrade your job ad into a polished, readable, and attractive post that brings in the right candidates."
)
 
# Launch the enhancer
iface.launch()