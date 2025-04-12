"""
Project 73. Cold Outreach Assistant

Description:
This tool helps you craft effective cold emails or messages that feel personalized, respectful, and compelling. 
Whether you're reaching out for partnerships, jobs, networking, or lead generation, it structures the message 
to maximize response rate.
"""


import ollama
import os
import gradio as gr
 
 
# Function to generate cold outreach message
def generate_outreach(role, purpose, tone):
    # Prompt the AI to act like a networking and outreach expert
    messages = [
        {
            "role": "system",
            "content": (
                "You are a cold outreach writing assistant. Craft a concise and respectful cold email or LinkedIn message. "
                "Focus on building rapport, explaining the purpose clearly, and ending with a soft CTA (call to action). "
                "Make sure it’s not spammy. Keep the tone in line with the user's intent."
            )
        },
        {
            "role": "user",
            "content": (
                f"Who I'm reaching out to: {role}\n"
                f"Reason: {purpose}\n"
                f"Tone: {tone}"
            )
        }
    ]
 
    try:
        # Generate the outreach message
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
        return response["message"]["content"].strip()
    
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface
iface = gr.Interface(
    fn=generate_outreach,
    inputs=[
        gr.Textbox(label="Who Are You Contacting? (e.g. CTO at a startup, recruiter on LinkedIn)"),
        gr.Textbox(label="Why Are You Reaching Out? (e.g. job opportunity, collaboration, pitch)"),
        gr.Radio(["Professional", "Casual", "Respectful", "Friendly"], label="Tone of Message")
    ],
    outputs="text",
    title="📬 Cold Outreach Assistant",
    description="Enter your intent and audience—I’ll help you write a respectful, compelling message to spark a reply."
)
 
# Launch the outreach assistant
iface.launch()