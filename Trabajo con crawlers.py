#Python tutorizado. Crawlers II, III, IV, V, VI, VII, VIII - Vídeo 50, 51, 52, 53, 54, 55, 56
#vemos cómo extraer información de una página web desde Python


import requests
from bs4 import BeautifulSoup
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


    def extraer(self):

        urlBase="http://python.beispiel.programmierenlernen.io/index.php"

        posts=[]


        while urlBase!="":

            miDoc=requests.get(urlBase)

            docFinal=BeautifulSoup(miDoc.text,"html.parser")

            time.sleep(2)

            for card in docFinal.select(".card"):
                titulo=card.select(".card-title span")[1].text
                emoticono=card.select_one(".emoji").text
                contenido=card.select_one(".card-text").text
                imagen=urljoin(urlBase, card.select_one("img").attrs["src"])

                crawled=PostCrawled(titulo, emoticono, contenido, imagen)
                posts.append(crawled)

            boton_siguiente=docFinal.select_one(".navigation .btn")

            if boton_siguiente:
                rutas_absolutas=urljoin(urlBase, boton_siguiente.attrs["href"])
                urlBase=rutas_absolutas
                print(rutas_absolutas)    
            else:
                urlBase=""
          

        return posts
    
unPost=PostExtractor()

listaPosts=unPost.extraer()

for post in listaPosts:
    print(post.emoticono)
    print(post.titulo)
    print(post.contenido)
    print(post.imagen)
    print()

#print(listaPosts)

with open('post.csv', 'w',newline='', encoding='utf-8') as csvfile:
    postwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    for mipost in unPost.extraer():
        postwriter.writerow([mipost.titulo, mipost.emoticono, mipost.contenido, mipost.imagen])    
    