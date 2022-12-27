from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from time import sleep
import numpy as np
import pyperclip

#Funcao que envia midia como mensagem
def enviar_midia(midia, driver):
    
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

#Funcao que pesquisa o Contato/Grupo
def buscar_contato(contato, driver):
    encontro = True
    
    while encontro:
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
            else:
                break
        
        driver.find_element(By.XPATH,'//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]').send_keys(Keys.ENTER)
        
        if(driver.find_element(By.XPATH,'//*[@id="main"]/header/div[2]/div[1]/div/span').text == contato):
            encontro = False

#Funcao que envia a mensagem
def enviar_mensagem(mensagem, driver):
    
    while driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]').text == '':
        
        pyperclip.copy(mensagem);
        ActionChains(driver)\
            .key_down(Keys.CONTROL)\
            .send_keys('v')\
            .key_up(Keys.CONTROL)\
            .perform()
