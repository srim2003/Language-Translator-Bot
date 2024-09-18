import gradio as gr
import requests

# Mapping of language codes to full names
language_names = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "hi": "Hindi",
    "kn": "Kannada",
    "te": "Telugu",
    "zh-CN": "Chinese",
    "ru": "Russian",
    "bh": "Bhojpuri",
    "ar": "Arabic",
    "de": "German",
    "ja": "Japanese",
    "pt": "Portuguese",
    "it": "Italian"
}

def translate_text(text, source_language, target_language):
    # Retrieve language codes from language names
    source_code = next(key for key, value in language_names.items() if value == source_language)
    target_code = next(key for key, value in language_names.items() if value == target_language)

    # Make request to translation service
    response = requests.post(
        'http://localhost:5000/translate',
        json={'source_language': source_code, 'target_language': target_code, 'text': text}
    )
    return response.json().get('translated_text')

iface = gr.Interface(
    fn=translate_text,
    inputs=[
        gr.Textbox(lines=2, placeholder="Enter text to translate..."),
        gr.Dropdown(choices=list(language_names.values()), label="Source Language"),
        gr.Dropdown(choices=list(language_names.values()), label="Target Language")
    ],
    outputs="text",
    title="Language Translator Bot",
    description="Translate text from one language to another."
)

iface.launch()
