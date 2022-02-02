#!/usr/bin/python3
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def bonjour():
    message = "Bonjour, je suis Xavki \n"
    return message

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=8080)
    app.run(host='192.168.33.10', port=8080)

