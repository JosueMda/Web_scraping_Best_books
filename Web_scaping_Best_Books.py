import bs4
import requests

# ITERAR EN MULTIPLES PAGINAS DE UNA PAGINA USANDO EL FORMAT

#CREAR URL SIN NUMERO DE PAGINA
url_base = "http://books.toscrape.com/catalogue/page-{}.html"

# LISTA DE TITULO CON 4 O 5 ESTRELLAS
titulos_rating_alto = []

#ITERAR PAGINA
for pagina in range(1,50):
    #CREAR SOPA EN CADA PAGINA
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, "lxml")
    
    # SELECCIONAR DATO DE LOS LIBROS 
    libros = sopa.select(".product_pod")
    
    #ITERAR LIBROS
    for libro in libros:
        #CHEQUEAR QUE TENGAN 4 O 5 ESTRELLAS
        if len(libro.select(".star-rating.Four")) != 0 or len(libro.select(".star-rating.Five")):
            #GUARDAR TITULO EN UNA VARIABLE
            titulo_libro = libro.select("a")[1]["title"]
            
            #AGREGAR LIBRO A LA LISTA
            titulos_rating_alto.append(titulo_libro)
            
# VER LIBROS 4 o 5 ESTRELLAS EN CONSOLA
for t in titulos_rating_alto:
    print(t)