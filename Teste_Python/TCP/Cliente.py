import socket
import threading

from tkinter import *
from tkinter import filedialog

IP_Servidor = '127.0.0.1'             
# Endereco IP do Servidor

PORTA_Servidor = 8000
# Porta em que o servidor estara ouvindo

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET = INET (exemplo IPv4)sockets, #socket.SOCK_STREAM=usaremos TCP

DESTINO = (IP_Servidor, PORTA_Servidor) 
#destino(IP + porta)

tcp.connect(DESTINO) 
# inicia a conexao TCP

testa_mensagem=''

user = {'apelido':'', 'server':'', 'cont':0}   

def recebendoMensagem(lbl,conversa):    
    while True:
        Mensagem = ''
        #Recebe mensagem
        Mensagem_Recebida = tcp.recv(1024).decode("utf-8")
        #Mensagem recebida do cliente 
        if testa_mensagem != Mensagem_Recebida:  
        #aqui verifica se exite mensagem nova  
            if user['cont'] == 0:
                user['apelido'] = Mensagem_Recebida
                user['server'] = DESTINO
                
                Mensagem = "Apelido: "+ user['apelido'] +" recebido"+"\n"
                
                conversa.append(Mensagem)
                lbl.config(text = conversa)
                user['cont'] = 1
            else:
                Mensagem = user['apelido'] +": "+ Mensagem_Recebida+"\n"
                
                conversa.append(Mensagem)
                lbl.config(text = conversa)

def interface():

    conversa = []

    def dadosMensagem():
        Mensagem = inputMensagem.get(1.0, "end-1c")
        if Mensagem != "":
            tcp.send(bytes(Mensagem,"utf8"))
            if user['apelido'] == '':
                Mensagem = 'Eu: ' + Mensagem+"\n"
                conversa.append(Mensagem)
                lbl.config(text = conversa)
            else:
                Mensagem = user['apelido'] + ': ' + Mensagem+"\n"
                conversa.append(Mensagem)
                lbl.config(text = conversa)

    def close():
        tcp.close()

    root = Tk()

    inputMensagem = Text(root)
    inputMensagem["height"] = 2
    inputMensagem["width"] = 50
    inputMensagem["wrap"] = WORD
    inputMensagem.grid(column=0, row=0, padx=10, pady=10)
    inputMensagem.pack()

    lbl = Label(root)
    lbl["text"] = ""
    lbl.pack()

    mensagemButton = Button(root) 
    mensagemButton["text"] = "Enviar Mensagens"
    mensagemButton["command"] = dadosMensagem
    mensagemButton.pack()

    mensagemButton = Button(root) 
    mensagemButton["text"] = "Fechar"
    mensagemButton["command"] = close
    mensagemButton.pack()

    threading.Thread(target=recebendoMensagem, args=(lbl,conversa,)).start()
    root.mainloop()

interface()

tcp.close()
# finalizar o socket