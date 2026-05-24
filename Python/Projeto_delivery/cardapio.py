from banco import conexao

#consulta
def consulta_cardapio():

    cursor = conexao.cursor()
    sql = "SELECT * FROM cardapio"
    cursor.execute(sql)
    cardapio = cursor.fetchall()
    cursor.close()
    

    for item in cardapio:
        print (f"Nome: {item[1]} Preço: R$ {item[2]} Categoria: {item[3]} \n")
    return 

print(consulta_cardapio())