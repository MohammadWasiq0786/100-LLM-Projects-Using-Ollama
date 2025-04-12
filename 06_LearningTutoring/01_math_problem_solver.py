"""
Project 51. Math Problem Solver

Description:
This smart assistant solves math problems and explains the steps clearly. Whether it’s arithmetic, algebra, geometry, or 
calculus—you enter a problem, and it returns the answer along with a step-by-step explanation in plain language.
"""

import ollama
import os
import gradio as gr

 
# Function to solve math problems and explain them
def solve_math(problem):
    # Prompt to guide AI to act like a math tutor
    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful and friendly math tutor. Solve the math problem given by the user and explain the steps in simple language. "
                "Use bullet points or numbered steps for clarity. Keep the tone encouraging and beginner-friendly."
            )
        },
        {
            "role": "user",
            "content": f"Solve this: {problem}"
        }
    ]
 
    try:
        # Call the Ollama
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return the solution and explanation
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio UI
iface = gr.Interface(
    fn=solve_math,
    inputs=gr.Textbox(label="Enter a Math Problem (e.g. solve 3x + 5 = 20)"),
    outputs="text",
    title="🧮 Math Problem Solver",
    description="Enter a math question and get a step-by-step solution with an explanation. Great for homework help and learning!"
)
 
# Launch the solver
iface.launch()