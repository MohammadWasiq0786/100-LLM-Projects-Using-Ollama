"""
Project 79. Press Release Generator

Description:
This media-savvy tool crafts professional, engaging press releases for your product launches, funding announcements, 
events, or milestones. It follows journalistic structure and includes quotes, impact statements, and a compelling headline.
"""

import ollama
import os
import gradio as gr
 
 
# Function to generate press release
def generate_press_release(announcement_type, company_name, key_details, quote_by_whom):
    # Prompt to act like a tech PR writer
    messages = [
        {
            "role": "system",
            "content": (
                "You are a public relations assistant. Create a professional press release based on the information below. "
                "The press release should include:\n"
                "- A headline\n"
                "- A strong opening paragraph with key facts\n"
                "- A quote from the person named\n"
                "- Details about the impact or significance\n"
                "- A closing paragraph about the company.\n"
                "Keep it formal, media-friendly, and structured."
            )
        },
        {
            "role": "user",
            "content": (
                f"Announcement Type: {announcement_type}\n"
                f"Company Name: {company_name}\n"
                f"Key Details: {key_details}\n"
                f"Quote From: {quote_by_whom}"
            )
        }
    ]
 
    try:
        # Generate the press release
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
        return response["message"]["content"].strip()
    
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface
iface = gr.Interface(
    fn=generate_press_release,
    inputs=[
        gr.Textbox(label="Type of Announcement (e.g. Product Launch, Funding Round)"),
        gr.Textbox(label="Company or Brand Name"),
        gr.Textbox(label="Key Details (what, when, why, how)"),
        gr.Textbox(label="Who’s Quoting? (e.g. CEO, Founder, CMO)")
    ],
    outputs="text",
    title="🗞️ Press Release Generator",
    description="Craft a media-ready announcement that tells your story with impact. Great for launches, partnerships, or milestones."
)
 
# Launch the PR tool
iface.launch()