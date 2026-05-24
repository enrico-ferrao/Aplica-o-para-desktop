from banco import conexao

#remover

def remover():
    login = input("Qual login deseja retirar? ")
    cursor = conexao.cursor()
    sql = "SELECT * FROM credenciais"
    cursor.execute(sql)
    dados = cursor.fetchall()
    for i in range (len(dados)):
        if dados[i][1] == login:
            sql = "DELETE FROM credenciais WHERE login = %s"
            cursor.execute(sql,(login,))
            conexao.commit()
            return "Usuario deletado!"
    return "Usuario não encontrado! "

#executando
print(remover())