#!/usr/bin/python

from urllib.request import urlopen
import bs4


class Clientweb(object):
    """Clientweb per for openweathermap"""

    def __init__(self):
        super(Clientweb, self).__init__()

    #Modificar url por la de la api de la web openweathermap
    def do_request(self):
        #https://api.openweathermap.org/data...
        f = urlopen("http://www.eps.udl.cat/ca/")
        data = file.read()
        f.close()
        return data

    def process_weather(self, html):
        arbre = bs4.BeautifulSoup(html, features="lxml")
        temperature = arbre.find("temperature")
        weather = arbre.find("weather")
        print(temperature["value"] + "and" + weather["value"])

        return None

    def run(self):
        # descargar pagina web en html
        data = self.do_request()

        # buscar activitats
        data  = self.process_weather(data)

        # imprimir resultat
        # print(activitats)


if __name__ == "__main__":
    c = Clientweb()
    c.run()
