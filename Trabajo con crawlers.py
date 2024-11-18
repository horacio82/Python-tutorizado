#Pildoras informáticas - Python tutorizado. Crawlers II. Vídeo 50
#Crawlers III. Vídeo 51 - #Python tutorizado. Crawlers IV. Vídeo 52
#Python tutorizado. Crawlers V. Vídeo 53 - #Python tutorizado. Crawlers VI. Vídeo 54 - #Python tutorizado. Crawlers VII. Vídeo 55
#Python tutorizado. Crawlers VIII. Vídeo 56


from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import time
import csv

class PostCrawled():
    def __init__(self, titulo, emoticono, contenido, imagen):
        self.titulo=titulo
        self.emoticono=emoticono
        self.contenido=contenido
        self.imagen=imagen

    
class PostExtractor():

    def extraeinfo(self):

        urlBase = "https://www.python.beispiel.programmierenlernen.io/"

        #posts=[]

        while urlBase!="":

            miDoc = requests.get(urlBase)

            docFinal = BeautifulSoup(miDoc.text, "html.parser")

            time.sleep(2)

            for card in docFinal.select(".card"):
                titulo=card.select(".card-title span")[1].text
                emoticono=card.select_one(".emoji").text
                contenido=card.select_one(".card-text").text
                imagen=urljoin(urlBase,card.select_one("img").attrs["src"])

                #crawled=PostCrawled(titulo,emoticono,contenido,imagen)
                #posts.append(crawled)

                yield PostCrawled(titulo,emoticono,contenido,imagen)

            boton_siguiente = docFinal.select_one(".navigation .btn")

            if boton_siguiente:
                rutas_absolutas = urljoin(urlBase, boton_siguiente.attrs["href"])
                urlBase = rutas_absolutas
                print(rutas_absolutas)

            else:
                urlBase = ""
            

        
        #return posts

unPost=PostExtractor()

listaPost=unPost.extraeinfo()
contador=0
for elPost in listaPost:

    if contador==12:
        break
    contador+=1

    print(elPost.emoticono)
    print(elPost.titulo)
    print(elPost.contenido)
    print(elPost.imagen)
    print()

#print(listaPost)

'''
with open('posts.csv', 'w', newline='', encoding="utf-8") as csvfile:
    postwriter = csv.writer(csvfile, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    for mipost in unPost.extraeinfo():
        postwriter.writerow([mipost.emiticono, mipost.titulo, mipost.contenido, mipost.imagen])
    
'''

    