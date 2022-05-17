import os
from dotenv import dotenv_values
import requests as rqs
from flask import Flask, jsonify, render_template, request
from utils import encrypt

server = Flask(__name__)

ENV = dotenv_values()  


"""
EXERCISE: 

Turn your program for the cesear cipher (exercise 3 from earlier)
into a little flask app that takes a string input, and returns the 
encrypted text to the user 

""" 


@server.route("/", methods=['GET', 'POST'])
def index():
    """
    welcome page
    """
    if request.method == "POST":
       name = request.form["name_field"]

       try:
           cipher_ = int(request.form["cipher_len"])
       except ValueError:
           raise ValueError("Input not valid integer!")

       encrypted = encrypt(name, cipher_)
       return f"Encrypted Text: {encrypted}" 

    return render_template("index.html")


@server.route("/api/encrypt/<string:clear_text>", methods=['GET'])
def cesear_api(clear_text: str):
    """
    api hello
    """   
    return jsonify({"clear_text": clear_text, "encrypted_text": encrypt(clear_text) })
if __name__ == '__main__':
    server.run(host=ENV['HOST'],port=ENV['PORT'], debug=True)
