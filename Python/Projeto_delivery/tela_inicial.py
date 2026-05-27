import tkinter as tk
import subprocess
import sys

#funçoes
def tela_T():
    janela.destroy()


def tela_P():
    subprocess.Popen([sys.executable,"Projeto_delivery/tela_pedidos.py"])
    janela.destroy()

def tela_S():
    subprocess.Popen([sys.executable,"Projeto_delivery/tela_login.py"])
    janela.destroy()

#janela
janela = tk.Tk()

janela.title("Tela inicial")
janela.geometry("800x400")

#titulo central
label_titulo_central = tk.Label(   
    janela,
    text = "Escolha a tela",
    font = (
        "Arial",
        30
            ))
label_titulo_central.pack()

#botao trabalhador

botaoT = tk.Button(
    janela,
    text = "Trabalhador",
    command = tela_T,
    width = 20,
    height = 3
)
botaoT.pack(pady = 20)


#botao pedido

botaoP = tk.Button(
    janela,
    text = "Pedido",
    command = tela_P,
    width = 20,
    height = 3
)
botaoP.pack(pady=20)

#botao sair
botaoS = tk.Button(
    janela,
    text = "Logout",
    command = tela_S,
    width = 20, 
    height = 3
)
botaoS.pack(pady=20)
#inciar
janela.mainloop()