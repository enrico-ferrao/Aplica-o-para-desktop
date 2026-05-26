from banco import conexao



#coleta e validação de login

def logins():
    login_usuario = input("Digite seu usuario: ")
    senha_usuario = input("Digite sua senha: ")
    cursor = conexao.cursor()
    sql = "SELECT login FROM credenciais WHERE nome = %s"
    cursor.execute(sql)
    dados = cursor.fetchone()
    cursor.close()
    if dados is None:
        return False
    if dados == login_usuario:


    
print(dados)


#finalizando
print(login())
