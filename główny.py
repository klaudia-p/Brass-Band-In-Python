from muzyk import Muzyk
from występ import Występ
from zajęcia import Zajęcia


class Główny:
    """Klasa głowna, w której odbywa się większość operacji."""

    def __init__(self):
        self.lista_występów = []
        self.słownik_muzyków = {}


    def nowa_osoba(self, imie_nazwisko, wiek, instrument):
        """Funkcja dodająca nowego muzyka do słownika muzyków"""

        osoba = Muzyk(imie_nazwisko, wiek, instrument)
        if str(osoba.instrument) in self.słownik_muzyków:
            self.słownik_muzyków[str(osoba.instrument)] += [osoba]
        else:
            self.słownik_muzyków[str(osoba.instrument)] = [osoba]


    def nowy_występ(self, wydarzenie, cena, czas_występu):
        """Fukncja dodająca nowy występ do listy występów"""

        występ = Występ(wydarzenie, cena, czas_występu)
        self.lista_występów += [występ]


    def liczba_muzyków(self):
        """Funkcja zliczającą wszystkich muzyków w orkiestrze"""

        licznik = 0
        for i in self.słownik_muzyków:
            licznik += len(self.słownik_muzyków[i])

        return licznik


    def czy_zajęta(self, osoba, czas):
        """Funkcja sprawdzająca, czy dana osoba występuje już w tym czasie"""

        for i in self.lista_występów:
            if i.data == czas:
                if osoba in i.grupa_muzyków.lista_muzyków:
                    return True
        return False


    def wybierz_muzyków(self, występ):
        """Funkcja tworząca listę muzyków na konkretny występ. Przyjmuje obiekt typu Występ()"""

        instrumenty = występ.potrzebne_instrumenty()
        lista = []
        for i in instrumenty:
            if i in self.słownik_muzyków:
                ile_osób = len(self.słownik_muzyków[i])
                a = 0
                while ile_osób > 0:
                    if self.czy_zajęta(self.słownik_muzyków[i][a], występ.data):
                        a += 1
                        ile_osób -= 1
                    else:
                        lista += [self.słownik_muzyków[i][a]]
                        break

        if len(lista) == len(instrumenty):
            występ.utwórz_grupe(lista)


    def obstaw_występy(self):

        for i in self.lista_występów:
            self.wybierz_muzyków(i)


    def moje_terminy(self, osoba):
        """Funkcja zwracająca dwie listy: listę występów muzyka oraz jego zajęć"""

        self.obstaw_występy()
        moje_występy = []
        moje_zajęcia = []
        zajęcia = Zajęcia()
        osoba = self.szukaj_osoby(osoba)

        for i in self.lista_występów:
            if osoba in i.grupa_muzyków.lista_muzyków:
                moje_występy += [i]

        if zajęcia.sprawdź_termin_próby(self.lista_występów, self.liczba_muzyków(), osoba, zajęcia.próba_1):
            moje_zajęcia += [zajęcia.próba_1]

        if zajęcia.sprawdź_termin_próby(self.lista_występów, self.liczba_muzyków(), osoba, zajęcia.próba_2):
            moje_zajęcia += [zajęcia.próba_2]

        if not osoba.czy_pełnoletnia():
            if zajęcia.sprawdź_termin_lekcji(self.lista_występów):
                moje_zajęcia += [zajęcia.lekcja]

        return moje_występy, moje_zajęcia


    def szukaj_osoby(self, osoba):
        """Funkcja znajdująca obiekt typu Muzyk() dla podanego imienia i nazwiska"""

        for i in self.słownik_muzyków:
            for j in range(len(self.słownik_muzyków[i])):
                if osoba == self.słownik_muzyków[i][j].imie_nazwisko:
                    return self.słownik_muzyków[i][j]

        return "Przepraszamy, nie ma takiego muzyka w orkiestrze."


    def wczytaj_muzyków(self, plik):
        """Funkcja wczytująca listę muzyków z pliku"""

        with open(plik) as fm:
            muzycy = fm.readlines()
            for i in muzycy:
                argumenty = i.split(",")
                argumenty[2] = argumenty[2].strip("\n")
                self.nowa_osoba(*argumenty)


    def wczytaj_występy(self, plik):
        """Funkcja wczytująca występy z pliku"""

        with open(plik) as fm:
            występy = fm.readlines()
            for i in występy:
                argumenty = i.split(",")
                argumenty[2] = argumenty[2].strip("\n")
                self.nowy_występ(*argumenty)


    def generuj_grafik(self, osoba):

        try:
            moje_występy, moje_zajęcia = self.moje_terminy(osoba)
            mój_grafik = moje_występy + moje_zajęcia
            mój_grafik = sorted(mój_grafik)
            pomocnicza = ""

            print("***********************")
            print("TWÓJ TYGODNIOWY GRAFIK: ")
            print("")
            for i in mój_grafik:
                if pomocnicza != i.data.dzien:
                    pomocnicza = i.data.dzien
                    print(pomocnicza)
                print("{0} - {1}  {2}" .format(i.data.rozpoczecie, i.data.zakonczenie, i.wydarzenie))
            print("")
            return "Powodzenia! :D"

        except:
            return "Przepraszamy, nie ma takiego muzyka w orkiestrze."


    def bilans_pieniężny(self, osoba):

        try:
            moje_występy, moje_zajęcia = self.moje_terminy(osoba)
            bilans = 0
            for i in moje_występy:
                bilans += i.cena / i.grupa_muzyków.liczba_muzyków()
            for i in moje_zajęcia:
                bilans += i.cena

            print("")
            return "Twój bilans pieniężny wynosi: " + str(int(bilans)) + " zł."

        except:
            return "Przepraszamy, nie ma takiego muzyka w orkiestrze."



def menu():
    try:
        q = Główny()
        while True:
            print("***************************  MENU  ***************************")
            print("1 - dodaj muzyka                5 - pokaż osobę")
            print("2 - dodaj występ                6 - generuj grafik")
            print("3 - wczytaj muzyków z pliku     7 - bilans pieniężny")
            print("4 - wczytaj występy z pliku     8 - wyjście")

            a = int(input("Podaj numer: "))
            if a == 1:
                imie = input("Podaj imie i nazwisko: ")
                wiek = input("Podaj wiek: ")
                instrument = input("Podaj instrument: ")
                q.nowa_osoba(imie, wiek, instrument)
                print("Osoba została dodana!")

            if a == 2:
                wydarzenie = input("Jakie wydarzenie? ")
                cena = input("Podaj koszt: ")
                data = input("Podaj datę (dzień;godzina rozpoczęcia;godzina zakończenia np. sroda;10:00;11:30) ")
                q.nowy_występ(wydarzenie,cena,data)
                print("Wystep został dodany!")

            if a == 3:
                plik = input("Podaj śnieżkę do pliku: ")
                q.wczytaj_muzyków(plik)
                print("Wczytano plik")

            if a == 4:
                plik = input("Podaj śnieżkę do pliku: ")
                q.wczytaj_występy(plik)
                print("Wczytano plik")

            if a == 5:
                imie = input("Podaj imie i nazwisko: ")
                print(q.szukaj_osoby(imie))

            if a == 6:
                imie = input("Podaj imie i nazwisko: ")
                print(q.generuj_grafik(imie))

            if a == 7:
                imie = input("Podaj imie i nazwisko: ")
                print(q.bilans_pieniężny(imie))

            if a == 8:
                break
        return ""

    except:
        return "Błąd! Wpisz poprawne dane."



print(menu())
