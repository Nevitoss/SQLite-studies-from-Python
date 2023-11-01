#Programa para criar tabela num Banco de Dados usando Python
import os
os.remove("Agenda.db")if os.path.exists("Agenda.db")else None
import sqlite3
from sqlite3 import Error
#Criar conexão com o BD
conexao=sqlite3.connect("Agenda.db")
cursor=conexao.cursor()
#Criar tabela
vsql="""CREATE TABLE Contatos(
            N_IDCONTATO Inteiro Chave primária Autoincremento,
            T_NOMECONTATO Texto(30),
            T_TELEFONECONTATO Texto(14),
            T_EMAILCONTATO Texto(30)
        );"""
def criarTabela(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        print("Tabela criada")
    except Error as ex: #Se não conseguir conectar
        print(ex) #Mostrar o erro
criarTabela(conexao,vsql)
conexao.close()