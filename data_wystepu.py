class Data_występu():
    """" Klasa przechowująca datę występu. """

    def __init__(self, data):
        lista = data.split(";")
        self.dzien = lista[0]
        self.rozpoczecie = lista[1]
        self.zakonczenie = lista[2]

    def __eq__(self, other):
        """Funkcja sprawdzająca czy występy odbywają się w tym samym czasie"""

        if self.dzien == other.dzien:
            minuty_1 = self.minuty()
            minuty_2 = other.minuty()
            minuty_1[0], minuty_2[0] = minuty_1[0] - 30, minuty_2[0] - 30  #Doliczamy 30 minut na dojazd

            if minuty_1[0] < minuty_2[0]:
                if minuty_1[1] > minuty_2[0]:
                    return True
            else:
                if minuty_1[0] < minuty_2[1]:
                    return True

        return False


    def minuty(self):
        """Funkcja konwertująca godziny na minuty"""

        a, b = self.rozpoczecie.split(":"), self.zakonczenie.split(":")
        rozpoczęcie = int(a[0]) * 60 + int(a[1])
        zakończenie = int(b[0]) * 60 + int(b[1])

        return [rozpoczęcie, zakończenie]


    def __str__(self):
        return "Dzień tygodnia: {0}, w godzinach: {1} - {2}" .format(self.dzien, self.rozpoczecie, self.zakonczenie)