import gradio as gr
from transformers import pipeline

# Free HuggingFace model
chatbot = pipeline(
    "text-generation",
    model="google/flan-t5-base"
)

def study_helper(question):
    prompt = (
        "You are a helpful study assistant. "
        "Explain answers step by step in simple Hindi and English.\n\n"
        f"Question: {question}\nAnswer:"
    )
    result = chatbot(prompt, max_length=200)
    return result[0]["generated_text"]

ui = gr.Interface(
    fn=study_helper,
    inputs=gr.Textbox(lines=3, placeholder="Apna study question likho..."),
    outputs="text",
    title="📚 StudyBuddy AI",
    description="Free Study Helper AI (Hindi + English)"
)

ui.launch()
