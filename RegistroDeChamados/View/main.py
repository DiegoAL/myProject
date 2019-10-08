'''
Created on 17 de set de 2019

@author: Diego Alves A. (diego.assis@enel.com)

'''
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy, event
from sqlalchemy import create_engine
from Controller.BD.sqlLite3_creat import main, getConnect
from Controller.BD import sqlLite3_creat
from Model.ModelChamado import *
from datetime import date, datetime
from matplotlib.backends.backend_agg import RendererAgg

app = Flask(__name__)

#Parametrização da conexao com o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///../Controller/BD/RegistroChamado.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#variavel global de data atual
diaAtual = date.today()
diaAtual = diaAtual.strftime("%d/%m/%Y")

#converter o objeto em datetime
diaAtual = datetime.strptime(diaAtual, '%d/%m/%Y')

database_url = r'..\Controller\BD\RegistroChamado.db'

#FIXME:Validação de FK no sqlite3 não esta funcionando, post no stackoverflow
#Ativar validação FK para o sqlite3
engine = create_engine(r'sqlite:///../Controller/BD/RegistroChamado.db')

def _fk_pragma_on_connect(con = getConnect(database_url)):
    con.execute('pragma foreign_keys=ON')

event.listen(engine, 'connect', _fk_pragma_on_connect)

def main():
    #realiza a criação do banco de dados
    sqlLite3_creat.main(database_url)
    
    #Realiza a criação das tabelas
    sqla.create_all()
    
    
#Inicio
@app.route("/")
def index():
    main()
    return render_template("index.html")

#Registrod e novos chamados
@app.route("/registrarchamado")
def paginaDeRegistroChamados():
    tpChamados = TipoChamado.query.all()
    sistemas = Sistema.query.all()
    origemReclamacao = OrigemReclamacao.query.all()
        
    return render_template("registrarChamado.html", tpchamados = tpChamados, sistemas = sistemas, origemReclamacao = origemReclamacao )

@app.route('/chamadoRegistrado', methods=['POST'])
def registrarChamado():
    
    newChamado = Chamado(
        dataAbertura = diaAtual,
        dataEncerramento = None,
        #Busca pelo status 'aberto' no chamado
        statusChamado = Status.query.filter_by(descStatus = 'Aberto').first(),
        solicitanteNome = request.form.get('nome'),
        solicitanteTelefone = request.form.get('telefone'),
        solicitanteLocalidade = request.form.get('localidade'),
        tipo = request.form.get('cbxTpChamado'),
        sistema = request.form.get('cbxSistema'),
        origemReclamacao = request.form.get('cbxOrigemReclamacao'),
        tempoLentidao = request.form.get('TempoProcessamento'),
        descricaoProblema = request.form.get('inpOutros'),
        processoConclui = request.form.get('chbxGroup1'),
        problemaLojas = request.form.get('chbxGroup2'),
        problemaEmAllWSLojas = request.form.get('chbxGroup3'),
        problemaEnel = request.form.get('chbxGroup4'),
        problemaEmAllWSEnel = request.form.get('chbxGroup5'),
        problemaCCenter = request.form.get('chbxGroup6'),
        chamadoAberto = request.form.get('chbxGroup7'),
        nmrChamadoAberto = request.form.get('chamadoAnterior'),
        contatoNome = request.form.get('contatoNome'),
        contatoTelefone = request.form.get('contatoTelefone'),
        contatoLocalidade = request.form.get('contatoLocalidade'))
    
    try:        
        db.session.add(newChamado)
        db.session.commit()
        
        #FIXME: Identificar por que o try except está indo parar no erro mesmo tendo sucesso
        return render_template("chamadoRegistradoSucesso.html", numeroChamado = newChamado.numeroChamado)
    
    #TODO: gerar um log de erro
    except Exception as error:
        return render_template("erro.html")

@app.route("/teste")
def teste():
    return render_template("chamadoRegistradoSucesso.html")   
    