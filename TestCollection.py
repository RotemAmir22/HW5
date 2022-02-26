from Collection import Collection
from unittest import TestCase


class TestCollection(TestCase):
    def test_print_collection(self):
        print(" --> test: collection -> method: str and repr ")
        collect1 = Collection(["hello", 12, "monkeys"])
        self.assertEqual("hello12monkeys", collect1.__str__())
        self.assertEqual("hello12monkeys", collect1.__repr__())
        self.assertEqual("", Collection([]).__repr__())

    def test_get_collection(self):
        print(" --> test: collection -> method: get collection ")
        collection1 = Collection([1, 2, 3, 4])
        self.assertEqual([1, 2, 3, 4], collection1.get_collection())
        collect2 = Collection(["hey", 5, True])
        self.assertEqual(["hey", 5, True], collect2.get_collection())

    def test_add(self):
        print(" -->  test: collection -> method: add ")
        with self.assertRaises(NotImplementedError):
            collection1 = Collection([1, 2, 3, 4])
            collection1.add(4, "option")

    def test_getitem(self):
        print(" -->  test: collection -> method: get item ")
        collect1 = Collection([1, 2, 3, 4])
        self.assertEqual(3, collect1.__getitem__(2))
        self.assertEqual(None, collect1.__getitem__(7))

    def test_eq(self):
        print(" -->  test: collection -> method: eq ")
        self.assertEqual(True, Collection([1, 2, 3, 4]) == Collection([1, 2, 3, 4]))
        self.assertEqual(False, Collection([1, 2, 3, 5]) == Collection([1, 2, 3, 4]))
        self.assertEqual(False, Collection([1, 2, 3, 5]) == Collection([1, 2, 3]))
        with self.assertRaises(TypeError):
            Collection([1, 2, 3, 4]) == 12
        with self.assertRaises(TypeError):
            11 == Collection([1, 2, 3, 4])

    def test_ne(self):
        print(" -->  test: collection -> method: ne ")
        self.assertEqual(False, Collection([1, 2, 3, 4]) != Collection([1, 2, 3, 4]))
        self.assertEqual(True, Collection([1, 2, 3, 5]) != Collection([1, 2, 3, 4]))
        self.assertEqual(True, Collection([1, 2, 3, 5]) != Collection([1, 2, 3]))
        with self.assertRaises(TypeError):
            Collection([1, 2, 3, 4]) == 12
        with self.assertRaises(TypeError):
            11 == Collection([1, 2, 3, 4])

    def test_len(self):
        print(" --> test: collection -> method: len")
        self.assertEqual(4, len(Collection([1, 2, 3, 4])))
        self.assertEqual(2, len(Collection([1, 2])))
        self.assertEqual(0, len(Collection([])))

    def test_contains(self):
        print(" -->  test: collection -> method: contains ")
        self.assertEqual(True, Collection([1, 2, 3, 4]).__contains__(4))
        self.assertEqual(True, Collection([1, 2, "a", 4]).__contains__("a"))
        self.assertEqual(False, Collection([1, 2, "a", 4]).__contains__("b"))
