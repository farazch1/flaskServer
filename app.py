from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hi():
    if request.method == 'GET':
        return "<p>this is test</p>"
    if request.method == 'POST':
        print("chnged")
        return "<p>hury</p>"