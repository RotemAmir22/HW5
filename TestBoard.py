from unittest import TestCase
from Domino import Domino
from Board import Board
from Exceptions import EmptyBoardException, FullBoardException, InvalidNumberException


class TestBoard(TestCase):
    def setUp(self):
        self.board1 = Board(4)
        self.board1.add(Domino(1, 2))
        self.board1.add(Domino(2, 5))
        self.board1.add(Domino(3, 1), False)

        self.board2 = Board(3)
        self.board2.add(Domino(3, 2))
        self.board2.add(Domino(2, 4))
        self.board2.add(Domino(4, 1))

        self.board3 = Board(3)
        self.board3.add(Domino(2, 2))
        self.board3.add(Domino(3, 2), False)
        self.board3.add(Domino(2, 4))

    def test_in_left(self):
        print(" --> test: board -> method: in_left ")
        self.assertEqual(3, self.board1.in_left())
        with self.assertRaises(EmptyBoardException):
            Board(2).in_left()
        with self.assertRaises(InvalidNumberException):
            Board(-1)
        with self.assertRaises(InvalidNumberException):
            Board(29)

    def test_in_right(self):
        print(" --> test: board -> method: in_right ")
        self.assertEqual(1, self.board2.in_right())
        with self.assertRaises(EmptyBoardException):
            Board(2).in_right()
        with self.assertRaises(InvalidNumberException):
            Board(-1)
        with self.assertRaises(InvalidNumberException):
            Board(29)

    def test_add(self):
        print(" --> test: board -> method: add ")
        board = Board(4)
        board.add(Domino(1, 2))
        board.add(Domino(5, 2))  # flip
        board.add(Domino(3, 1), False)
        self.assertEqual(False, board.add(Domino(3, 1)))
        self.assertEqual("[3|1][1|2][2|5]", board.__str__())
        self.assertEqual(False, board.add(Domino(4, 6)))
        board.add(Domino(3, 4), False)  # flip
        with self.assertRaises(FullBoardException):
            board.add(Domino(2, 4))

    def test_add_left_add_right(self):
        print(" --> test: board -> method: add in left/right ")
        board1 = Board(5)
        """add left:"""
        self.assertEqual(True, board1.add_left(Domino(1, 2)))
        self.assertEqual(True, board1.add_left(Domino(4, 1)))
        self.assertEqual(False, board1.add_left(Domino(6, 2)))

        """add right:"""
        self.assertEqual(True, board1.add_right(Domino(2, 5)))
        self.assertEqual(False, board1.add_right(Domino(3, 2)))

        """uses flip()"""
        self.assertEqual(True, board1.add_left(Domino(4, 1)))
        self.assertEqual(True, board1.add_right(Domino(1, 5)))
        with self.assertRaises(FullBoardException):
            board1.add_left(Domino(5, 1))
        with self.assertRaises(FullBoardException):
            board1.add_right(Domino(1, 1))

    def test_getitem(self):
        print(" --> test: board -> method: getitem ")

        self.assertEqual(Domino(2, 2), self.board3.__getitem__(1))
        self.assertEqual(Domino(3, 2), self.board3.__getitem__(0))
        self.assertEqual(Domino(2, 4), self.board3.__getitem__(2))
        self.assertEqual(None, self.board3.__getitem__(4))

    def test_contains(self):
        print(" --> test: board -> method: contains")
        self.assertEqual(True, self.board3.__contains__(Domino(2, 2)))
        self.assertEqual(False, self.board3.__contains__(Domino(4, 2)))

    def test_eq_and_ne(self):
        print(" --> test: board -> method: eq/ne ")
        board1 = Board(4)
        board1.add(Domino(2, 2))
        board1.add(Domino(3, 2))
        board1.add(Domino(2, 4), False)
        board1.add(Domino(4, 4), False)
        board2 = board1
        """eq:"""
        self.assertEqual(True, board1 == board2)
        self.assertEqual(False, board1 == Board(4))
        self.assertEqual(False, board1 == Board(2))
        board3 = Board(4)
        board3.add(Domino(2, 2))
        board3.add(Domino(3, 2))
        board3.add(Domino(2, 4), False)
        board3.add(Domino(4, 5), False)
        self.assertEqual(False, board1 == board3)
        """ne:"""
        self.assertEqual(False, board1 != board2)
        self.assertEqual(True, board1 != Board(4))
        self.assertEqual(True, board1 != Board(2))
        self.assertEqual(True, board1 != board3)

        with self.assertRaises(TypeError):
            board1 == "hello"
        with self.assertRaises(TypeError):
            board1 != 123

    def test_len_str_repr(self):
        print(" --> test: board -> method: len/str/repr ")
        board1 = Board(4)
        board1.add(Domino(2, 2))
        self.assertEqual(1, len(board1))
        board1.add(Domino(3, 2), False)
        self.assertEqual(2, len(board1))
        board1.add(Domino(2, 4))
        self.assertEqual(3, len(board1))
        board1.add(Domino(4, 4))
        self.assertEqual(4, len(board1))
        """str/repr:"""
        self.assertEqual("[3|2][2|2][2|4][4|4]", board1.__str__())
        self.assertEqual("[3|2][2|2][2|4][4|4]", board1.__repr__())
        self.assertEqual("", Board(1).__repr__())
