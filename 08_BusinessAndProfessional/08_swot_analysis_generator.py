"""
Project 78. SWOT Analysis Generator

Description:
This tool creates a detailed SWOT (Strengths, Weaknesses, Opportunities, Threats) analysis for any business, project, 
or personal brand. Great for pitch decks, strategic planning, or self-assessment to uncover risks and advantages.
"""

import ollama
import os
import gradio as gr
 
 
# Function to generate SWOT analysis
def generate_swot(business_name, description, industry):
    # Prompt to behave like a strategic business analyst
    messages = [
        {
            "role": "system",
            "content": (
                "You are a business analyst helping to generate a SWOT analysis. Based on the company name, its description, and industry, "
                "create a detailed SWOT covering:\n- Strengths\n- Weaknesses\n- Opportunities\n- Threats\n"
                "Make it clear, concise, and suitable for strategic decision making or a pitch deck."
            )
        },
        {
            "role": "user",
            "content": (
                f"Business Name: {business_name}\n"
                f"Description: {description}\n"
                f"Industry: {industry}"
            )
        }
    ]
 
    try:
        # Ask OpenAI to generate SWOT
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface
iface = gr.Interface(
    fn=generate_swot,
    inputs=[
        gr.Textbox(label="Business or Brand Name"),
        gr.Textbox(label="Brief Description of Business"),
        gr.Textbox(label="Industry (e.g. SaaS, Retail, HealthTech, Personal Brand)")
    ],
    outputs="text",
    title="📊 SWOT Analysis Generator",
    description="Enter your business info and get a full SWOT breakdown to use in planning, pitches, or team discussions."
)
 
# Launch the SWOT builder
iface.launch()