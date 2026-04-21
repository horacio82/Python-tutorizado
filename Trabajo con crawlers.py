#Python tutorizado. Crawlers II, III, IV, V - Vídeo 50, 51, 52, 53, 
#vemos cómo extraer información de una página web desde Python


import requests
from bs4 import BeautifulSoup

class PostCrawled():

    def __init__(self, titulo, emoticono, contenido, imagen):

        self.titulo=titulo
        self.emoticono=emoticono
        self.contenido=contenido
        self.imagen=imagen
        
class PostExtractor():


    def extraer(self):

        miDoc=requests.get("https://www.youtube.com/watch?v=X4d4barv1fA")

        docFinal=BeautifulSoup(miDoc.text,"html.parser")

        posts=[]

        for card in docFinal.select(".card"):
            titulo=card.select(".card-title span")[1].text
            emoticono=card.select_one(".emoji").text
            contenido=card.select_one(".card-text").text
            imagen=card.select_one("img").attrs["src"]

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