import tkinter as tk
from funcoes import *
import subprocess
import sys

#funcoes
def botao_l():
    janela.destroy()
    subprocess.Popen([sys.executable,"Projeto_delivery/tela_inicial.py"])

#janela

janela = tk.Tk()

janela.title ("Tela de Pedidos")
janela.geometry("1800x1080")

#texto cardapio
label_titulo_cardapio = tk.Label(janela, text = "Cardapio", font = ("Arial", 20))
label_titulo_cardapio.pack(pady = 10)

#quadrado
frame_cardapio = tk.Frame(janela, bg ="white", bd = 3, relief = "solid")
frame_cardapio.pack(pady = 20,padx = 20)

#imprimindo
produtos = consulta_cardapio()
for id_produto, nome, preco, categoria in produtos:
    cardapio = tk.Label(
            frame_cardapio,
            text = f" ID {id_produto} | {nome} | R$ {preco} | {categoria}",
            font = ("Arial", 10),
            bg = "white"
        )
    cardapio.pack (pady= 5, padx = 10)

label_titulo_add = tk.Label(janela,text = "Adicionar produtos do cardapio SGBD", font =("Arial", 10))
label_titulo_add.pack(anchor = "e", padx = 10)


frame_funcoes_add = tk.Frame (janela,bg = "white" ,bd = 3, relief = "solid")
frame_funcoes_add.pack(anchor = "e",pady = 10)
#titulo add
label_titulo_add = tk.Label(frame_funcoes_add, text = "Adicionar item")
label_titulo_add.pack(pady = 10, anchor = "e", padx =  70)
#nome produto add
label_nome_item = tk.Label(frame_funcoes_add, text = "Nome do produto")
label_nome_item.pack(anchor = "e", padx =  58)
entrada_nome_item = tk.Entry(frame_funcoes_add)
entrada_nome_item.pack(anchor = "e", padx =  50)

#preco produto add
label_preco_item = tk.Label(frame_funcoes_add, text = "Preco do produto")
label_preco_item.pack(anchor = "e", padx =  60)
entrada_preco_item = tk.Entry(frame_funcoes_add)
entrada_preco_item.pack(anchor = "e", padx =  50)

#categoria produto add
label_categoria_item = tk.Label(frame_funcoes_add, text = "Categoria do produto")
label_categoria_item.pack(anchor = "e", padx =  53)
entrada_categoria_item = tk.Entry(frame_funcoes_add)
entrada_categoria_item.pack(anchor = "e", padx =  50)


#botao de adicionar item
botao_add =tk.Button(
    frame_funcoes_add,
    text = "Adicionar item"
)
botao_add.pack(anchor = "e", padx =  68)


label_titulo_rmv = tk.Label(janela,text = "Remover produtos do cardapio SGBD", font = ("Arial", 10) )
label_titulo_rmv.pack(anchor = "e", padx = 10)

frame_funcoes_remover = tk.Frame (janela, bg = "white", bd = 3, relief = "solid")
frame_funcoes_remover.pack(anchor = "e" , pady = 10)


#titulo remover
label_titulo_remover = tk.Label(frame_funcoes_remover, text = "Remover item")
label_titulo_remover.pack(pady = 10, anchor = "e", padx =  69)
#remover produto
label_nome_remover = tk.Label(frame_funcoes_remover, text ="ID produto")
label_nome_remover.pack(anchor = "e", padx =  78)
entrada_nome_remover = tk.Entry(frame_funcoes_remover)
entrada_nome_remover.pack(anchor = "e", padx =  50)

#botao de remover item
botao_remover = tk.Button (
    frame_funcoes_remover,
    text = "Remover item"
)
botao_remover.pack(anchor = "e", padx =  68)

botao_incial = tk.Button(
    janela,
    text = "Tela incial",
    command = botao_l
)
botao_incial.pack()
#iniciar
janela.mainloop()
