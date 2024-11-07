#Pildoras informáticas - Python tutorizado. Crawlers II. Vídeo 50
#Crawlers III. Vídeo 51
import requests

miReq = requests.get("https://www.pildorasinformaticas.es")

print(miReq.status_code)
print(miReq.headers)
#print(miReq.text)

from bs4 import BeautifulSoup

miDoc =requests.get("https://www.python.beispiel.programmierenlernen.io/")

docFinal = BeautifulSoup(miDoc.text, "html.parser")

iconos = docFinal.select(".emoji")
print(iconos[0].text)



