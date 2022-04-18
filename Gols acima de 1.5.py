# -*- coding: cp1252 -*-
from os import close
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from time import sleep
import json 
import pandas as pd
import numpy as np

options = Options()
#options.add_argument('--headless')
options.add_argument('window-size=1358,700')

navegador = webdriver.Chrome(options=options)
navegador.get("https://dicasbet.com.br/palpites-de-amanha/")

page_content = navegador.page_source
site = BeautifulSoup(page_content, 'html.parser')

competicao = site.findAll('div', attrs={"class":"competition"})

competic = []
time = []
time_c = []
time_v = []
palpt = []
palpite_resultado_casa = []
palpite_resultado_empate = []
palpite_resultado_visitante = []
palpite_casa_intervalo = []
palpite_empate_intervalo = []
palpite_visitante_intervalo = []
palpite_over_1 = []
palpite_over_2 = []
palpite_over_3 = []
palpite_am = []
palpite_an = []

competicao = site.findAll('div', attrs={"class":"competition"})

contador= 0
nun_elementos = len(competicao)

while(contador < nun_elementos):

    competicao = site.findAll('div', attrs={"class":"competition"})[contador]

    try:
        nome =  competicao.findAll('div', attrs={"class":"name"})[0].text

        tempo =  competicao.findAll('div', attrs={"class":"time"})[0].text
       

        time_casa = competicao.findAll('div', attrs={"class":"hostteam"})[0].text
        time_casa = time_casa.strip()


        time_fora = competicao.findAll('div', attrs={"class":"guestteam"})[0].text
        time_fora = time_fora.strip()


        palpite = competicao.findAll('div', attrs={"class":"value"})[3].text
        value1 = competicao.findAll('div', attrs={"class":"value"})[4].text
        value2 = competicao.findAll('div', attrs={"class":"value"})[5].text
        value3 = competicao.findAll('div', attrs={"class":"value"})[6].text
        value4 = competicao.findAll('div', attrs={"class":"value"})[7].text
        value5 = competicao.findAll('div', attrs={"class":"value"})[8].text
        value6 = competicao.findAll('div', attrs={"class":"value"})[9].text
        value7 = competicao.findAll('div', attrs={"class":"value"})[10].text
        value8 = competicao.findAll('div', attrs={"class":"value"})[11].text
        value9 = competicao.findAll('div', attrs={"class":"value"})[12].text
        value10 = competicao.findAll('div', attrs={"class":"value"})[13].text
        value11 = competicao.findAll('div', attrs={"class":"value"})[14].text

        competic.append(nome)
        time.append(tempo)
        time_c.append(time_casa)
        time_v.append(time_fora)
        palpt.append(palpite)
        palpite_resultado_casa.append(value1)
    
        palpite_resultado_empate.append(value2)
        palpite_resultado_visitante.append(value3)
        palpite_casa_intervalo.append(value4)
        palpite_empate_intervalo.append(value5)
        palpite_visitante_intervalo.append(value6)
        palpite_over_1.append(value7)
        palpite_over_2.append(value8)
        palpite_over_3.append(value9)
        palpite_am.append(value10)
        palpite_an.append(value11)
   
    except:
        print('nao existe')

    print(f'----------extracao da competicao {contador+1} com sucesso---------------')

    contador+=1

# transforma em dataframe
df = pd.DataFrame(list(zip(competic,time,time_c,time_v,palpt,palpite_resultado_casa,palpite_resultado_empate, palpite_resultado_visitante,palpite_casa_intervalo,palpite_empate_intervalo,palpite_visitante_intervalo,palpite_over_1, palpite_over_2, palpite_over_3,palpite_am,palpite_an)), columns = ['competicao', 'tempo', 'casa','visitante', 'palpite','1', 'x', '2', 'ht1', 'htx', 'ht2', '1.5', '2.5', '3.5', 'am', 'an', ])

# transforma em dicionario
jogosamanha = {}
jogosamanha['partidas'] = df.to_dict('records')

# transforma em arquivo JSON
js = json.dumps(jogosamanha)
fp = open('jogosamanha.json', 'w')
fp.write(js)
fp.close()

print('--------------Proceso finalizado-----------------------')

sleep(60)
