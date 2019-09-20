'''
Created on 19 de set de 2019

@author: M206255
'''

'''
    Classe utilizada apenas para criar o banco de dados SQLite3
'''
import sqlite3

def main (local):
    conn = sqlite3.connect(local)
    conn.close()

def mainSemParametros ():
    conn = sqlite3.connect('RegistroChamado.db')
    conn.close()


'''!!! METODO TEMPORARIO ENQUANTO NÃO É DESENVOLVIDA A PAGINA DE CADASTRO NAS TABELAS!!!!'''
def TEMP_cargaDeDados():
    conn = sqlite3.connect('RegistroChamado.db')
    cursor = conn.cursor() 
    
    #lIMPANDO TABELAS
    cursor.execute(""" DELETE FROM tblTipoChamado """)
    conn.commit()
    cursor.execute(""" DELETE FROM tblSistema """)
    conn.commit()
    
    #Tabela de tipos
    cursor.execute(""" INSERT INTO tblTipoChamado (id, descricao, fkNumeroChamado) VALUES (1, 'Lentidão', 1)""")
    cursor.execute(""" INSERT INTO tblTipoChamado (id, descricao, fkNumeroChamado) VALUES (2, 'Oscilação', 1)""")
    cursor.execute(""" INSERT INTO tblTipoChamado (id, descricao, fkNumeroChamado) VALUES (3, 'Indisponibilidade', 1)""")
    
    #Tabela de tblSistema
    cursor.execute(""" INSERT INTO tblSistema (id, descricao, fkNumeroChamado) VALUES (1, 'Agencia Virtual', 1)""")
    cursor.execute(""" INSERT INTO tblSistema (id, descricao, fkNumeroChamado) VALUES (2, 'CRM', 1)""")
    cursor.execute(""" INSERT INTO tblSistema (id, descricao, fkNumeroChamado) VALUES (3, 'Workspace', 1)""")
    
    conn.commit()
    
    #print registros
    cursor.execute(""" SELECT * FROM tblTipoChamado""")
    for linha in cursor.fetchall():
        print(f'Tabela Tipo: {linha}')
    
    cursor.execute(""" SELECT * FROM tblSistema""")
    for linha in cursor.fetchall():
        print(f'Tabela Sistema: {linha}')


if __name__ == '__main__':
    mainSemParametros()
    TEMP_cargaDeDados()

