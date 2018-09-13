class Grupa_muzyków():
    """Klasa przechowująca listę muzyków dla konkretnego występu."""

    def __init__(self, lista_muzyków):

        self.lista_muzyków = lista_muzyków


    def __str__(self):

        return self.lista_muzyków


    def liczba_muzyków(self):

        return len(self.lista_muzyków)

