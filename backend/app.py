from flask import Flask

app = Flask(_name_)

@app.route('/')
def home():
    return "Backend API Running"

app.run(host="0.0.0.0", port=5000)
