from flask import Flask, jsonify
app = Flask(__name__)


from controller import *


@app.route("/test")
def test():
    return "Bismillah"
