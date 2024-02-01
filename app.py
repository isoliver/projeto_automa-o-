import pyautogui
from time import sleep 
import re

# -passos manuais para realizar esste processo 
# 1 - clicar e digitar o usuario 

pyautogui.click(962,539, duration=0)
pyautogui.write('irlan')

# 2 - clicar e digitar minha senha 

pyautogui.click(967,572, duration=0)
pyautogui.write('123456')

# 3 - clicar em entrar 

pyautogui.click(851,608,duration=0)

# 4 - extrair cada produlto

with open('produtos.txt', 'r') as file:
    linhas = file.readlines()

# Aplique a regex para cada linha e atribua os valores a variáveis
for linha in linhas:
    padrao = r'\b(?:Produto \d|[\d.]+)\b'
    itens = re.findall(padrao, linha)

    # Atribua cada item a uma variável
    produto_nome = itens[0] if itens else None  # Assumindo que o primeiro item é o nome do produto
    quantidade = (itens[1]) if len(itens) > 1 else None
    preco = (itens[2]) if len(itens) > 2 else None

    # 	1- clicar e digitar produto
    pyautogui.click(687,523,duration=0)
    pyautogui.write(produto_nome)

    # 	2 - clicar e digitar quantidade 
    pyautogui.click(687,560,duration=0)
    pyautogui.write(quantidade)

    # 	3 - clicar e digitar preço
    pyautogui.click(694,588,duration=0)
    pyautogui.write(preco)

    # 	4 - clicar em registrar
    pyautogui.click(508,787,duration=0)
    sleep(1)
