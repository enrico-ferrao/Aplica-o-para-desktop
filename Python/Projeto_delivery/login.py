from banco import conexao

#testador
def teste_senha(login,senha,dados):
    for i in range (len(dados)):
        if dados[i][1] == login:   
            if dados[i][2] == senha:
                return "Bem vindo usuario!"
    return "error: login or senha incorret! "

#coletando logins

def logins():
    login_usuario = input("Digite seu usuario: ")
    senha_usuario = input("Digite sua senha: ")
    return login_usuario,senha_usuario

#validando logins
def autentificador():
    cursor = conexao.cursor()
    sql = "SELECT * FROM credenciais"
    cursor.execute(sql)
    dados = cursor.fetchall()
    cursor.close()
    return dados


#finalizando
att = logins()

banco = autentificador()

print(teste_senha(att[0],att[1],banco))

