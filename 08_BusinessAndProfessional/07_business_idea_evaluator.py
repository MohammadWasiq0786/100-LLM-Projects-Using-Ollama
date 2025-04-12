"""
Project 77. Business Idea Evaluator

Description:
This tool evaluates your business idea based on the problem, target market, uniqueness, and potential challenges. 
It provides a quick SWOT-style analysis and gives a realistic thumbs-up (or down) with improvement tips.
"""

import ollama
import os
import gradio as gr
 
# Function to evaluate the business idea
def evaluate_business_idea(idea, market, uniqueness, challenge):
    # Prompt to act as a startup strategist
    messages = [
        {
            "role": "system",
            "content": (
                "You are a startup strategist. Evaluate this business idea and provide:\n"
                "- A quick summary\n"
                "- SWOT-style evaluation (Strengths, Weaknesses, Opportunities, Threats)\n"
                "- Overall potential (Low, Moderate, High)\n"
                "- One suggestion to improve the idea."
            )
        },
        {
            "role": "user",
            "content": (
                f"Idea: {idea}\n"
                f"Target Market: {market}\n"
                f"What makes it unique: {uniqueness}\n"
                f"Biggest challenge: {challenge}"
            )
        }
    ]
 
    try:
        # Ask Ollama to evaluate
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio UI
iface = gr.Interface(
    fn=evaluate_business_idea,
    inputs=[
        gr.Textbox(label="Describe Your Business Idea"),
        gr.Textbox(label="Target Market"),
        gr.Textbox(label="What Makes It Unique?"),
        gr.Textbox(label="What's the Biggest Challenge?")
    ],
    outputs="text",
    title="💡 Business Idea Evaluator",
    description="Quickly assess your startup idea with SWOT analysis, potential score, and improvement tips."
)
 
# Launch the evaluator
iface.launch()