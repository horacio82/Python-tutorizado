#Python tutorizado. Crawlers II. Vídeo 50
#vemos cómo extraer información de una página web desde Python


import requests
from bs4 import BeautifulSoup


#miReq=requests.get("https://www.movistar.es/")
#print(miReq.status_code)
#print(miReq.headers)
#print(miReq.text)

miDoc="""

    <html>
        <body>
            <p>Hola, soy un párrafo</p>
            <p>Hola, soy otro párrafo</p>
            <a>Hola, soy un enlace</a>
        </body>
    </html>


"""

docFinal=BeautifulSoup(miDoc,"html.parser")

for parrafos in docFinal.find_all("p"):
    print(parrafos.text)

print(docFinal.find_all("p")) 