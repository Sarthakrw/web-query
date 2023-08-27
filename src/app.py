import gradio as gr
from web_scraper import scraper
from chat_chain import chat, system_message

def run(url, input):
    context = scraper(url)
    cleaned_response = chat.predict(system_message=system_message, context=context, prompt=input)

    return cleaned_response

# Create a Gradio interface
iface = gr.Interface(
    fn=run,
    inputs=["text","text"],
    outputs="text",
    title="Web Query App",
    description="Enter the webpage url and your query\nIMPORTANT: Larger webpages are likely to cause error due to lack of high end computational resources"
)

# Launch the interface
iface.launch()