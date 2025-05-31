from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
import openai
import requests

load_dotenv()

openai.api_key = "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"
openai.base_url = "https://openrouter.ai/api/v1"

app = Flask(__name__, static_folder="../frontend")
CORS(app)

@app.route('/api/question', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question', '')
    try:
        headers = {
            "Authorization": f"Bearer {openai.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "deepseek/deepseek-r1-0528-qwen3-8b:free",
            "messages": [{"role": "user", "content": question}]
        }

        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        answer = data['choices'][0]['message']['content']
        return jsonify({'answer': answer})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Главная страница
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

# Остальные файлы (JS, CSS и т.д.)
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory(app.static_folder, path)

# Не нужен на Render — только для локального запуска
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)
