import tkinter as tk
from tkinter import messagebox
from funcoes import logins
import subprocess
import sys

def autentificacao():

    usuario = entrada_usuario.get()
    senha =  entrada_senha.get()

    resultado = logins(usuario,senha)

    if resultado:
        janela.destroy()
        subprocess.Popen([sys.executable,"Projeto_delivery/tela_inicial.py"])

    else:
        messagebox.showinfo(
            "Error",
            "login ou senha incorreta"
        )
        

#janela
janela = tk.Tk()

janela.title ("Tela de Login")
janela.geometry("300x150")

#texto usuario
label_usuario = tk.Label(janela, text = "Usuario")
label_usuario.pack()

entrada_usuario = tk.Entry(janela)
entrada_usuario.pack()

#texto senha
label_senha = tk.Label(janela, text = "Senha") 
label_senha.pack()

entrada_senha = tk.Entry(janela)
entrada_senha.pack()


#botao

botao = tk.Button(
    janela,
    text = "Entrar",
    command = autentificacao
)

botao.pack()

#inciar
janela.mainloop()