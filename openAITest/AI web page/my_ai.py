from flask import Flask, render_template, request, session
import os
import openai


app = Flask(__name__)
app.secret_key = "dragonflame12"

openai.api_key = os.getenv("OPENAI_API_KEY")




@app.route('/')
def index():
    session.clear()
    return render_template("index.html")

@app.route('/', methods=["POST"])
def receive_input():
    user_input = request.form["message"]
    previous_inputs = []
    if 'all_prev_inputs' in session:
        previous_inputs = session["all_prev_inputs"]
    previous_inputs.append(user_input)
    
    response = openai.ChatCompletion.create(
    model= "gpt-3.5-turbo",
    messages= [{"role": "user", "content": user_input}]
    )
    
    previous_inputs.append(response.choices[0].message["content"])
    session["all_prev_inputs"] = previous_inputs
    return render_template("index.html", result=previous_inputs)

if __name__ == "__main__":
    app.run(debug=True)
