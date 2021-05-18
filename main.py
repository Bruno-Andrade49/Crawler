import re
import requests
from bs4 import BeautifulSoup

semente = 'https://www.diferenca.com/hardware-e-software/'
sites = [[semente],[],[]]
conteudo = {}
prof_limite = 2
prof_atual = 0

while prof_atual <= prof_limite :

    for site in sites [prof_atual] :
        try:
            site1 = str(site)
            link = requests.get(site1)
            soup = BeautifulSoup(link.content, 'html.parser')

        except:
            print('O arquivo em formato url não funciona!')

        links_site = soup.findAll('a', attrs={'href': re.compile("^http")})
        lista = []
        for link in links_site:
            lista.append(link.get('href'))
        texto = list(soup.text.upper().split())

        conteudo[site1]= set(texto)
        if len(sites) < prof_atual + 2 :
            sites.append ( [ ] )

        sites[prof_atual+1].extend(lista)

    print(lista)
    prof_atual += 1




