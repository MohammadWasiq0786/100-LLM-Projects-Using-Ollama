"""
Project 55. SAT/GRE Vocabulary Practice Bot

Description:
This quiz-style bot helps users practice high-level vocabulary commonly found in the SAT, GRE, and other competitive exams. 
It generates questions like definitions, synonyms, antonyms, and sentence completions—ideal for students aiming to master academic words.
"""

import ollama
import os
import gradio as gr
 
 
# Function to generate a vocabulary practice quiz
def vocab_practice(level, question_type):
    # Prompt to act like a test prep tutor
    messages = [
        {
            "role": "system",
            "content": (
                f"You are a test prep tutor helping students prepare for the {level}. "
                f"Create 3 vocabulary practice questions of type: {question_type}. "
                "Each question should have 4 answer options (A–D) and highlight the correct one in the explanation. "
                "Use advanced vocabulary relevant to the exam."
            )
        },
        {
            "role": "user",
            "content": "Generate quiz."
        }
    ]
 
    try:
        # Request practice questions from Ollama
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return quiz
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio UI
iface = gr.Interface(
    fn=vocab_practice,
    inputs=[
        gr.Radio(["SAT", "GRE"], label="Exam Level"),
        gr.Radio(["Definitions", "Synonyms", "Antonyms", "Fill in the Blank"], label="Question Type")
    ],
    outputs="text",
    title="🎓 SAT/GRE Vocabulary Practice Bot",
    description="Choose your test and question type to practice high-level vocabulary with quiz-style questions and explanations."
)
 
# Launch the quiz bot
iface.launch()