import sqlite3

def criar_tabela():
    conn = sqlite3.connect('agenda.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contatos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL,
            email TEXT,
            endereco TEXT,
            cpf TEXT
        )
    ''')
    conn.commit()
    conn.close()

def adicionar_contato(nome, telefone, email, endereco, cpf):
    conn = sqlite3.connect('agenda.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO contatos (nome, telefone, email, endereco, cpf)
        VALUES (?, ?, ?, ?, ?)
    ''', (nome, telefone, email, endereco, cpf))
    conn.commit()
    conn.close()
    print("Contato adicionado com sucesso!")

def listar_contatos():
    conn = sqlite3.connect('agenda.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contatos')
    contatos = cursor.fetchall()
    conn.close()

    if contatos:
        for contato in contatos:
            print(f"ID: {contato[0]}")
            print(f"Nome: {contato[1]}")
            print(f"Telefone: {contato[2]}")
            print(f"Email: {contato[3]}")
            print(f"Endereço: {contato[4]}")
            print(f"CPF: {contato[5]}")
            print("-" * 30)
    else:
        print("Nenhum contato encontrado.")

def buscar_contato(nome):
    conn = sqlite3.connect('agenda.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contatos WHERE nome LIKE ?', ('%' + nome + '%',))
    contatos = cursor.fetchall()
    conn.close()

    if contatos:
        for contato in contatos:
            print(f"ID: {contato[0]}")
            print(f"Nome: {contato[1]}")
            print(f"Telefone: {contato[2]}")
            print(f"Email: {contato[3]}")
            print(f"Endereço: {contato[4]}")
            print(f"CPF: {contato[5]}")
            print("-" * 30)
    else:
        print("Contato não encontrado.")

def remover_contato(id_contato):
    conn = sqlite3.connect('agenda.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM contatos WHERE id = ?', (id_contato,))
    conn.commit()
    conn.close()
    print("Contato removido com sucesso!")

def menu():
    criar_tabela()
    while True:
        print("\n=== AGENDA DE CONTATOS ===")
        print("1 - Adicionar contato")
        print("2 - Listar contatos")
        print("3 - Buscar contato")
        print("4 - Remover contato")
        print("5 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            endereco = input("Endereço: ")
            cpf = input("CPF: ")
            adicionar_contato(nome, telefone, email, endereco, cpf)
        elif escolha == '2':
            listar_contatos()
        elif escolha == '3':
            nome = input("Digite o nome para busca: ")
            buscar_contato(nome)
        elif escolha == '4':
            id_contato = input("Digite o ID do contato para remover: ")
            remover_contato(id_contato)
        elif escolha == '5':
            print("Saindo da agenda...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__": 
    menu()
