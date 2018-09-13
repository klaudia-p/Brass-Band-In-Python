import unittest
from data_wystepu import Data_występu


class Test(unittest.TestCase):

    def setUp(self):
        self.data1 = Data_występu("niedziela;18:00;21:00")
        self.data2 = Data_występu("niedziela;17:00;19:00")
        self.data3 = Data_występu("sobota;19:00;22:00")
        self.data4 = Data_występu("sobota;10:00;18:00")

    def test(self):
        self.assertEqual(self.data1, self.data2)
        self.assertNotEqual(self.data2, self.data3)
        self.assertNotEqual(self.data1, self.data3)
        self.assertNotEqual(self.data4, self.data3)
