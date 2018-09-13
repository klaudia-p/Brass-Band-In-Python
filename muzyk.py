from instrument import Instrument


class Muzyk():
    """Klasa przechowująca muzyków orkiestry dętej."""

    def __init__(self, imie_nazwisko, wiek, instrument):
        self.imie_nazwisko = imie_nazwisko
        self.wiek = int(wiek)
        self.instrument = Instrument(instrument)


    def __str__(self):
        return "\n".join(["Imię i nazwisko: {0}".format(self.imie_nazwisko),
                          "Wiek: {0} lat".format(self.wiek),
                          "Instrument: {0}".format(self.instrument)])


    def czy_pełnoletnia(self):
        """Funkcja sprawdzająca czy osoba ma ukończone 18 lat"""

        if self.wiek >= 18:
            return True
        else:
            return False
