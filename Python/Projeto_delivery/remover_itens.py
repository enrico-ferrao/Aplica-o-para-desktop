from banco import conexao

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
