'''
Created on 19 de set de 2019

@author: Diego
'''

from flask_sqlalchemy import SQLAlchemy

sqla = SQLAlchemy()

class Chamado(sqla.Model):
    __tablename__ = 'tblChamado'
    numeroChamado = sqla.Column(sqla.Integer, primary_key = True)
    dataAbertura = sqla.Column(sqla.Date, nullable = False)
    dataEncerramento = sqla.Column(sqla.Date, nullable = True)
    #statusChamado = sqla.relationship('Status', backref = 'tblChamado', lazy = True)
    statusChamado = sqla.Column(sqla.Integer, sqla.ForeignKey('tblStatus.id'), nullable = False)
    solicitanteNome = sqla.Column(sqla.String(30), nullable = False)
    solicitanteTelefone = sqla.Column(sqla.String(14), nullable = False)
    solicitanteLocalidade = sqla.Column(sqla.String(30), nullable = False)
    tipo = sqla.Column(sqla.Integer, sqla.ForeignKey('tblTipoChamado.id'), nullable = False)
    sistema = sqla.Column(sqla.Integer, sqla.ForeignKey('tblSistema.id'), nullable = False)
    origemReclamacao = sqla.Column(sqla.Integer, sqla.ForeignKey('tblOrigemReclamacao.id'), nullable = False)
    tempoLentidao = sqla.Column(sqla.Integer, nullable = False)
    descricaoProblema = sqla.Column(sqla.String(100), nullable = False)
    processoConclui = sqla.Column(sqla.String(20), nullable = False)
    problemaLojas = sqla.Column(sqla.String(20), nullable = False)
    problemaEmAllWSLojas = sqla.Column(sqla.String(20), nullable = False)
    problemaEnel = sqla.Column(sqla.String(20), nullable = False)
    problemaEmAllWSEnel = sqla.Column(sqla.String(20), nullable = False)
    problemaCCenter = sqla.Column(sqla.String(50), nullable = False)
    chamadoAberto = sqla.Column(sqla.String(50), nullable = False)
    nmrChamadoAberto = sqla.Column(sqla.String(20), nullable = True)
    contatoNome = sqla.Column(sqla.String(30), nullable = False)
    contatoTelefone = sqla.Column(sqla.String(14), nullable = False)
    contatoLocalidade = sqla.Column(sqla.String(30), nullable = False)
    comentarios = sqla.Column(sqla.Integer, sqla.ForeignKey('tblComentarios.id'), nullable = True)
    causaRaiz = sqla.Column(sqla.String(255), nullable = True)
    
class TipoChamado(sqla.Model):
    __tablename__ = 'tblTipoChamado'
    id = sqla.Column(sqla.Integer, primary_key = True)
    descricao = sqla.Column(sqla.String(30), nullable = False)

class Sistema(sqla.Model):
    __tablename__ = 'tblSistema'
    id = sqla.Column(sqla.Integer, primary_key = True)
    descricao = sqla.Column(sqla.String(30), nullable = False)
    
class OrigemReclamacao (sqla.Model):
    __tablename__ = "tblOrigemReclamacao"
    id = sqla.Column(sqla.Integer, primary_key = True)
    area = sqla.Column(sqla.String(30), nullable = False)

class Status (sqla.Model):
    __tablename__ = 'tblStatus'
    id = sqla.Column(sqla.Integer, primary_key = True)
    descStatus = sqla.Column(sqla.String(30), nullable = False)

class Comentarios (sqla.Model):
    #FIXME: Necessario definir como sera o relacionamento da tabela de chamados com a tabela de comentarios (1:n)
    __tablename__ = 'tblComentarios'
    id = sqla.Column(sqla.Integer, primary_key = True)
    comentario
     
