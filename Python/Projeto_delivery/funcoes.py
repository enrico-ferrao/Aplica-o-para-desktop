import requests
from banco import conexao


#coleta e validação de login
def logins(login_usuario, senha_usuario):

    cursor = conexao.cursor(buffered=True)
    sql = "SELECT login,senha FROM credenciais WHERE login = %s"
    cursor.execute(sql,(login_usuario,))
    dados = cursor.fetchone()
    cursor.close()
    if dados is None:
        return False
    if dados[1] == senha_usuario:
        return True
    else:
        return False

#cadastrar
def cadastro_trabalhador():

    #coletando dados
    login = input("Digite seu usuario: ")
    senha = input("Digite sua senha: ")


    cursor = conexao.cursor()

    #verificar se o usuario ja existe
    sql = "SELECT * FROM credenciais WHERE login = %s"
    cursor.execute(sql,(login,))
    usuario = cursor.fetchall()

    #caso ja existir
    if usuario:
        cursor.close()
        return "Usuario já cadastrado!"
    

    #inserindo novo usuario
    sql = "INSERT INTO credenciais (login,senha) VALUES (%s, %s)"
    cursor.execute(sql,(login,senha,))

    #final
    conexao.commit()
    cursor.close()
    return "Cadastrado!"

#remover
def remover_trabalhador():
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



#consulta
def consulta_cardapio():

    cursor = conexao.cursor()
    sql = "SELECT * FROM cardapio"
    cursor.execute(sql)
    cardapio = cursor.fetchall()
    cursor.close()
    
    return cardapio

#cadastro do cardapio
def cadastro_itens():
    nome = input("Qual nome do item? ")
    preco = input("Qual valor do produto? ").replace(",",".")
    categoria = input("Qual categoria do produto? ")
    
    cursor = conexao.cursor()

    #verificando se já existe
    sql = "SELECT nome FROM cardapio WHERE nome = %s"
    cursor.execute(sql,(nome,))

    item = cursor.fetchone()

    if item == nome:
        cursor.close
        return "Item ja cadastrado!"
    
    #cadastrando item
    sql = "INSERT INTO cardapio (nome,preco,categoria) VALUES (%s,%s,%s)"
    cursor.execute(sql,(nome,preco,categoria))

    conexao.commit()
    cursor.close()
    return "Item cadastrado!"

def remover_itens():
    item = input("Qual item você deseja remover? ")

    cursor = conexao.cursor()
    sql = "SELECT nome FROM cardapio where nome = %s"
    cursor.execute(sql,(item,))
    nome = cursor.fetchone()

    if nome:
        sql = "DELETE FROM cardapio WHERE nome = %s"
        cursor.execute(sql,(item,))
        conexao.commit()
        cursor.close()
        return "Item deletado!"
    
    cursor.close()
    return "Item não encontrado!"


#calculador de frete
def calcular_frete():
    rua = input("Qual o nome da rua? ").replace(" ","+")
    url = f"https://nominatim.openstreetmap.org/search?q={rua}&format=json"
    
