from flask import Flask, request, jsonify, send_from_directory
from groq import Groq

app = Flask(__name__)

# Aapki API Key
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@app.route("/")
def home():
    return send_from_directory('.', 'index.html')

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_question = data.get("question", "")

    if not user_question:
        return jsonify({"answer": "Please write a question"})

    try:
        completion = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {"role": "system", "content": "You are a helpful AI Study Helper. Answer in simple Roman Urdu and English."},
                {"role": "user", "content": user_question}
            ]
        )
        answer = completion.choices[0].message.content
    except Exception as e:
        answer = f"Error: {e}"

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
