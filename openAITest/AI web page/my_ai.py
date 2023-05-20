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
    userinlist = ["User: "]
    aiinlist = ["Chatbot: "]
    user_input = request.form["message"]
    userinlist.append(user_input)
    previous_inputs = []
    if 'all_prev_inputs' in session:
        previous_inputs = session["all_prev_inputs"]
    previous_inputs.append(userinlist)
    
    response = openai.ChatCompletion.create(
    model= "gpt-3.5-turbo",
    messages= [{"role": "user", "content": user_input}]
    )
    
    aiinlist.append(response.choices[0].message["content"])
    previous_inputs.append(aiinlist)
    session["all_prev_inputs"] = previous_inputs
    print(previous_inputs)
    return render_template("index.html", result=previous_inputs)

if __name__ == "__main__":
    app.run(debug=True)


#[[0, "user message"][1, "ai message"]]