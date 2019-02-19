#!/usr/bin/python

from urllib.request import urlopen
import bs4


class Clientweb(object):
    """Clientweb per la web de la EPS"""

    def __init__(self):
        super(Clientweb, self).__init__()

    def descargar_html(self):
        file = urlopen("http://www.eps.udl.cat/ca/")
        html = file.read()
        file.close()
        return html

    def buscar_activitats(self, html):
        arbre = bs4.BeautifulSoup(html, features="lxml")
        activitats = arbre.find_all("div", "featured-links-item")
        activity_list = []
        for activity in activitats:
            title = activity.find("span", "flink-title")
            link = activity.find("a")
            activity_list.append((title.text, link["href"]))
            print(title.text)

        return activity_list

    def run(self):
        # descargar pagina web en html
        html = self.descargar_html()

        # buscar activitats
        activitats  = self.buscar_activitats(html)

        # imprimir resultat
        # print(activitats)


if __name__ == "__main__":
    c = Clientweb()
    c.run()
