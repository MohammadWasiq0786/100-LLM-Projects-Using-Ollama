"""
Project 45. AI Stand-Up Comedy Writer

Description:
This hilarious tool writes stand-up comedy routines based on your chosen topic and audience style. 
Whether you’re prepping for open mic night, writing a skit, or just love comedy—it delivers punchlines, setups, and 
classic timing with AI wit.
"""

import ollama
import os
import gradio as gr
 
 
# Function to generate a comedy bit
def write_comedy_routine(topic, audience_style):
    # Set the AI to behave like a stand-up comedian
    messages = [
        {
            "role": "system",
            "content": (
                f"You are a professional stand-up comedian. Write a short comedy routine (about 5-7 jokes or one-liners) "
                f"on the topic '{topic}' for a {audience_style} audience. Be clever, funny, and keep it clean if necessary."
            )
        },
        {
            "role": "user",
            "content": f"Write a routine about: {topic}"
        }
    ]
 
    try:
        # Get jokes from Ollama
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return the stand-up bit
        return response['message']['content'].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface for stand-up writing
iface = gr.Interface(
    fn=write_comedy_routine,
    inputs=[
        gr.Textbox(label="Comedy Topic (e.g. online dating, work from home, AI taking over)"),
        gr.Radio(["general audience", "tech crowd", "college students", "corporate"], label="Audience Style")
    ],
    outputs="text",
    title="🎤 AI Stand-Up Comedy Writer",
    description="Enter a topic and choose your crowd, and I’ll write a funny stand-up bit you can perform, tweet, or just laugh at!"
)
 
# Launch the comedy writer
iface.launch()