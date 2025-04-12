"""
Project 31. Email Rewriter

Description:
This tool rewrites any email into a more professional, polite, concise, or friendly tone—depending on your need. 
Perfect for job applications, cold outreach, internal communication, or simply leveling up your email game.
"""

import ollama
import os
import gradio as gr
 
 
# Function to rewrite emails with a chosen tone
def rewrite_email(original_email, tone):
    # Setup system instruction for rewriting style
    messages = [
        {
            "role": "system",
            "content": (
                f"You are a professional email assistant. Rewrite the following email to make it more {tone}. "
                "Preserve the original intent and content but improve clarity and tone."
            )
        },
        {
            "role": "user",
            "content": original_email
        }
    ]
 
    try:
        # Send the request to Ollama
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return the rewritten email
        return response["message"]["content"].strip()
 
    except Exception as e:
        # Display any error
        return f"Error: {str(e)}"
 
# Gradio interface with input for email and tone
iface = gr.Interface(
    fn=rewrite_email,                                       # Function to rewrite email
    inputs=[
        gr.Textbox(lines=8, label="Your Original Email"),   # Original email input
        gr.Radio(choices=["professional", "friendly", "concise", "polite"], label="Rewrite Tone")
    ],
    outputs="text",                                         # Rewritten email
    title="📧 Email Rewriter",
    description="Paste your email and choose a tone to get a polished version. Great for professional, friendly, or polite rewrites."
)
 
# Launch the app
iface.launch()