import socket
import threading

from tkinter import *
from tkinter import filedialog

MEU_IP = ''  
 # Endereco IP do Servidor, '' = significa que ouvira em todas as interfaces

MINHA_PORTA = 8000  
# Porta que o Servidor vai ouvir 

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET = INET (exemplo IPv4)sockets, #socket.SOCK_STREAM=usaremos TCP

#x = 1
testa_mensagem = '127.0.0.1'
MEU_SERVIDOR = (MEU_IP, MINHA_PORTA) 
tcp.bind(MEU_SERVIDOR)
 # faz o bind do ip e a porta para que possa comecar a ouvir

tcp.listen(1) 
#comeca a ouvir

users = []
#dados de cada usuário

conexao, docliente =tcp.accept()
print ("o cliente = ", docliente, " se conectou")
#pega o ip do cliente que conectou

user = {'apelido':'', 'ip':'', 'cont':0}

def recebendoMensagem(lbl,conversa):
  while 1:
    Mensagem = ''
    #Recebe mensagem
    Mensagem_Recebida = conexao.recv(1024).decode("utf-8")
    #Mensagem recebida do cliente 
    if testa_mensagem != Mensagem_Recebida:  
      
    #aqui verifica se exite mensagem nova  
      if user['cont'] == 0:
        user['apelido'] = Mensagem_Recebida
        user['ip'] = docliente
        # users.append(user.copy)
        
        Mensagem = "Nome: "+ user['apelido'] +" recebido"
        conversa.append(Mensagem)
        lbl.config(text = conversa)

        user['cont'] = 1

      else:
        Mensagem = user['apelido'] +": "+ Mensagem_Recebida
        conversa.append(Mensagem)
        lbl.config(text = conversa)

def interface():

    conversa = []

    def dadosMensagem():
        Mensagem = inputMensagem.get(1.0, "end-1c")
        if Mensagem != "":
            conexao.send(bytes(Mensagem,"utf8"))
            if user['apelido'] == '':
                Mensagem = 'Eu: ' + Mensagem+"\n"
                conversa.append(Mensagem)
                lbl.config(text = conversa)
            else:
                Mensagem = user['apelido'] + ': ' + Mensagem+"\n"
                conversa.append(Mensagem)
                lbl.config(text = conversa)

    def close():
        conexao.close()

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
    mensagemButton["text"] = "Fechar conexão"
    mensagemButton["command"] = close
    mensagemButton.pack()

    threading.Thread(target=recebendoMensagem, args=(lbl,conversa,)).start()
    root.mainloop()

interface()

conexao.close()
# finalizar o socket