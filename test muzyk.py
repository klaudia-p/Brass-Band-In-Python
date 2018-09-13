import unittest
from muzyk import Muzyk


class Test(unittest.TestCase):

    def setUp(self):
        self.w1 = Muzyk("Klaudia Pietras", 21, "flet")
        self.w2 = Muzyk("Krzysztof Krawiec", 16, "trabka")

    def test(self):
        self.assertEqual(self.w1.__str__(), "Imię i nazwisko: Klaudia Pietras\nWiek: 21 lat\nInstrument: flet")
        self.assertEqual(self.w1.czy_pełnoletnia(), True)
        self.assertEqual(self.w2.czy_pełnoletnia(), False)