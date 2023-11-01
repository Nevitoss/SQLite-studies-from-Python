import sqlite3

# Criar conexão com o BD
conexao = sqlite3.connect("Agenda.db")
cursor = conexao.cursor()

def visualizar_tabela():
    try:
        cursor.execute("SELECT * FROM Contatos")
        rows = cursor.fetchall()

        if len(rows) == 0:
            print("A tabela está vazia.")
        else:
            col_names = [description[0] for description in cursor.description]

            # Imprime cabeçalho da tabela
            print("{:<5} {:<20} {:<15} {:<30}".format(col_names[0], col_names[1], col_names[2], col_names[3]))
            print("=" * 70)

            # Imprime os dados da tabela formatados
            for row in rows:
                print("{:<5} {:<20} {:<15} {:<30}".format(row[0], row[1], row[2], row[3]))

    except sqlite3.Error as error:
        print("Erro ao tentar buscar dados na tabela:", error)

# Visualizar a tabela
visualizar_tabela()

# Fechar a conexão com o banco de dados
conexao.close()