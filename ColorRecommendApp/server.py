from flask import Flask, render_template, request, session, jsonify
import os
import openai


app = Flask(__name__)
app.secret_key = "dragonflame12"

openai.api_key = os.getenv("OPENAI_API_KEY")




@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=["POST"])
def receive_input():
    user_input = request.form["message"]
    
    response = openai.ChatCompletion.create(
        model= "gpt-3.5-turbo",
        messages = [{"role": "system", "content": "your response will contain only 1 single list, \
                     no words or numbers will be returned outside of that list. In the list you will place 5 values. \
                     These values will be color codes that describes the user's input. \
                     You will create this list based on one single word, and if the user enters more than one word you will return this message exactly: \
                     'Please enter a single word.' \
                     If the message is not a noun, you will return this message exactly: 'Please enter a noun.'  \
                     Respond in a json array like this: ['#1F492A', '#198FA1', ...]"}, {"role": "user", "content": user_input}]
    )
    airesponse = response.choices[0].message["content"]
    return render_template("index.html", result=jsonify(airesponse))

if __name__ == "__main__":
    app.run(debug=True)