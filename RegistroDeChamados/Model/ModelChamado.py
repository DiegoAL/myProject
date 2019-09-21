'''
Created on 19 de set de 2019

@author: Diego
'''

from flask_sqlalchemy import SQLAlchemy

sqla = SQLAlchemy()

class Chamado(sqla.Model):
    __tablename__ = 'tblChamado'
    numeroChamado = sqla.Column(sqla.Integer, primary_key = True)
    tipo =  sqla.relationship('TipoChamado', backref = 'tblChamado', lazy = True)
    sistema = sqla.relationship('Sistema', backref='tblChamado', lazy = True)
    descricaoProblema = sqla.Column(sqla.String(100), nullable = False)
    origemReclamacao = sqla.relationship('OrigemReclamacao', backref = 'tblChamado', lazy = True)
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