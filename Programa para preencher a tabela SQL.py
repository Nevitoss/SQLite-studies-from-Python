#Programa para inserir dados na tabela usando Python
import sqlite3
from sqlite3 import Error
#Criar conexão com o BD
conexao=sqlite3.connect("Agenda.db")
cursor=conexao.cursor()
 
ID=input("Digite o número de identificação do registro:")
nome=input("Digite o nome:")
telefone=input("Digite o telefone:")
email=input("Digite o email:")
vsql="insert into Contatos(N_IDCONTATO,T_NOMECONTATO,T_TELEFONECONTATO,T_EMAILCONTATO)Values('"+ID+"','"+nome+"','"+telefone+"','"+email+"')"
 
#Inserir dados na tabela
def inserir(conexao,sql):
   try:
       c=conexao.cursor()
       c.execute(sql)
       conexao.commit()
       print("Registro inserido")
   except Error as ex:
       print(ex)
inserir(conexao,vsql)