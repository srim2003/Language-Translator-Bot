from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)
@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    source_language = data.get('source_language')
    target_language = data.get('target_language')
    text = data.get('text')

    translator = Translator()
    translation = translator.translate(text, src=source_language, dest=target_language)
    translated_text = translation.text

    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
