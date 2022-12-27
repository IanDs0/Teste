#bibliotecas necessarias, caso nao tenha instalada em sua maquina basta executar os comandos (pip install -r requirements.txt)
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

import pandas as pd
from time import sleep
import numpy as np
import os
import pyperclip

from tkinter import *
from tkinter import filedialog

import sys
sys.path.append('./Envio_Mensagem_com_Arquivo')

from mensagemArquivo import *

#start dados

contatos = []#Contatos/Grupos - Informar o nome(s) de Grupos ou Contatos que serao enviadas as mensagens

mensagem = ""#starta a mensagem

midia = ""#Midia = imagem, pdf, documento, video (caminho do arquivo, lembrando que mesmo no windows o caminho deve ser passado com barra invertida */* ) 

#incia os grupos
grupoContatos = pd.read_csv("./csv/planilhaGrupos.csv")

#inicia nomes dos padroes
nomes = grupoContatos.columns

#filtar dos contatos os que devem ser enviados
def getContato(Filtro):
    #leitura e filtragem
    salvo = pd.read_csv("./csv/Contatos.csv")
    salvo = salvo['Contatos'].values

    #array com os ontatos a serem enviados
    envio = []

    for busca in Filtro:
        for contact in salvo:
            if contact.startswith(busca):
                envio.append(contact)

    return envio

#gera o array de envio
def concatGrups(array):
    padrao = []
    contatos.clear()
    for i in range(np.size(array)):
        padrao.append(nomes[array[i]])


    print(padrao)
    contatos.extend(getContato(padrao))

def interface():
    
    posGrupos = []
    mensagem = ''
    midia = ''

    def dadosMensagem():
        men = inputMensagem.get(1.0, "end-1c")
        if men == "":
            lbl.config (text = "Não tem TEXTO para evio das mensagens")
        else:
            
            aux = False

            posGrupos.clear()
            
            for i in range(np.size(chkValue)):
                if chkValue[i].get() == True:
                    posGrupos.append(i)
                    aux = True
            
            if (True == aux):
                midia = procuraArquivo()

                if(midia != ""):
                    concatGrups(posGrupos)
                    mensagem = str(men)

                    status = ''

                    enviar(mensagem,midia,driver,status,contatos)

                    if status == 'Enviado':
                        lbl.config (text = ("Enviando a mensagens: \n" + men + "\n Arquivo: \n" + midia))
                    else:
                        lbl.config (text = ("O envio das mensagens foi cancelado"))

                else:
                    lbl.config (text = "Não tem ARQUIVO para evio das mensagens")
            else:
                lbl.config (text = ("Selecione pelo menos um grupo"))
            

    #Pegar o arquivo a ser enviado
    def procuraArquivo(): 
        filename = filedialog.askopenfilename(initialdir = "/", 
            title = "Select a File", 
            filetypes = (("all files", "*.*"),("all files", "*.*"))) 
        
        return filename

    root = Tk()

    inputMensagem = Text(root)
    inputMensagem["height"] = 5
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

    chkValue = []
    for i in range(np.size(nomes)):

        chkValue.append(BooleanVar()) 
        chkValue[i].set(False)
        
        chkExample = Checkbutton(root, text=nomes[i], var=chkValue[i]) 
        chkExample.pack()

    root.iconphoto(False, PhotoImage(file='./img/icon.png'))
    # root.iconphoto(False, PhotoImage(file='./img/icon.jpeg'))
    root.mainloop()

""" 
Abre o Firefox
driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com") #abre o site Whatsapp Web
 """

dir_path = os.getcwd()
profile = os.path.join(dir_path, "profile", "wpp")
options = webdriver.ChromeOptions()

#tira a tela
# options.add_argument("--headless")

options.add_argument(r"user-data-dir={}".format(profile))

driver = webdriver.Chrome('./chromedriver.exe',chrome_options=options)

driver.get("https://web.whatsapp.com")


try:
    while len(driver.find_elements(By.ID, 'side')) < 1:
        sleep(0.1)
    sleep(0.1) # só uma garantia

    print("OK")

    interface()

    driver.quit()
except:
    print("Close")

    driver.quit()