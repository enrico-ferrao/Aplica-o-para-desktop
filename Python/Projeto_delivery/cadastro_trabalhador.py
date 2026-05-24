from banco import conexao
#cadastrar

def cadastro_trabalhador():

    #coletando dados
    login = input("Digite seu usuario: ")
    senha = input("Digite sua senha: ")


    cursor = conexao.cursor()

    #verificar se o usuario ja existe
    sql = "SELECT * FROM credenciais WHERE login = %s"
    cursor.execute(sql,(login,))
    usuario = cursor.fetchone

    #caso ja existir
    if usuario:
        cursor.close()
        return "Usuario já cadastrado!"
    

    #inserindo novo usuario
    sql = "INSERT INTO credenciais (login,senha) VALUES (%s, %s)"
    cursor.execute(sql,valores)

    #final
    conexao.commit()
    cursor.close()
    return "Cadastrado!"

#executando

print(cadastro_trabalhador())




