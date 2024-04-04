import sqlite3

connection = sqlite3.connect("teste.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Alunos (nome TEXT, matricula INTEGER, cpf INTEGER, curso TEXT, periodo INTEGER)")

def adicionarAluno(nome, matricula, cpf, curso, periodo):
    caracteres_especiais = ";-'!+,:."
    if any(caracter in caracteres_especiais for caracter in str(matricula) + str(cpf) + str(periodo)):
        print("Caracteres especiais não são permitidos.")
    else:
        cursor.execute("INSERT INTO Alunos (nome, matricula, cpf, curso, periodo) VALUES (?, ?, ?, ?, ?)", (nome, matricula, cpf, curso, periodo))
        connection.commit()

def buscarAluno(nome_ou_matricula):
    try:
        busca = int(nome_ou_matricula)
        cursor.execute("SELECT nome FROM Alunos WHERE matricula = ?", (busca,))
    except ValueError:
        cursor.execute("SELECT nome FROM Alunos WHERE nome = ?", (nome_ou_matricula,))
    aluno = cursor.fetchone()
    if aluno:
        print(f"Aluno encontrado: {aluno[0]}")
    else:
        print("Aluno não encontrado.")

adicionarAluno("Leonardo", 12345, 20011111111, "Ciência da Computação", 3)
buscarAluno("Leonardo")
buscarAluno(12345
