from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

messages = [
    "You are someone’s reason to smile today ❤️",
    "This heart beats just for you 💖",
    "Happy Valentine’s Day 🌹",
    "You matter more than you know ✨",
    "Sending you lots of love 💕",
    "You are the reason for me living in this cruel world",
    "Love you a lot Baby Gurl"
]

@app.route("/")
def home():
    return render_template("heart.html")

@app.route("/message")
def get_message():
    return jsonify({
        "message": random.choice(messages)
    })

if __name__ == "__main__":
    app.run(debug=True)