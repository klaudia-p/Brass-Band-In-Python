from występ import Występ

class Zajęcia():
    """Klasa zawierająca informacje na temat zajęć orkiestry.

     Próby orkietry odbywają sie dwa razy w tygodniu (wtorek oraz czwartek, godz 18:00 - 20.00). Próba odbywa się
     jeśli 80% muzyków jest dostępna. Muszą wziąć w niej udział wszyscy wolni muzycy.

     W zajęciach indywidualnych (lekcjach) mają obowiązek uczestniczyć muzycy poniżej 18 roku życia, aby szkolić swój warsztat muzyczny.
     Odbywają się w środę w godz 10:00 - 11:00, jeśli muzyk jest dostępny w tym czasie. Koszt jednej lekcji to 50 zł."""

    def __init__(self):

        self.próba_1 = Występ("próba",0,"wtorek;18:00;20:00")
        self.próba_2 = Występ("próba",0,"czwartek;18:00;20:00")
        self.lekcja = Występ("lekcja",-50,"sroda;10:00;11:00")


    def sprawdź_termin_próby(self, lista_występów, liczba_osób, osoba, próba):
        """Funkcja decydująca czy próba się odbywa oraz czy osoba bierze w niej udział"""

        for i in lista_występów:
            if i.data == próba.data:
                if osoba in i.grupa_muzyków.lista_muzyków:
                    return False
                else:
                    procent = liczba_osób * 0.8
                    if len(i.grupa_muzyków.lista_muzyków) > procent:
                        return False
        return True



    def sprawdź_termin_lekcji(self, lista_występów):
        """Funkcja decydująca czy lekcja się odbywa"""

        for i in lista_występów:
            if i.data == self.lekcja.data:
                return False
        return True