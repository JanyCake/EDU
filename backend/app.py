from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = "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"
openai.base_url = "https://openrouter.ai/api/v1"

app = Flask(__name__)
CORS(app)

@app.route('/api/question', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question', '')
    try:
        # Отправка запроса напрямую с использованием REST, так как openai-py может не работать с OpenRouter корректно
        import requests

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
