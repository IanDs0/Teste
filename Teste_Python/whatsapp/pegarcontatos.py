from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

from time import sleep
import sys
import pandas as pd

import os
from selenium import webdriver

dir_path = os.getcwd()
profile = os.path.join(dir_path, "profile", "wpp")
options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir={}".format(profile))

driver = webdriver.Chrome(chrome_options=options)

driver.get("https://web.whatsapp.com")

while len(driver.find_elements(By.ID, 'side')) < 1:
    sleep(2)
sleep(2)

iframe = driver.find_element(By.XPATH, '//*[@id="pane-side"]/div/div/div')
altura = 700
scroll_origin = ScrollOrigin.from_element(iframe)

sleep(1)

Contato = []
temporario = []
anterior = []

while(True):

    sleep(0.1)

    # Pega os contatos
    for person in driver.find_elements(By.XPATH,'//*[@id="pane-side"]/div/div/div/div'):
        nomeContato = person.find_element(By.XPATH, './div/div/div/div[2]/div[1]/div').text
        Contato.append(nomeContato)
        temporario.append(nomeContato)
    
    # Anda para baixo
    ActionChains(driver)\
        .scroll_from_origin(scroll_origin, 0, altura)\
        .perform()
    
    if(anterior == temporario):
        break

    anterior=temporario.copy()
    temporario.clear()

teste = list(set(Contato))

#salva
salvar = pd.DataFrame(teste)
salvar = salvar.rename(columns = {0:'Contatos'})
salvar.to_csv("csv/Contatos.csv", index=False)

driver.quit()