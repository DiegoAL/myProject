'''
Created on 19 de set de 2019

@author: M206255
'''

'''
    Classe utilizada apenas para criar o banco de dados SQLite3
'''
import sqlite3

def main ():
    conn = sqlite3.connect('RegistroChamado.db')
    conn.close()
    
if __name__ == '__main__':
    main()

