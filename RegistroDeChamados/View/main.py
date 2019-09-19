'''
Created on 17 de set de 2019

@author: Diego Alves A. (diego.assis@enel.com)

'''
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Parametrização da conexao com o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///../Controller/BD/RegistroChamado.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) 

def main():
    #Realiza a criação das tabelas
    #FIXME: Tabela não estão sendo criadas, necessario analisar
    db.create_all()

#Inicio
@app.route("/")
def index():
    main()
    return render_template("index.html")
