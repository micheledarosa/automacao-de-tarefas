from pyautogui import PAUSE, press, write, click, scroll
from time import sleep
import pandas
import unicodedata

PAUSE = 1

#Passo 1 - Entrar no sistema da empresa
# abrindo o navegador
press("win")
write("opera")
press("enter")

sleep(2)

# acessando o site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
write(link)
press("enter")

sleep(5)

# Passo 2 - Acessar a conta da empresa
click(x=770, y=388)
write("email123@teste.com")
press("tab")
write("senha123")
press("tab")
press("enter")

# Passo 3 - Importar o banco de dados
tabela = pandas.read_csv("produtos.csv")

sleep(1)

# Passo 4 - Cadastrar os produtos
for linha in tabela.index:
   click(x=747, y=273)
   sleep(1)
   write(str(tabela.loc[linha, "codigo"]))
   press("tab")
   write(tabela.loc[linha, "marca"])
   press("tab")
   write(tabela.loc[linha, "tipo"])
   press("tab")
   write(str(tabela.loc[linha, "categoria"]))
   press("tab")
   write(str(tabela.loc[linha, "preco_unitario"]))
   press("tab")
   write(str(tabela.loc[linha, "custo"]))
   press("tab")
   obs = tabela.loc[linha, "obs"]
   if not pandas.isna(obs):
      write(obs)
   press("tab")
   press("enter")
   scroll(1000)