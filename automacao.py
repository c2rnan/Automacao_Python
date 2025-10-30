import pyautogui 
import time

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("microsft edge")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=245, y=353)
pyautogui.write("caiozin.r1227@gmail.com")
pyautogui.click(x=248, y=441)
pyautogui.write("Caio123")
pyautogui.click(x=478, y=489, clicks=2)

time.sleep(3)

import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index: 
    pyautogui.click(x=252, y=249)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab") 
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab") 
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab") 
    categoria = str(tabela.loc[linha, "categoria"]) 
    pyautogui.write(categoria)

    pyautogui.press("tab") 
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab") 
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab") 
    obs = str(tabela.loc[linha, "obs"])
        
    if obs != "nan":  
        pyautogui.write(obs)

    pyautogui.press("tab") 
    pyautogui.press("enter")

    pyautogui.scroll(10000)

# Passo 5: Repetir para todos os produtos

