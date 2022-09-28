import unittest

from main import Delta
"""
Ponieważ w main.py jest zdefiniowana klasa Delta, to w tym pliku musimy ją zaimportować.
Następnie tworzymy asercje, które sprawdzają czy nasza klasa działa poprawnie.
Poniżej przykład asercji, która sprawdza czy funkcja oblicz() zwraca poprawną wartość dla argumentów a=1, b=2, c=1.
"""
delta = Delta()
assert delta.oblicz(1, 2, 1) == (1, 2, 1, 0, -1.0), "Delta powinna wynosić 0"


"""
Pierwsza metoda testowa poniżej sprawdza czy instancja klasy Delta istnieje.
Druga sprwadza czy funkcja oblicz() zwraca poprawną wartość dla argumentów a=1, b=2, c=1.
"""

class DeltaTest(unittest.TestCase):
    def test_start_delta(self):
        delta = Delta()
        self.assertTrue(delta)

    def test_delta(self):
        delta = Delta()
        self.assertEqual(delta.oblicz(1, 2, 1), (1, 2, 1, 0, -1.0))


if __name__ == "__main__":
    unittest.main()
