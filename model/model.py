import networkx as nx
from pydantic_core.core_schema import none_schema

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.DiGraph()
        pass


    def getGenere(self):
        return DAO.getAllGeneri()

    def getVertici(self,genere):
        return DAO.getAllVertici(genere)

    def listaArtistaPop(self,genere):
        popolarita= DAO.getAllArtistiPop()
        artisti=DAO.getAllVertici(genere)
        filtro=[]
        for a in artisti:
            for p in popolarita:
                if a.ArtistId == p.ArtistId:
                    filtro.append(p)
        return filtro

    def buildGrafo(self,genere):
        self._grafo.clear()
        for v in self.getVertici(genere):
            self._grafo.add_node(v)
        lista=self.getVertici(genere)
        filtro=self.listaArtistaPop(genere)
        mappa_popolarita = {f.ArtistId: f.popolarita for f in filtro}
        for i in range(len(lista)):
            for j in range(i + 1, len(lista)):
                a1 = lista[i]
                a2 = lista[j]
                if len(DAO.getArco(a1, a2)) > 0:
                    pesoa1 = mappa_popolarita.get(a1.ArtistId, 0)
                    pesoa2 = mappa_popolarita.get(a2.ArtistId, 0)


                    if pesoa1 > pesoa2:
                        self._grafo.add_edge(a1, a2,weight=pesoa1+pesoa2)
                    elif pesoa2 > pesoa1:
                        self._grafo.add_edge(a2, a1,weight=pesoa2+pesoa1)
                    elif pesoa1 == pesoa2 and (pesoa1!=0 and pesoa2!=0):
                        self._grafo.add_edge(a1, a2,weight=pesoa1+pesoa2)
                        self._grafo.add_edge(a2, a1,weight=pesoa2+pesoa1)








    def getNumVertici(self):
        return len(self._grafo.nodes())

    def getNumArchi(self):
        return len(self._grafo.edges())








