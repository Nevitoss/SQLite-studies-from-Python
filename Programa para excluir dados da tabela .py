import sqlite3
from sqlite3 import Error

# Criar conexão com o BD
conexao = sqlite3.connect("Agenda.db")
cursor = conexao.cursor()

def inserir(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Registro inserido")
    except Error as ex:
        print(ex)

# Remover dados da tabela
def remover(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Registro removido")

def verificar_existencia(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    rows = c.fetchall()
    return rows

escolha = input("Como você gostaria de excluir o contato? Digite 'ID', 'nome', 'telefone' ou 'email': ").lower()

if escolha == 'id':
    ID_ = input('Digite um ID para excluir: ')
    vsql = f"SELECT * FROM Contatos WHERE N_IDCONTATO = '{ID_}'"
    resultado = verificar_existencia(conexao, vsql)

    if resultado:
        vsql = f"DELETE FROM Contatos WHERE N_IDCONTATO = '{ID_}'"
        remover(conexao, vsql)
    else:
        print("Nenhum registro encontrado com este ID.")

elif escolha == 'nome':
    nome = input('Digite um nome para excluir: ')
    vsql = f"SELECT * FROM Contatos WHERE T_NOMECONTATO = '{nome}'"
    resultado = verificar_existencia(conexao, vsql)

    if resultado:
        vsql = f"DELETE FROM Contatos WHERE T_NOMECONTATO = '{nome}'"
        remover(conexao, vsql)
    else:
        print("Nenhum registro encontrado com este nome.")
elif escolha == 'telefone':
    telefone = input('Digite um telefone para excluir: ')
    vsql = f"SELECT * FROM Contatos WHERE T_TELEFONECONTATO = '{telefone}'"
    resultado = verificar_existencia(conexao, vsql)

    if resultado:
        vsql = f"DELETE FROM Contatos WHERE T_TELEFONECONTATO = '{telefone}'"
        remover(conexao, vsql)
    else:
        print("Nenhum registro encontrado com este telefone.")

elif escolha == 'email':
    email = input('Digite um email para excluir: ')
    vsql = f"SELECT * FROM Contatos WHERE T_EMAILCONTATO = '{email}'"
    resultado = verificar_existencia(conexao, vsql)

    if resultado:
        vsql = f"DELETE FROM Contatos WHERE T_EMAILCONTATO = '{email}'"
        remover(conexao, vsql)
        
    else:
        print("Nenhum registro encontrado com este email.")
else:
    print("Escolha inválida. Por favor, escolha entre 'ID', 'nome', 'telefone' ou 'email'.")
