from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Basic health replies
def get_health_reply(message):
    msg = message.lower()
    if "fever" in msg:
        return "Fever ke liye rest lo, paani zyada piyo aur doctor se consult karo agar 2 din se jyada ho."
    elif "headache" in msg:
        return "Headache ke liye paani piyo, stress kam lo aur rest karo."
    elif "cold" in msg or "cough" in msg:
        return "Garam paani ya kadha lo, thanda food avoid karo."
    elif "diet" in msg or "food" in msg:
        return "Balanced diet lo — fruits, green vegetables, aur junk food kam karo."
    elif "sleep" in msg:
        return "Har din kam se kam 7-8 ghante ki neend lo."
    if "hi" in msg:
        return "bolna be saale jaldi."
    else:
        return "bsdk bolna kya kaam hai , bakchodi karne me to aage hai."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    bot_reply = get_health_reply(user_message)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
