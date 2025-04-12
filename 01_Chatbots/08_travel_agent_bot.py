"""
Project 8. Travel Agent Chatbot

Description:
This chatbot acts as a personalized travel agent. It can help users discover destinations, plan itineraries, 
suggest activities, and offer travel tips based on budget, season, or preferences. A great demo for travel, 
hospitality, or leisure-based LLM use cases.
"""


import ollama
import gradio as gr
import os
 
# Function to simulate a travel agent interaction
def travel_planner(user_input):
    # Set up the system prompt that defines the bot's role and behavior
    messages = [
        {
            "role": "system",
            "content": (
                "You are a knowledgeable and friendly virtual travel agent. "
                "Help users plan trips by suggesting destinations, itineraries, activities, packing tips, and budget advice. "
                "Ask relevant follow-up questions if necessary to personalize suggestions."
            )
        },
        {
            "role": "user",
            "content": user_input  # The travel-related query from the user
        }
    ]
 
    try:
        # Make API call to OpenAI's GPT model with the prompt and user input
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return the assistant's travel suggestions or response
        return response['message']['content'].strip()
 
    except Exception as e:
        # Handle any error (like missing API key or connection issue)
        return f"Error: {str(e)}"
 
# Create Gradio interface for user interaction
iface = gr.Interface(
    fn=travel_planner,                      # Function that generates travel advice
    inputs="text",                          # Text input field for user questions
    outputs="text",                         # Bot’s response will appear here
    title="🌍 Travel Agent Chatbot",        # App title shown in the browser
    description=(
        "Plan your next trip with a virtual travel assistant. "
        "Try things like: 'Plan a 5-day trip to Japan on a budget', "
        "'Suggest summer destinations in Europe', or 'Things to do in Bali in December'."
    )
)
 
# Launch the chatbot web app using Gradio
iface.launch()