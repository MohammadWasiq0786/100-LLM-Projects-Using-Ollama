"""
Project 19. Research Paper Key Points Extractor

Description:
This tool extracts the key takeaways from research papers—covering objectives, methods, findings, and conclusions. 
It’s perfect for summarizing complex studies into simple, structured summaries for faster reading and comprehension.
"""


import ollama
import os
import gradio as gr

 
# Function that summarizes research papers into key sections
def extract_research_key_points(paper_text):
    # Use a system message to guide the assistant's behavior
    messages = [
        {
            "role": "system",
            "content": (
                "You are a research assistant. Your job is to extract the key points from academic research papers. "
                "Structure the summary into sections: Objective, Methods, Results, and Conclusion. "
                "Keep it concise, clear, and jargon-free for general understanding."
            )
        },
        {
            "role": "user",
            "content": f"Summarize this research paper:\n\n{paper_text}"
        }
    ]
 
    try:
        # Make the call to Ollama with the messages
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Extract the content and return the structured summary
        return response['message']['content'].strip()
 
    except Exception as e:
        # Handle and display errors
        return f"Error: {str(e)}"
 
# Create a Gradio interface
iface = gr.Interface(
    fn=extract_research_key_points,                    # Function to extract key points
    inputs=gr.Textbox(lines=20, placeholder="Paste the full text of a research paper here..."),
    outputs="text",                                    # Output summary
    title="📄 Research Paper Key Points Extractor",    # Title of the app
    description=(
        "Paste a research paper or abstract to get structured key points. "
        "Outputs include Objective, Methods, Results, and Conclusion—great for study and review."
    )
)
 
# Launch the app in a web browser
iface.launch()