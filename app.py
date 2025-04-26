from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)


MESSAGES_FILE = 'messages.json'


def load_messages():
    if os.path.exists(MESSAGES_FILE):
        with open(MESSAGES_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return []


def save_messages(messages):
    with open(MESSAGES_FILE, 'w', encoding='utf-8') as f:
        json.dump(messages, f, ensure_ascii=False, indent=4)

@app.route('/', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        message = request.form['message']
        messages = load_messages()
        messages.append(message)
        save_messages(messages)
        return redirect('/')  # чтобы после отправки не повторно отправлялась форма

    messages = load_messages()
    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))