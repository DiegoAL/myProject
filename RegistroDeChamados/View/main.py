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
from flask_debugtoolbar import DebugToolbarExtension
from scipy.stats._multivariate import method

app = Flask(__name__)

#Parametrização da conexao com o banco de dados
database_url = r'..\Controller\BD\RegistroChamado.db'


app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///' + database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#debug toolbar
app.config['SECRET_KEY'] = "QualquerCoisa"
debugToolBar = DebugToolbarExtension(app)

#variavel global de data atual
diaAtual = date.today()
diaAtual = diaAtual.strftime("%d/%m/%Y")

#converter o objeto em datetime
diaAtual = datetime.strptime(diaAtual, '%d/%m/%Y')

#FIXME:Validação de FK no sqlite3 não esta funcionando, post no stackoverflow
#Ativar validação FK para o sqlite3
engine = create_engine(r'sqlite:///../Controller/BD/RegistroChamado.db')

def _fk_pragma_on_connect(con = getConnect(database_url)):
    con.execute('pragma foreign_keys=ON')

event.listen(engine, 'connect', _fk_pragma_on_connect)

#Cria o banco sqlite caso nao exista e cria as tabelas caso não existam
@app.before_first_request
def initialize():
    
    #realiza a criação do banco de dados
    sqlLite3_creat.main(database_url)
    
    #Realiza a criação das tabelas
    sqla.create_all()
    
    
#Pagina inicial, onde sao exibidas notificacoes em aberto
@app.route("/")
def index():
    
    #Busca os chamados registrados no banco que estejam em aberto 
    chamados = db.session.query(Chamado,TipoChamado,Sistema).filter_by(dataEncerramento = None).order_by(Chamado.dataAbertura.desc()).join(TipoChamado).join(Sistema).all()
    return render_template("index.html", chamados = chamados)

#Registro de novos chamados
@app.route("/registrarchamado")
def paginaDeRegistroChamados():
    
    try:
        tpChamados = TipoChamado.query.all()
        sistemas = Sistema.query.all()
        origemReclamacao = OrigemReclamacao.query.all()
        return render_template("registrarChamado.html", tpchamados = tpChamados, sistemas = sistemas, origemReclamacao = origemReclamacao )
    
    except Exception as err:
        return render_template("erro.html", erro = err)
        
    

@app.route('/chamadoRegistrado', methods=['POST'])
def registrarChamado():
    
    #busca o ID do tipo de chamado Aberto pois todo chamado novo devera entrar com esse status 
    sts = Status.query.filter_by(descStatus = 'Aberto').first()
    
    newChamado = Chamado(
        dataAbertura = diaAtual,
        dataEncerramento = None,
        #Busca pelo status 'aberto' no chamado
        statusChamado = sts.id,
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
        
        return render_template("chamadoRegistradoSucesso.html", numeroChamado = newChamado.numeroChamado)
    
    #TODO: gerar um log de erro
    except Exception as error:
        return render_template("erro.html", erro  = error)

@app.route("/consultar", methods=['GET', 'POST'])
def consultarChamado():
    
    if request.method == 'GET':
        #retorna uma lista vazia
        chamado = (Chamado(),TipoChamado, Sistema, OrigemReclamacao) 
        return render_template('consultar.html', chamado = chamado)
    
    elif request.method == 'POST':
        numeroChamado = request.form.get('numeroChamado')
        chamado = db.session.query(Chamado, TipoChamado, Sistema, OrigemReclamacao).filter_by(numeroChamado = numeroChamado).join(TipoChamado).join(Sistema).join(OrigemReclamacao).first()
        status = Status.query.all()
        return render_template('consultar.html', chamado = chamado, status = status)
    
    
if __name__ == '__main__':
    initialize()
    