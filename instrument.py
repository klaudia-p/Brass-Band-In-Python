class Instrument():
    """Klasa przechowująca obiekty będące instrumentami muzyków."""

    def __init__(self, nazwa):
        if nazwa == "rog":    # waltornia i róg to ten sam instrument
            self.nazwa = "waltornia"
        else:
            self.nazwa = nazwa


    def __str__(self):
        return self.nazwa


    def rodzaj(self):
        """Funkcja sprawdzająca jakiego rodzaju jest instrument."""

        if self.nazwa in ["flet", "oboj", "klarnet", "rozek angielski", "fagot", "saksofon"]:
            return "Instrument dęty drewniany"
        if self.nazwa in ["waltornia", "trabka", "puzon", "tuba", "sakshorn"]:
            return "Instrument dęty blaszany"
        if self.nazwa in ["skrzypce", "altowka", "wiolonczela", "kontrabas"]:
            return "Instrument strunowy, smyczkowy"
        if self.nazwa in ["harfa", "gitara", "lutnia", "klawesyn"]:
            return "Instrument strunowy, szarpany"
        if self.nazwa in ["fortepian", "pianino", "cymbały"]:
            return "Instrument strunowy, uderzany"
        if self.nazwa in ["perkusja", "kotly", "beben", "talerze", "ksylofon", "dzwonki", "wibrafon"]:
            return "Instrument perkusyjny"
        else:
            return "Przepraszamy, nie ma takiego instrumentu w spisie"


