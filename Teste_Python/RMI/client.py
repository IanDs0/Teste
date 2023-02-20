import Pyro4
import tkinter as tk
from datetime import datetime

uri = "PYRO:obj_a7a603cfa8a4418799f8dd84df78cd8f@localhost:63137"
obj = Pyro4.Proxy(uri)



def enviar():
    texto1 = campo_texto1.get()
    texto2 = campo_texto2.get()
    opcao = var_opcao.get()
    resultado = f""

    match opcao:
        # Aeroporto
        case "add_aeroporto":
            resultado = obj.add_aeroporto(texto1, texto2)

        case "get_aeroporto":
            resultado = obj.get_aeroporto()

        case "get_aeroporto_id":
            resultado = obj.get_aeroporto_id(texto1)

        case "update_aeroporto":
            resultado = obj.update_aeroporto(texto1, texto2)

        case "delete_aeroporto":
            resultado = obj.delete_aeroporto(texto1)


        # Companhia Aérea
        case "add_companhia":
            resultado = obj.add_companhia(texto1, texto2)

        case "get_companhia":
            resultado = obj.get_companhia()

        case "get_companhia_id":
            resultado = obj.get_companhia_id(texto1)

        case "update_companhia":
            resultado = obj.update_companhia(texto1, texto2)

        case "delete_companhia":
            resultado = obj.delete_companhia(texto1)


        # Aeroporto_Companhia
        case "add_aeroporto_companhia":
            now = datetime.now()
            horario = now.strftime("%I:%M").lstrip("0").replace(":00", "")
            resultado = obj.add_aeroporto_companhia(texto1, texto2, horario)

        case "get_aeroporto_companhia":
            resultado = obj.get_aeroporto_companhia()

        case "get_aeroporto_companhia_id":
            resultado = obj.get_aeroporto_companhia_id(texto1)

        case "update_aeroporto_companhia":
            now = datetime.now()
            horario = now.strftime("%I:%M").lstrip("0").replace(":00", "")
            resultado = obj.update_aeroporto_companhia(texto1, horario)

        case "delete_aeroporto_companhia" :
            resultado = obj.delete_aeroporto_companhia(texto1)
        
        case _:
            resultado = f"Texto 1: {texto1}\nTexto 2: {texto2}\nOpção selecionada: {opcao}"
    campo_resposta.configure(state='normal')
    campo_resposta.delete('1.0', 'end')
    campo_resposta.insert('1.0', resultado)
    campo_resposta.configure(state='disabled')

janela = tk.Tk()
janela.title("Minha Janela")

# Criação dos campos de texto
label_texto1 = tk.Label(janela, text="Texto 1:")
label_texto1.pack()
campo_texto1 = tk.Entry(janela)
campo_texto1.pack()

label_texto2 = tk.Label(janela, text="Texto 2:")
label_texto2.pack()
campo_texto2 = tk.Entry(janela)
campo_texto2.pack()

# Criação do campo select
opcoes = [
    "add_aeroporto",
    "get_aeroporto",
    "get_aeroporto_id",
    "update_aeroporto",
    "delete_aeroporto",
    "add_companhia",
    "get_companhia",
    "get_companhia_id",
    "update_companhia",
    "delete_companhia",
    "add_aeroporto_companhia",
    "get_aeroporto_companhia",
    "get_aeroporto_companhia_id",
    "update_aeroporto_companhia",
    "delete_aeroporto_companhia",
]
var_opcao = tk.StringVar(janela)
var_opcao.set(opcoes[0])
label_opcao = tk.Label(janela, text="Selecione uma opção:")
label_opcao.pack()
campo_opcao = tk.OptionMenu(janela, var_opcao, *opcoes)
campo_opcao.pack()

# Criação do botão "Enviar"
botao_enviar = tk.Button(janela, text="Enviar", command=enviar)
botao_enviar.pack()

# Criação do campo de resposta
label_resposta = tk.Label(janela, text="Resposta:")
label_resposta.pack()
campo_resposta = tk.Text(janela, state='disabled', width=30, height=5)
campo_resposta.pack()

janela.mainloop()


print(resultado)
