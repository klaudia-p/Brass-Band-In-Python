from data_wystepu import Data_występu
from grupa_muzyków import Grupa_muzyków


class Występ:
    """Klasa przechowująca dane występu.
    Podaj rodzaj wydarzenia, cenę oraz czas wystepu w formie napisu 'dzień;godzina rozpoczęcia;godzina zakończenia'
    np. 'poniedziałek;12:30;15:00' """

    def __init__(self, wydarzenie, cena, czas_występu):
        self.wydarzenie = wydarzenie
        self.cena = int(cena)
        self.data = Data_występu(czas_występu)
        self.grupa_muzyków = Grupa_muzyków([])


    def potrzebne_instrumenty(self):
        """Funkcja zwracająca listę instrumentów wymaganych na dane wydarzenie"""

        try:
            słownik_wydarzeń = {"koncert": ["flet", "oboj", "klarnet", "fagot", "saksofon", "saksofon", "waltornia",
                               "trabka", "trabka", "trabka", "puzon", "puzon", "tuba", "sakshorn", "perkusja", "kotly",
                               "beben", "talerze", "ksylofon"],
                                "slub": ["skrzypce", "altowka", "wiolonczela", "kontrabas"],
                                "wesele": ["trabka", "puzon", "saksofon", "beben", "sakshorn"],
                                "rocznica": ["trabka", "puzon", "saksofon", "beben", "sakshorn"],
                                "pogrzeb": ["trabka"],
                                "uroczystosc panstwowa": ["trabka","perkusja"],
                                "parada": ["flet", "oboj", "klarnet", "saksofon", "waltornia",
                               "trabka", "trabka", "puzon", "puzon", "tuba", "sakshorn", "perkusja",
                               "beben", "talerze"]}

            return słownik_wydarzeń[self.wydarzenie]

        except KeyError:
            return "Przepraszamy, orkiestra nie występuje na takim wydarzeniu."


    def utwórz_grupe(self, lista_muzyków):
        """Funkcja tworząca obiekt klasy Grupa_muzyków"""

        self.grupa_muzyków = Grupa_muzyków(lista_muzyków)


    def __eq__(self, other):

        return self.data == other.data


    def __lt__(self, other):

        if self.data.dzien == other.data.dzien:
            if self.data.rozpoczecie < other.data.rozpoczecie:
                return True
            return False

        słownik_dni = {"poniedzialek": 1, "wtorek": 2, "sroda": 3, "czwartek": 4, "piatek": 5, "sobota": 6, "niedziela": 7}
        return słownik_dni[self.data.dzien] < słownik_dni[other.data.dzien]


    def __str__(self):
        return "\n".join(["Wydarzenie: {0}".format(self.wydarzenie),
                          "Data: {0}, {1} - {2}".format(self.data.dzien, self.data.rozpoczecie, self.data.zakonczenie),
                          "Koszt: {0} zł.".format(self.cena)])



#a = Występ("ślub", 400, "sobota;12:30;14:00")
#b = Występ("ślub", 400, "piatek;12:30;14:00")
#c = Występ("ślub", 400, "sobota;10:00;11:00")
#d = Występ("ślub", 400, "sobota;12:30;14:00")
#print(a)
#print(a.potrzebne_instrumenty())
#a.utwórz_grupe(["Klaudia", "Kasia"])
#print(a.grupa_muzyków)
#print(sorted([a,b,c]))