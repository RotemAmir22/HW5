from unittest import TestCase
from Domino import Domino
from Exceptions import NoSuchDominoException
from Hand import Hand


class TestHand(TestCase):
    def setUp(self):
        self.hand1 = Hand([Domino(1, 2), Domino(3, 4), Domino(5, 5)])
        self.hand2 = self.hand1
        self.hand3 = Hand([Domino(3, 2), Domino(3, 6), Domino(1, 5)])
        self.hand4 = Hand([Domino(2, 1), Domino(4, 3), Domino(5, 5)])

    def test_add(self):
        print(" --> test: hand -> method: add ")
        self.hand1.add(Domino(2, 2), 2)
        self.assertEqual("[1|2][3|4][2|2][5|5]", self.hand1.__str__())
        self.hand1.add(Domino(2, 5))
        self.assertEqual("[1|2][3|4][2|2][5|5][2|5]", self.hand1.__str__())

    def test_remove(self):
        print(" --> test: hand -> method: remove ")
        self.assertEqual(1, self.hand2.remove_domino(Domino(3, 4)))
        self.assertEqual(0, self.hand2.remove_domino(Domino(2, 1)))
        with self.assertRaises(NoSuchDominoException):
            self.hand2.remove_domino(Domino(1, 3))

    def test_getitem(self):
        print(" --> test: hand -> method: getitem ")
        self.assertEqual(Domino(3, 6), self.hand3.__getitem__(1))
        self.assertEqual(Domino(3, 2), self.hand3.__getitem__(0))
        self.assertEqual(None, self.hand3.__getitem__(5))

    def test_contains(self):
        print(" --> test: hand -> method: contains ")
        self.assertEqual(True, self.hand1.__contains__(Domino(2, 1)))
        self.assertEqual(True, self.hand1.__contains__(Domino(1, 2)))
        self.assertEqual(False, self.hand1.__contains__(Domino(6, 1)))

    def test_eq(self):
        print(" --> test: hand -> method: eq ")
        self.assertEqual(True, self.hand1 == self.hand2)
        self.assertEqual(True, self.hand1 == self.hand1)
        self.assertEqual(True, self.hand1 == self.hand4)
        self.assertEqual(False, self.hand1 == self.hand3)

    def test_ne(self):
        print(" --> test: hand -> method: ne ")
        self.assertEqual(False, self.hand1 != self.hand2)
        self.assertEqual(False, self.hand1 != self.hand4)
        self.assertEqual(True, self.hand1 != self.hand3)

    def test_len(self):
        print(" --> test: hand -> method: len ")
        self.assertEqual(3, len(self.hand1))
        self.assertEqual(0, len(Hand([])))
        self.hand1.add(Domino(2, 2), 2)
        self.assertEqual(4, len(self.hand1))

    def test_str_repr(self):
        print(" --> test: hand -> method: str/repr ")
        self.assertEqual("[2|1][4|3][5|5]", self.hand4.__str__())
        self.assertEqual("[2|1][4|3][5|5]", self.hand4.__repr__())
        self.assertEqual("", Hand([]).__str__())
