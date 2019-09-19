'''
Created on 17 de set de 2019

@author: Diego Alves A. (diego.assis@enel.com)

'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
