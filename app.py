from flask import Flask, render_template, request, redirect
from chatbot import get_response

app = Flask(__name__)

chat_history = []

@app.route("/", methods=["GET", "POST"])
def home():
    global chat_history

    if request.method == "POST":
        message = request.form["message"]

        reply = get_response(message)

        chat_history.append({
            "user": message,
            "bot": reply
        })

    return render_template(
        "index.html",
        chat_history=chat_history
    )


@app.route("/clear", methods=["POST"])
def clear():
    global chat_history
    chat_history = []
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)







