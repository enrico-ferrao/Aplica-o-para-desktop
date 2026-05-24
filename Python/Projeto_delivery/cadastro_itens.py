from banco import conexao


#cadastro do cardapio

def cadastro_itens():
    nome = input("Qual nome do item? ")
    preco = input("Qual valor do produto? ")
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


print(cadastro_itens())