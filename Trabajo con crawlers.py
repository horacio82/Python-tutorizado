#Python tutorizado. Crawlers II, III, IV, V, VI - Vídeo 50, 51, 52, 53, 54
#vemos cómo extraer información de una página web desde Python


import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class PostCrawled():

    def __init__(self, titulo, emoticono, contenido, imagen):

        self.titulo=titulo
        self.emoticono=emoticono
        self.contenido=contenido
        self.imagen=imagen
        
class PostExtractor():


    def extraer(self):

        urlBase="https://www.youtube.com/watch?v=X4d4barv1fA"
        miDoc=requests.get(urlBase)

        docFinal=BeautifulSoup(miDoc.text,"html.parser")

        posts=[]

        for card in docFinal.select(".card"):
            titulo=card.select(".card-title span")[1].text
            emoticono=card.select_one(".emoji").text
            contenido=card.select_one(".card-text").text
            imagen=urljoin(urlBase, card.select_one("img").attrs["src"])

            crawled=PostCrawled(titulo, emoticono, contenido, imagen)
            posts.append(crawled)
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