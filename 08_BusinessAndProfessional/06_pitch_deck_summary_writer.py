"""
Project 76. Pitch Deck Summary Writer

Description:
This assistant creates a concise, investor-ready summary of your pitch deck based on your product, market, vision, and traction. 
Ideal for intros, executive summaries, or quick-share documents that still pack a punch.
"""

import ollama
import os
import gradio as gr
 
# Function to generate a pitch deck summary
def generate_pitch_summary(product, target_market, traction, vision):
    # Prompt the AI to act like a startup storytelling coach
    messages = [
        {
            "role": "system",
            "content": (
                "You are a startup pitch writing expert. Using the inputs below, generate a compelling one-paragraph summary of the startup pitch deck. "
                "The summary should highlight the problem, the solution (product), the target market, the traction or success so far, and a forward-looking vision. "
                "Keep it concise, confident, and appealing to investors or partners."
            )
        },
        {
            "role": "user",
            "content": (
                f"Product or Idea: {product}\n"
                f"Target Market: {target_market}\n"
                f"Current Traction: {traction}\n"
                f"Vision: {vision}"
            )
        }
    ]
 
    try:
        # Get summary from Ollama
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
        return response["message"]["content"].strip()
    
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface
iface = gr.Interface(
    fn=generate_pitch_summary,
    inputs=[
        gr.Textbox(label="Product or Idea (What are you building?)"),
        gr.Textbox(label="Target Market (Who is it for?)"),
        gr.Textbox(label="Current Traction (Milestones, Revenue, Users)"),
        gr.Textbox(label="Vision (What does the future look like?)")
    ],
    outputs="text",
    title="📊 Pitch Deck Summary Writer",
    description="Input your startup details and get a polished pitch summary paragraph for investors, demo days, or one-pagers."
)
 
# Launch the pitch summary tool
iface.launch()