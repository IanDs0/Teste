#bibliotecas necessarias, caso nao tenha instalada em sua maquina basta executar os comandos (pip instal....)
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import pandas as pd
from time import sleep
import numpy as np
import os
import threading
import pyperclip

from tkinter import *
from tkinter import filedialog 
from tkinter import ttk

from PIL import Image, ImageTk

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.firefox.options import Options

#start dados

#Contatos/Grupos - Informar o nome(s) de Grupos ou Contatos que serao enviadas as mensagens
contatos = []

#starta a mensagem
mensagem = ""

#Midia = imagem, pdf, documento, video (caminho do arquivo, lembrando que mesmo no windows o caminho deve ser passado com barra invertida */* ) 
midia = ""

#incia os grupos
grupoContatos = pd.read_csv("./planilhaGrupos.csv")

#inicia nomes dos padroes
nomes = grupoContatos.columns

#Funcao que pesquisa o Contato/Grupo
def buscar_contato(contato):
    campo_pesquisa = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/button')
    campo_pesquisa.click()

    ActionChains(driver)\
                .pause(0.3)\
                .key_down(Keys.CONTROL)\
                .send_keys('a')\
                .key_up(Keys.CONTROL)\
                .send_keys(Keys.DELETE)\
                .perform()

    driver.find_element(By.XPATH,'//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]').send_keys(contato)

    sleep(0.3)

    while True:
        if driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]').text != contato:

            ActionChains(driver)\
                .pause(0.3)\
                .key_down(Keys.CONTROL)\
                .send_keys('a')\
                .key_up(Keys.CONTROL)\
                .send_keys(Keys.DELETE)\
                .perform()

            driver.find_element(By.XPATH,'//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]').send_keys(contato)
            
            print('erro')
        else:
            break
    
    driver.find_element(By.XPATH,'//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]').send_keys(Keys.ENTER)

#Funcao que envia a mensagem
def enviar_mensagem(mensagem):

    # nomeContato = ''#driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]').text
    
    while driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]').text == '':
        print("\n-tenta-\n")
        pyperclip.copy(mensagem);
        ActionChains(driver)\
            .key_down(Keys.CONTROL)\
            .send_keys('v')\
            .key_up(Keys.CONTROL)\
            .perform()
            
        # nomeContato = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]').text

        # for i in range(np.size(mensagem)):
        #     if mensagem[i] == ' | ':
        #         ActionChains(driver)\
        #             .key_down(Keys.SHIFT)\
        #             .send_keys(Keys.ENTER)\
        #             .key_up(Keys.SHIFT)\
        #             .perform()
        #     else:
        #         ActionChains(driver)\
        #             .send_keys(mensagem[i])\
        #             .perform()
    ActionChains(driver)\
        .pause(0.3)\
        .send_keys(Keys.ENTER)\
        .perform()

#Funcao que envia midia como mensagem
def enviar_midia(midia):
    
    while len(driver.find_elements(By.XPATH,'/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span')) < 1:
        sleep(0.0001)

    #abre opção de upar arquivo
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span').click()
    
    #upa o arquivo
    up=driver.find_element(By.XPATH,"//input[@type='file']")
    up.send_keys(midia.replace("/", "\\"))

    #esperar a imagem ou arquivo ser adcionado
    while len(driver.find_elements(By.XPATH,'/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[1]')) < 1:
        sleep(0.0001)

#envia as mensagens
def envio(mensagem,midia,send,event,barra,button_start):
    i=0
    tam=len(contatos)
    print(contatos)
    for contato in contatos:
        button_start["text"] = "Cancelar"
        if event.is_set():
            break

        try:

            buscar_contato(contato)
            enviar_midia(midia) 
            enviar_mensagem(mensagem)
            print("contato: "+str(contato)+"\n")
            i+=1    
            if (i%100==0):
                button_start["text"] = "Descanso 60s"
                sleep(60)
                button_start["text"] = "Cancelar"
            progress = (i/tam)*100
            barra.set(progress)
            send.update()
        except:
            print("\nerro: "+contato)
            button_start["text"] = "Erro"
    button_start["text"] = "Fechar"
    barra.set(100)
    send.update()

#filtar dos contatos os que devem ser enviados
def getContato(Filtro):
    #leitura e filtragem
    salvo = pd.read_csv("./Contatos.csv")
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

def enviar(mensagem,midia,save):

    def start ():
        envioMensagem.start()

        button_start.config (text = 'Cancelar')
        button_start.config (command = cancelar)

    def cancelar():
        event.set()
        resultado = 'Cancelar'
        close()
    
    def close():
        send.destroy()

    resultado = 'Enviado'

    send = Tk() 


    lbl = Label(send)   
    lbl["text"] = save
    lbl.pack()

    barra = DoubleVar(send,value=0)

    minha_barra = ttk.Progressbar(send, variable=barra, maximum=100)
    minha_barra.pack()

    button_start = Button(send)  
    button_start["text"] = "Confirmar" 
    button_start["command"] = start
    button_start.pack()

    event = threading.Event()
    envioMensagem = threading.Thread(target=envio, args=(mensagem,midia,send,event,barra,button_start), name='envioMensagem')
    

    send.mainloop() 
    return resultado

#interface gráfica
# interface()
def interface():
#verificar e solicitar o arquivo a ser enviado
    posGrupos = []
    mensagem = ''
    midia = ''

    def dadosMensagem():
        men = inputMensagem.get(1.0, "end-1c")
        if men == "":
            lbl.config (text = "Não tem TEXTO para evio das mensagens")
        else:
            mensagem = str(men)
            save = mensagem
            mensagem = mensagem.replace('\n', ' ¨ | ¨ ')
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
                    # mensagem = mensagem.split("¨")
                    mensagem = str(men)

                    status = enviar(mensagem,midia,save)
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





    button_explore = Button(root)  
    button_explore["text"] = "Padrao de Grupos" 
    button_explore["command"] = procuraArquivo
    button_explore.pack()

    root.iconphoto(False, PhotoImage(file='./icon.png'))
    # root.iconphoto(False, PhotoImage(file='./icon.jpeg'))
    root.mainloop()

# Abre o Firefox
# driver = webdriver.Firefox()#webdriver.Chrome('./chromedriver.exe')
# driver.get("https://web.whatsapp.com") #abre o site Whatsapp Web

#https://stackoverflow.com/questions/50792181/how-to-save-the-session-of-whatsapp-web-with-selenium-python
dir_path = os.getcwd()
profile = os.path.join(dir_path, "profile", "wpp")
options = webdriver.ChromeOptions()

#tira a tela
# options.add_argument("--headless")

options.add_argument(r"user-data-dir={}".format(profile))

driver = webdriver.Chrome(chrome_options=options)

driver.get("https://web.whatsapp.com")


try:
    while len(driver.find_elements(By.ID, 'side')) < 1:
        time.sleep(0.1)
    time.sleep(0.1) # só uma garantia

    print("OK")

    interface()

    driver.quit()
except:
    print("Close")

    driver.quit()   

# def saveContato():
#     #elemento que via scroll
#     iframe = driver.find_element(By.XPATH, '//*[@id="pane-side"]/div/div/div')
#     scroll_origin = ScrollOrigin.from_element(iframe)
    
#     #altura andada
#     altura = 700

#     sleep(1)

#     Contato = []
#     temporario = []
#     anterior = []

#     while(True):

#         sleep(0.1)

#         # Pega os contatos
#         for person in driver.find_elements(By.XPATH,'//*[@id="pane-side"]/div/div/div/div'):
#             nomeContato = person.find_element(By.XPATH, './div/div/div/div[2]/div[1]/div').text
#             Contato.append(nomeContato)
#             temporario.append(nomeContato)
        
#         # Anda para baixo
#         ActionChains(driver)\
#             .scroll_from_origin(scroll_origin, 0, altura)\
#             .perform()
        
#         if(anterior == temporario):
#             break

#         anterior=temporario.copy()
#         temporario.clear()

#     #filtra contatos repetidos
#     semRepetir = list(set(Contato))

#     #salva os contatos
#     salvar = pd.DataFrame(semRepetir)
#     salvar = salvar.rename(columns = {0:'Contatos'})
#     salvar.to_csv("Contatos.csv")

# saveContato()