'''
Created on 19 de set de 2019

@author: Diego
'''

from flask_sqlalchemy import SQLAlchemy

sqla = SQLAlchemy()

class Chamado(sqla.Model):
    __tablename__ = 'tblChamado'
    numeroChamado = sqla.Column(sqla.Integer, primary_key = True)
    solicitanteNome = sqla.Column(sqla.String(30), nullable = False)
    solicitanteTelefone = sqla.Column(sqla.String(14), nullable = False)
    solicitanteLocalidade = sqla.Column(sqla.String(30), nullable = False)
    #TODO: Incluir dados de log para possivel rastreio e auditoria
    tipo =  sqla.relationship('TipoChamado', backref = 'tblChamado', lazy = True)
    sistema = sqla.relationship('Sistema', backref='tblChamado', lazy = True)
    origemReclamacao = sqla.relationship('OrigemReclamacao', backref = 'tblChamado', lazy = True)
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
    processoConclui = sqla.Column(sqla.String(20), nullable = False)
    contatoNome = sqla.Column(sqla.String(30), nullable = False)
    contatoTelefone = sqla.Column(sqla.String(14), nullable = False)
    contatoLocalidade = sqla.Column(sqla.String(30), nullable = False)
    #TODO: criar o campo e tabela de status do chamado, alem de complementar as informações com os dados do solicitante
    
class TipoChamado(sqla.Model):
    __tablename__ = 'tblTipoChamado'
    id = sqla.Column(sqla.Integer, primary_key = True)
    descricao = sqla.Column(sqla.String(30), nullable = False)
    fkNumeroChamado = sqla.Column(sqla.Integer, sqla.ForeignKey('tblChamado.numeroChamado'), nullable = False)

class Sistema(sqla.Model):
    __tablename__ = 'tblSistema'
    id = sqla.Column(sqla.Integer, primary_key = True)
    descricao = sqla.Column(sqla.String(30), nullable = False)
    fkNumeroChamado = sqla.Column(sqla.Integer, sqla.ForeignKey('tblChamado.numeroChamado'), nullable = False)
    
class OrigemReclamacao (sqla.Model):
    __tablename__ = "tblOrigemReclamacao"
    id = sqla.Column(sqla.Integer, primary_key = True)
    area = sqla.Column(sqla.String(30), nullable = False)
    fkNumeroChamado = sqla.Column(sqla.Integer, sqla.ForeignKey('tblChamado.numeroChamado'), nullable = False)
    
