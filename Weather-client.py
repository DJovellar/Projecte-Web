#!/usr/bin/python

from urllib.request import urlopen
import bs4
import json
import pprint


class Clientweb(object):
    """Clientweb per for openweathermap"""

    def __init__(self):
        super(Clientweb, self).__init__()

    #Modificar url por la de la api de la web openweathermap
    def do_request(self):
        #https://api.openweathermap.org/data/2.5/find?q=Lleida&units=metric&appid=7de50c11e01dc42f66131cb4c8c0dc10
        ##https://api.openweathermap.org/data/2.5/find?q=Lleida&units=metric&appid=2a5b07d9b473350f8b06a8f47273d903&mode=json&lang=ca
        f = urlopen("https://api.openweathermap.org/data/2.5/find?q=Lleida&units=metric&appid=2a5b07d9b473350f8b06a8f47273d903&mode=json&lang=ca")
        data = f.read()
        f.close()
        return data

    #def process_weather(self, html):
    #    arbre = bs4.BeautifulSoup(html, features="lxml")
    #    temperature = arbre.find("temperature")
    #    weather = arbre.find("weather")
    #    print(temperature["value"] + "and" + weather["value"])

    #    return None

    #Usar esta si es posible!
    def process_weather(self, html):
        dic = json.loads(html)
        pprint.pprint(dic)
        temp = dic['list'][0]['main']['temp']
        weath = dic['list'][0]['weather'][0]['description']
        return (temp + " and " + weath)

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
