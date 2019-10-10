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

def getConnect (local):
    return sqlite3.connect(local)


'''!!! METODO TEMPORARIO ENQUANTO NÃO É DESENVOLVIDA A PAGINA DE CADASTRO NAS TABELAS!!!!'''
def TEMP_cargaDeDados():
    conn = sqlite3.connect('RegistroChamado.db')
    
    #Ativar foreign key do sqlite3
    conn.execute('PRAGMA foreign_keys = ON')
    
    cursor = conn.cursor() 
    
    #lIMPANDO TABELAS
    '''
    cursor.execute(""" DELETE FROM tblTipoChamado """)
    conn.commit()
    cursor.execute(""" DELETE FROM tblSistema """)
    conn.commit()
    cursor.execute(""" DELETE FROM tblOrigemReclamacao """)
    conn.commit()
    cursor.execute(""" DELETE FROM tblStatus """)
    conn.commit()
    #cursor.execute(""" DELETE FROM tblChamado """)
    #conn.commit()
    
    '''
    #Tabela de tipos
    cursor.execute(""" INSERT INTO tblTipoChamado (descricao) VALUES ('Lentidão')""")
    cursor.execute(""" INSERT INTO tblTipoChamado (descricao) VALUES ('Oscilação')""")
    cursor.execute(""" INSERT INTO tblTipoChamado (descricao) VALUES ('Indisponibilidade')""")
    
    #Tabela de tblSistema
    cursor.execute(""" INSERT INTO tblSistema (descricao) VALUES ('Agencia Virtual')""")
    cursor.execute(""" INSERT INTO tblSistema (descricao) VALUES ('CRM')""")
    cursor.execute(""" INSERT INTO tblSistema (descricao) VALUES ('Workspace')""")
    
    #Tabela de Origem
    cursor.execute(""" INSERT INTO tblOrigemReclamacao (area) VALUES ('Call Center - Santos')""")
    cursor.execute(""" INSERT INTO tblOrigemReclamacao (area) VALUES ('Linha Direta')""")
    cursor.execute(""" INSERT INTO tblOrigemReclamacao (area) VALUES ('Clientes Corporativos (CRC)')""")
    
    #Tabela de Status
    cursor.execute(""" INSERT INTO tblStatus (descStatus) VALUES ('Aberto')""")
    cursor.execute(""" INSERT INTO tblStatus (descStatus) VALUES ('Em Analise')""")
    cursor.execute(""" INSERT INTO tblStatus (descStatus) VALUES ('Encerrado')""")
    
     #Tabela de Chamados
    cursor.execute(""" INSERT INTO tblChamado (dataAbertura, statusChamado, solicitanteNome, solicitanteTelefone,solicitanteLocalidade, tipo, sistema, origemReclamacao, tempoLentidao, descricaoProblema,processoConclui, problemaLojas, problemaEmAllWSLojas, problemaEnel, problemaEmAllWSEnel,problemaCCenter, chamadoAberto, nmrChamadoAberto, contatoNome, contatoTelefone, contatoLocalidade) VALUES ('15/06/1995', 2,'Teste','Teste','Teste',1,2,1,3, 'Teste', 'Teste', 'Teste', 'Teste', 'Teste', 'Teste', 'Teste', 'Teste', 'Teste', 'Teste', 'Teste', 'Teste' )""")
    conn.commit()
    
    #print registros
    cursor.execute(""" SELECT * FROM tblTipoChamado""")
    for linha in cursor.fetchall():
        print(f'Tabela Tipo: {linha}')
    print('\n')
    
    cursor.execute(""" SELECT * FROM tblSistema""")
    for linha in cursor.fetchall():
        print(f'Tabela Sistema: {linha}')
    print('\n')    
        
    cursor.execute(""" SELECT * FROM tblOrigemReclamacao  """)
    for item in cursor.fetchall():
        print(f'Tabela OrigemReclamacao: {item}')
    print('\n')
        
    cursor.execute(""" SELECT * FROM tblStatus  """)
    for item in cursor.fetchall():
        print(f'Tabela Status: {item}')
    print('\n') 
    
    cursor.execute(""" SELECT * FROM tblChamado  """)
    for item in cursor.fetchall():
        print(f'Tabela Status: {item}')
    print('\n') 
     
def schemaPrint (nomeTable):
    conn = sqlite3.connect('RegistroChamado.db')
    cursor = conn.cursor() 
    # obtendo o schema da tabela
    cursor.execute("""
    SELECT sql FROM sqlite_master WHERE type='table' AND name=?
    """, (nomeTable,))

    print('Schema:')
    for schema in cursor.fetchall():
        print("%s" % (schema))
    
            
if __name__ == '__main__':
    mainSemParametros()
    #TEMP_cargaDeDados()
    
    conn = sqlite3.connect('RegistroChamado.db')
    #Ativar foreign key do sqlite3
    conn.execute('PRAGMA foreign_keys = ON')
    cursor = conn.cursor() 
    
    #cursor.execute(""" INSERT INTO tblChamado (dataAbertura, statusChamado, solicitanteNome, solicitanteTelefone,solicitanteLocalidade, tipo, sistema, origemReclamacao, tempoLentidao, descricaoProblema,processoConclui, problemaLojas, problemaEmAllWSLojas, problemaEnel, problemaEmAllWSEnel,problemaCCenter, chamadoAberto, nmrChamadoAberto, contatoNome, contatoTelefone, contatoLocalidade) VALUES ('15/06/1995', 2,'Teste','Teste','Teste','Oscilação',1,1,3, 'Teste', 'Teste', 'Teste', 'Teste', 'Teste', 'Teste', 'Teste', 'Teste', 'Teste', 'Teste', 'Teste', 'Teste' )""")
    #conn.commit()
    
    cursor.execute(""" DELETE FROM tblChamado """)
    conn.commit()
        
    cursor.execute(""" SELECT * FROM tblChamado  """)
    for item in cursor.fetchall():
        print(f'Tabela Status: {item}')
    print('\n')    

