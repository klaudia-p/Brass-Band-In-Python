import unittest
from występ import Występ


class Test(unittest.TestCase):

    def setUp(self):
        self.w1 = Występ("koncert", 8000, "niedziela;18:00;21:00")
        self.w2 = Występ("pogrzeb", 200, "czwartek;14:30;15:30")
        self.w3 = Występ("koncert", 8000, "niedziela;19:00;22:00")

    def test(self):
        self.assertLess(self.w2, self.w1)
        self.assertEqual(self.w1, self.w3)
        self.assertEqual(self.w1.potrzebne_instrumenty(), ['flet',
                                                           'oboj',
                                                           'klarnet',
                                                           'fagot',
                                                           'saksofon',
                                                           'saksofon',
                                                           'waltornia',
                                                           'trabka',
                                                           'trabka',
                                                           'trabka',
                                                           'puzon',
                                                           'puzon',
                                                           'tuba',
                                                           'sakshorn',
                                                           'perkusja',
                                                           'kotly',
                                                           'beben',
                                                           'talerze',
                                                           'ksylofon'])
        self.assertEqual(self.w3.__str__(),"Wydarzenie: koncert\nData: niedziela, 19:00 - 22:00\nKoszt: 8000 zł.")
