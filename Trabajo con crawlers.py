#Python tutorizado. Crawlers II. Vídeo 50
#vemos cómo extraer información de una página web desde Python


import requests
from bs4 import BeautifulSoup


miDoc=requests.get("https://www.youtube.com/watch?v=X4d4barv1fA")

docFinal=BeautifulSoup(miDoc.text,"html.parser")

docFinal.select(".emoji")

print(docFinal.select(".emoji"))

