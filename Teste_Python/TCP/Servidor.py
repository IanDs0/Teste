import socket
import threading
import os
import shutil

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

if os.path.isdir('./servidor') == False:
    path = os.path.join('./', 'servidor')
    os.mkdir(path)
else:
    shutil.rmtree('./servidor')
    path = os.path.join('./', 'servidor')
    os.mkdir(path)

def recebendoMensagem(lbl,conversa):
  conteudoComando = []
  while 1:

    Mensagem = ''
    #Recebe mensagem
    Mensagem_Recebida = conexao.recv(1024)
    #Mensagem recebida do cliente 

    #aqui verifica se exite mensagem nova 
    try:
        Mensagem_Recebida = Mensagem_Recebida.decode("utf-8") 
        if testa_mensagem != Mensagem_Recebida:  
          conteudoComando = Mensagem_Recebida.split('|')
          
          match conteudoComando[0]:

            case '#arquivo':
              print('arquivo')
              saveArquivo(conteudoComando,user['apelido'],lbl,conversa)


            case '#apelido':
              user['apelido'] = conteudoComando[1]
              user['ip'] = docliente

              path = os.path.join('./', 'cliente')
              newPath = os.path.join('./', user['apelido'])
              os.rename(path,newPath)

              Mensagem = "Apelido recebido: "+ conteudoComando[1] +" \n"
              conversa.append(Mensagem)
              lbl.config(text = conversa)

            case _:
              if user['apelido'] != '':
                Mensagem = user['apelido'] +": "+ Mensagem_Recebida+"\n"
                
                conversa.append(Mensagem)
                lbl.config(text = conversa)
              else:
                Mensagem = "Desconhecido: "+ Mensagem_Recebida+"\n"
                
                conversa.append(Mensagem)
                lbl.config(text = conversa)

    except:
      if user['apelido'] != '':
        Mensagem = user['apelido'] +": "+ Mensagem_Recebida+"\n"
        
        conversa.append(Mensagem)
        lbl.config(text = conversa)
      else:
        Mensagem = "Desconhecido: "+ Mensagem_Recebida+"\n"
        
        conversa.append(Mensagem)
        lbl.config(text = conversa)


def saveArquivo (conteudoComando,apelido,lbl,conversa):
  
  end = bytes("#enviado","utf8")

  if user['apelido'] != '':
    path = os.path.join('./'+apelido+'/'+conteudoComando[1])
  else:
    path = os.path.join('./servidor/'+conteudoComando[1])
  
  arq = open(path, 'wb')

  while 1:
      dados = conexao.recv(1024)
      if dados == end:
        print("\rrecebendo...")
        break
      arq.write(dados)
  arq.close()

  Mensagem = "O arquivo: "+conteudoComando[1]+"\nsalvo na pasta: "+path

  conversa.append(Mensagem)
  lbl.config(text = conversa)

  print("\rRecebido")

def interface():

    conversa = []

    def sendMensagem():
        Mensagem = inputMensagem.get(1.0, "end-1c")
        if Mensagem != "":
            conexao.send(bytes(Mensagem,"utf8"))
            Mensagem = 'Eu: ' + Mensagem+"\n"
            conversa.append(Mensagem)
            lbl.config(text = conversa)

    def close():
        conexao.close()

    #Pegar o arquivo a ser enviado
    def procuraArquivo(): 
        filename = filedialog.askopenfilename(initialdir = "/", 
          title = "Select a File", 
          filetypes = (("all files", "*.*"),("all files", "*.*"))) 
        
        name = filename.split('/')
        file_size = os.path.getsize(filename)
        aviso = '#arquivo|'+name[-1]+'|'+str(file_size)
        conexao.send(bytes(aviso,"utf8"))

        ###############################################
        print(filename)

        arquivo = open (filename, "rb")
        ler_buffer = arquivo.read(1024) 
        while (ler_buffer):
            print("\renviando...")
            conexao.send(ler_buffer) 
            ler_buffer = arquivo.read(1024)
        conexao.send(bytes("#enviado","utf8"))
        print("arquivo enviado")
        ################################################

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
    mensagemButton["command"] = sendMensagem
    mensagemButton.pack()

    button_explore = Button(root)  
    button_explore["text"] = "Enviar Arquivo" 
    button_explore["command"] = procuraArquivo
    button_explore.pack()

    mensagemButton = Button(root) 
    mensagemButton["text"] = "Fechar conexão"
    mensagemButton["command"] = close
    mensagemButton.pack()

    threading.Thread(target=recebendoMensagem, args=(lbl,conversa,)).start()
    root.mainloop()

interface()

conexao.close()
# finalizar o socket

#O comando #apelido envia seu nome
#O comando #arquivo envia os dads de como será o arquivo enviado