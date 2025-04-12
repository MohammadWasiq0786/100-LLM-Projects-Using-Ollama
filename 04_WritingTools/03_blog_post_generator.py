"""
Project 33. Blog Post Generator

Description:
This tool generates complete blog posts based on a topic, audience, and desired tone. Whether it’s technical, motivational, 
informative, or casual—it produces well-structured blog content that’s ready to post or personalize.
"""

import ollama
import os
import gradio as gr

 
# Function to generate a blog post
def generate_blog(topic, audience, tone):
    # System message to guide assistant as a blog writer
    messages = [
        {
            "role": "system",
            "content": (
                f"You are a skilled blog writer. Write a complete blog post about the topic provided, tailored to {audience} in a {tone} tone. "
                "Include an engaging introduction, 2-3 key sections, and a conclusion with a call to action if relevant."
            )
        },
        {
            "role": "user",
            "content": f"Blog topic: {topic}"
        }
    ]
 
    try:
        # Send request to Ollama
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return blog content
        return response["message"]["content"].strip()
 
    except Exception as e:
        # Return error
        return f"Error: {str(e)}"
 
# Gradio interface for blog generation
iface = gr.Interface(
    fn=generate_blog,                                       # Blog generator function
    inputs=[
        gr.Textbox(label="Topic (e.g., AI in Education)"),
        gr.Textbox(label="Target Audience (e.g., high school students, startup founders)"),
        gr.Radio(["informative", "motivational", "casual", "technical"], label="Tone")
    ],
    outputs="text",                                         # Blog post result
    title="📝 Blog Post Generator",
    description="Enter a blog topic, your audience, and tone—and I’ll generate a ready-to-post blog article with structure and flair."
)
 
# Launch the app
iface.launch()