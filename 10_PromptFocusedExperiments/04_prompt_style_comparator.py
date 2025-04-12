"""
Project 94. Instruction vs. Role Prompt Comparison Tool

Description:
This tool compares two popular prompting styles—instructional (e.g., “Write a poem”) vs role-based (e.g., “You are a poet...”). 
It shows how each affects tone, creativity, and clarity in the model’s response.
"""

import os
import ollama
import gradio as gr
 
# Load OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")
 
# Function to compare instruction vs. role prompts
def compare_prompts(task_description):
    try:
        # Instruction-style prompt
        prompt_instruction = f"Write a response for the following task:\n{task_description}"
 
        # Role-style prompt
        prompt_role = f"You are an expert in this task. Respond accordingly.\nTask: {task_description}"
 
        # Call OpenAI twice for both styles
        instruction_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt_instruction}]
        )
 
        role_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt_role}]
        )
 
        return instruction_response["choices"][0]["message"]["content"].strip(), role_response["choices"][0]["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}", ""
 
# Gradio interface
iface = gr.Interface(
    fn=compare_prompts,
    inputs=gr.Textbox(label="Enter Task (e.g., Write a motivational quote, Explain black holes)"),
    outputs=[
        gr.Textbox(label="Instruction Prompt Output"),
        gr.Textbox(label="Role Prompt Output")
    ],
    title="📋 Instruction vs Role Prompt Comparison",
    description="Enter a task and compare how GPT responds using an instruction-style vs role-style prompt."
)
 
# Launch it!
iface.launch()