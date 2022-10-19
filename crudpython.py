import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='pythoncrud'
)

cursor = conexao.cursor()

# CRUD

# CREATE
# nome_produto = "todynho"
# valor = 3
# comando = f'INSERT INTO Vendas(nome_produto, valor) values("{nome_produto}", {valor})'
# cursor.execute(comando)
# conexao.commit()

# READ
# comando = f'SELECT * FROM Vendas'
# cursor.execute(comando)
# resultado = cursor.fetchall()  # Quando lendo o banco de dados
# print(resultado)

# UPDATE
# nome_produto = "todynho"
# valor = 6
# comando = f'UPDATE Vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit()

# DELETE
# nome_produto = "todynho"
# comando = f'DELETE FROM Vendas WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit()

cursor.close()
conexao.close()
