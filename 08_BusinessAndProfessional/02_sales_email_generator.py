"""
Project 72. Sales Email Generator

Description:
This persuasive assistant creates high-converting sales emails tailored to your product, target audience, and desired tone. 
Whether it’s a cold outreach or product launch, the result is a crisp message that sells without sounding spammy.
"""

import ollama
import os
import gradio as gr
 

# Function to generate sales email
def generate_sales_email(product, audience, tone):
    # Prompt to act like a skilled sales copywriter
    messages = [
        {
            "role": "system",
            "content": (
                "You are a persuasive sales email copywriter. Craft a compelling email promoting the product/service below. "
                "Use the given tone, make the content relevant to the target audience, and include a clear call to action. "
                "Keep it professional yet engaging. Avoid sounding robotic or spammy."
            )
        },
        {
            "role": "user",
            "content": (
                f"Product or Offer: {product}\n"
                f"Target Audience: {audience}\n"
                f"Tone: {tone}"
            )
        }
    ]
 
    try:
        # Generate the email using Ollama
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio UI
iface = gr.Interface(
    fn=generate_sales_email,
    inputs=[
        gr.Textbox(label="Product or Offer (e.g. CRM software, AI writing tool)"),
        gr.Textbox(label="Target Audience (e.g. small business owners, SaaS founders)"),
        gr.Radio(["Professional", "Conversational", "Excited", "Friendly"], label="Tone of the Email")
    ],
    outputs="text",
    title="💼 Sales Email Generator",
    description="Describe your product, audience, and tone—I’ll write a compelling sales email with CTA included!"
)
 
# Launch the sales email writer
iface.launch()