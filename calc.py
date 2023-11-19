# CALCULADORA BÁSICA
from tkinter import *
janela = Tk()
janela.title("  *** C A L C U L A D O R A   B Á S I C A *** ")
janela.geometry("800x600")
janela.configure(bg="#908279")

def soma():
    n1 = int(texto_input.get())
    n2 = int(texto_input2.get())
    soma = n1 + n2
    resultado.configure(text=f"A soma dos números escolhidos foi {soma}")

def subtracao():
    n1 = int(texto_input.get())
    n2 = int(texto_input2.get())
    sub = n1 - n2
    resultado.configure(text=f"A subtração dos números escolhidos foi {sub}", background="yellow")

def multiplicacao():
    n1 = int(texto_input.get())
    n2 = int(texto_input2.get())
    mut = n1 * n2
    resultado.configure(text=f"A multiplicação dos números escolhidos foi {mut}", background="yellow")

def divisao():
    n1 = int(texto_input.get())
    n2 = int(texto_input2.get())
    div = n1 / n2
    resultado.configure(text=f"A divisão dos números escolhidos foi {div}", background="yellow")
    
def cadastro1():
    nome = nome_input.get().upper()
    cadastro_concluido.configure(text=f"Parabéns {nome}, seu cadastro foi concluído!")

nome = Label(text="Digite seu nome para cadastro: ")
nome.grid(row=1, column=1)

nome_input = Entry(width=40)
nome_input.grid(row=1, column=2)

botao_cadastro = Button(janela, text=f"Clique para completar o cadastro", command=cadastro1)
botao_cadastro.grid(row=1, column=3)

cadastro_concluido = Label(text="", bg="#908279")
cadastro_concluido.grid(row=15, column=1)

texto = Label(text="Escolha um número: ")
texto.grid(row=4, column=2)

texto_input = Entry()
texto_input.grid(row=5, column=2)

texto1 = Label(text="Escolha outro número: ")
texto1.grid(row=6, column=2)

texto_input2 = Entry()
texto_input2.grid(row=7, column=2)

resultado = Label(text="", bg="#908279", font="bold")
resultado.grid(row=13, column=2)

botao1 = Button(janela, text= "SOMA", command=soma, bg="black", fg="white")
botao1.grid(row=8, column=2)

botao2 = Button(janela, text= "SUBTRAÇÃO", command=subtracao, bg="black", fg="white")
botao2.grid(row=9, column=2)

botao3 = Button(janela, text= "MULTIPLICAÇÃO", command=multiplicacao, bg="black", fg="white")
botao3.grid(row=10, column=2)

botao4 = Button(janela, text= "DIVISÃO", command=divisao, bg="black", fg="white")
botao4.grid(row=11, column=2)

janela.mainloop()