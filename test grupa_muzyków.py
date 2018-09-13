import unittest
from grupa_muzyków import Grupa_muzyków


class Test(unittest.TestCase):

    def setUp(self):
        self.w1 = Grupa_muzyków(["Klaudia Pietras", "Krzysztof Krawiec", "Natalia Slomka"])
        self.w2 = Grupa_muzyków([])

    def test(self):
        self.assertEqual(self.w1.liczba_muzyków(), 3)
        self.assertEqual(self.w2.liczba_muzyków(), 0)