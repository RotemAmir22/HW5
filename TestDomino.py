from unittest import TestCase

from Domino import Domino
from Exceptions import InvalidNumberException


class TestDomino(TestCase):
    def setUp(self):
        self.domino1 = Domino(1, 5)
        self.domino2 = Domino(5, 1)
        self.domino3 = Domino(3, 6)
        self.domino4 = Domino(5, 4)

    def test_str_and_repr(self):
        print(" --> test: domino  -> method: str and repr")
        self.assertEqual("[1|5]", self.domino1.__str__())
        self.assertEqual("[1|5]", self.domino1.__repr__())

    def test_get_left(self):
        print(" --> test: domino  -> method: get left and innit")
        self.assertEqual(1, Domino(1, 2).get_left())
        self.assertEqual(3, Domino(3, 2).get_left())
        with self.assertRaises(InvalidNumberException):
            Domino(7, 1)

    def test_get_right(self):
        print(" --> test: domino  -> method: get right and innit")
        self.assertEqual(2, Domino(1, 2).get_right())
        self.assertEqual(4, Domino(3, 4).get_right())
        with self.assertRaises(InvalidNumberException):
            Domino(1, 8)

    def test_eq(self):
        print(" --> test: domino  -> method: __eq__")
        self.assertEqual(True, self.domino1 == self.domino1)
        self.assertEqual(True, self.domino1 == self.domino2)
        self.assertEqual(False, self.domino1 == self.domino3)
        with self.assertRaises(TypeError):
            self.domino1 == [1, 5]

    def test_ne(self):
        print(" --> test: domino  -> method: __ne__")
        self.assertEqual(False, self.domino1 != self.domino1)
        self.assertEqual(False, self.domino1 != self.domino2)
        self.assertEqual(True, self.domino1 != self.domino3)
        with self.assertRaises(TypeError):
            self.domino1 == [1, 5]

    def test_gt(self):
        print(" --> test: domino  -> method: __gt__")
        self.assertEqual(False, self.domino1 > self.domino4)
        self.assertEqual(False, self.domino1 > self.domino1)
        self.assertEqual(True, self.domino4 > self.domino1)
        with self.assertRaises(TypeError):
            self.domino1 > 5

    def test_contains(self):
        print(" --> test: domino  -> method: __contains__")
        self.assertEqual(True, self.domino1.__contains__(1))
        self.assertEqual(True, self.domino4.__contains__(4))
        self.assertEqual(False, self.domino4.__contains__(1))
        with self.assertRaises(InvalidNumberException):
            self.domino1.__contains__(7)

    def test_flip(self):
        print(" --> test: domino  -> method: flip")
        domino1_flip = Domino(5, 1)
        domino2_flip = Domino(5, 4)
        self.assertEqual(domino1_flip, self.domino1.flip())
        self.assertEqual(domino2_flip, self.domino4.flip())
