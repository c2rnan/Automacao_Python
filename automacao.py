import pyautogui # pyright: ignore[reportMissingModuleSource]
import time

pyautogui.PAUSE = 0.5

# Passo 1: Entrar no sistema - https://dlp.hashtagtreinamentos.com/p...
#abrir o google
pyautogui.press("win")
pyautogui.write("microsft edge")
pyautogui.press("enter")

#digitar o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#espera 3 segundos
time.sleep(3)

# Passo 2: Fazer login
pyautogui.click(x=245, y=353)
pyautogui.write("caiozin.r1227@gmail.com")
pyautogui.click(x=248, y=441)
pyautogui.write("Caio123")
pyautogui.click(x=478, y=489, clicks=2)

# espera de 3s
time.sleep(3)

# Passo 3: Importa a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4: Cadastra 1 produto
for linha in tabela.index: # para cada linha da minha tabela
    pyautogui.click(x=252, y=249)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab") # passar para o proximo campo
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab") # passar para o proximo campo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab") # passar para o proximo campo
    categoria = str(tabela.loc[linha, "categoria"]) # String = texto -> str()
    pyautogui.write(categoria)

    pyautogui.press("tab") # passar para o proximo campo
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab") # passar para o proximo campo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab") # passar para o proximo campo
    obs = str(tabela.loc[linha, "obs"])
        
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab") # passou para o botao enviar
    pyautogui.press("enter")

    pyautogui.scroll(10000)

# Passo 5: Repetir para todos os produtos

