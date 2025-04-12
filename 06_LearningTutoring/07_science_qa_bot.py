"""
Project 57. Science Q&A Bot

Description:
This intelligent bot answers science questions across physics, chemistry, biology, or astronomy in an easy-to-understand and accurate way. 
Ideal for curious students, quiz prep, or learning assistance—with explanations that make sense, not confusion.
"""

import ollama
import os
import gradio as gr
 
 
# Function to answer science questions
def answer_science_question(question, subject):
    # Prompt to behave like a science teacher
    messages = [
        {
            "role": "system",
            "content": (
                f"You are a brilliant and friendly science teacher. Answer the following question related to {subject}. "
                "Provide a clear, step-by-step explanation in simple language that even middle school students can understand. "
                "Use examples or analogies where helpful."
            )
        },
        {
            "role": "user",
            "content": question
        }
    ]
 
    try:
        # Call Ollama for response
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return explanation
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface
iface = gr.Interface(
    fn=answer_science_question,
    inputs=[
        gr.Textbox(label="Ask a Science Question"),
        gr.Dropdown(["Physics", "Chemistry", "Biology", "Astronomy", "General Science"], label="Subject Area")
    ],
    outputs="text",
    title="🔬 Science Q&A Bot",
    description="Ask any science question and get a clear, thoughtful answer with explanations—perfect for learners and science lovers!"
)
 
# Launch the bot
iface.launch()