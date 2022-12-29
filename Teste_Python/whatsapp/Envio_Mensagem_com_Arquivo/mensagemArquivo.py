from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from time import sleep
import threading

from tkinter import *
from tkinter import ttk

import sys
sys.path.append('./Busca_Arquivo_Mensagem')

from buscaeEnvio import *

#envia as mensagens
def sendMensagem(mensagem,midia,send,event,barra,button_start, driver,contatos):
    i=0
    tam=len(contatos)
    print(contatos)
    for contato in contatos:
        button_start["text"] = "Cancelar"
        if event.is_set():
            break

        try:
            buscar_contato(contato, driver)
            enviar_midia(midia, driver) 
            enviar_mensagem(mensagem, driver)

            #envia a mendagem
            ActionChains(driver)\
                    .pause(0.3)\
                    .send_keys(Keys.ENTER)\
                    .perform()

            print("Enviado -> contato: "+str(contato)+"\n")
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



def enviar(mensagem,midia,driver,contatos):

    def start ():
        envioMensagem.start()

        button_start.config (text = 'Cancelar')
        button_start.config (command = cancelar)

    def cancelar():
        event.set()
        close()
    
    def close():
        send.destroy()

    send = Toplevel()
    send.title('Envio')


    lbl = Label(send)   
    lbl["text"] = mensagem
    lbl.pack()

    barra = DoubleVar(send,value=0)

    minha_barra = ttk.Progressbar(send, variable=barra, maximum=100)
    minha_barra.pack()

    button_start = Button(send)  
    button_start["text"] = "Confirmar" 
    button_start["command"] = start
    button_start.pack()

    event = threading.Event()
    envioMensagem = threading.Thread(target=sendMensagem, args=(mensagem,midia,send,event,barra,button_start,driver,contatos), name='envioMensagem')
    

    send.mainloop() 
    # return resultado