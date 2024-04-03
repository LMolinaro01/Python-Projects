import sqlite3

connection = sqlite3.connect("teste.db")

cursor = connection.cursor()
cursor.execute("CREATE TABLE Tabela (nome TEXT, curso TEXT, matricula INTEGER)")

cursor.execute("INSERT INTO Tabela VALUES ('Leonardo', 'Ciencia da Computacao', 123456)")

rows = cursor.execute("SELECT * FROM Tabela").fetchall()
print(rows)
