
import requests
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
headers = {'User-Agent': user_agent}    

url = 'https://www.tecmundo.com.br/voxel/500885-ps2-relembre-25-otimos-jogos-para-celebrar-os-25-anos-do-playstation-2.htm'

page = requests.get(url=url, headers=headers)
# Verificando o status da requisição
print("Status da Requisição:", page.status_code)

html = page.text

# Criando o objeto BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Encontrando todos os títulos dos jogos
titulo_jogos = soup.find_all('h2')



# Salvando o texto em um arquivo .txt
with open('resultado.txt', 'w', encoding='utf-8') as file:
    file.write('---------Melhores Jogos de PlayStation 2 🎮:-------\n\n')
    for titulo in titulo_jogos:
        print(titulo.text)
        # Escrevendo cada título no arquivo
        file.write(titulo.text + '\n')