from flask import Flask, request, render_template, jsonify
from textblob import TextBlob

app = Flask(__name__)

def summarize(text, max_sentences=3):
    from textblob import TextBlob
    sentences = text.split('.')
    blob = TextBlob(text)
    ranked = sorted(
        [(s, TextBlob(s).sentiment.polarity) for s in sentences if s.strip()],
        key=lambda x: abs(x[1]),
        reverse=True
    )
    summary = '. '.join([s[0].strip() for s in ranked[:max_sentences]]) + '.'
    return summary

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize_text():
    data = request.get_json()
    text = data.get('text', '')
    summary = summarize(text)
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)
