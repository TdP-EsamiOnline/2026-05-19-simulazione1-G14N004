import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDGenre(self):
        generi = self._model.getGenere()
        for g in generi:
            self._view._ddGenre.options.append(ft.dropdown.Option(key=g.GenreId, text=g.Name))
        self._view.update_page()

    def handleCreaGrafo(self, e):
       # genere = self._view._ddGenre.value
       # self._view.txt_result.controls.append(ft.Text(f"il genere è {genere}"))
       # self._view.update_page()
       genere = None
       try:
           genere = int(self._view._ddGenre.value)
           self._model.buildGrafo(genere)
           self._view.txt_result.controls.append(ft.Text(f"Grafo creato correttamnete , ha {self._model.getNumVertici()} nodi e {self._model.getNumArchi()}"))
           archi = list(self._model._grafo.edges(data=True))
           archi.sort(key=lambda x: x[2].get('weight', 0))
           best5=archi[:5]
           for elm in best5:
               self._view.txt_result.controls.append(ft.Text(elm))

           self._view.update_page()

       except ValueError:
           self._view._txt_result.controls.append(ft.Text("seleziona un genere"))






    def handleCammino(self,e):
        pass