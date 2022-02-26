from Collection import Collection
from Exceptions import InvalidNumberException, EmptyBoardException, FullBoardException


class Board(Collection):
    def __init__(self, max_capacity):
        """
        generates a Board beginning with an empty collection
        :param max_capacity: maximum Dominoes Board can contain-> between 1 and 28
        """
        if not (1 <= max_capacity <= 28):
            raise InvalidNumberException("input not in range -> [1,28]")
        self.max_capacity = max_capacity
        Collection.__init__(self, [])  # empty list

    def in_left(self):
        """
        if the list is not empty, returns the left value of left Domino on the board
        :return: left value (if there is)
        """
        if not self.array:  # checks if the list is not empty
            raise EmptyBoardException("board is empty-> no left object")
        domino_temp = self.array[0]
        return domino_temp.get_left()

    def in_right(self):
        """
        if the list is not empty, returns the right value of right Domino on the board
        :return: right value (if there is)
        """
        if not self.array:  # checks if the list is not empty
            raise EmptyBoardException("board is empty-> no right object")
        domino_temp = self.array[len(self.array) - 1]
        return domino_temp.get_right()

    def valid_add_to_left(self, domino):
        """
        checks if it is possible to add the domino to the board on the left side:
        compares the left value of the left domino with the right side of the given domino to add
        :param domino: given domino to add
        :return: if successful returns True, if not, False
        """
        if len(self.array) == self.max_capacity:  # checks if board is full
            raise FullBoardException("board is full, cannot add object")
        if not len(self.array):
            return True
        if domino.get_right() == self.in_left():
            return True
        return False

    def valid_add_to_right(self, domino):
        """
        checks if it is possible to add the domino to the board on the right side:
        compares the right value of the right domino with the left side of the given domino to add
        :param domino: given domino to add
        :return: if successful returns True, if not, False
        """
        if len(self.array) == self.max_capacity:  # checks if board is full
            raise FullBoardException("board is full, cannot add object")
        if not len(self.array):
            return True
        if domino.get_left() == self.in_right():
            return True
        return False

    def add_left_helper(self, domino):
        """
        adds the domino to the left side of the board
        :param domino: given domino to add
        """
        self.array.insert(0, domino)

    def add_right_helper(self, domino):
        """
        adds the domino to the right side of the board
        :param domino: given domino to add
        """
        self.array.append(domino)

    def add(self, domino, add_to_right=True):
        """
        adds a given domino to the board, checks both sides:
        1. if add to right is True, tries to add to right side of board and if cant then flips the domino.
        2. if add to right is False, tries to add to left side of board and if cant then flips the domino.
        :param domino: given domino to add
        :param add_to_right: default value is True, but if False, tries to add to the left
        :return: True if able to add and False if not
        """
        if add_to_right:  # tries to add to the right side of the board
            if self.valid_add_to_right(domino):  # tries to add given domino as is
                self.add_right_helper(domino)
                return True
            if self.valid_add_to_right(domino.flip()):  # tries to add flipped domino
                self.add_right_helper(domino.flip())
                return True
        else:  # tries to add to the left side of board
            if self.valid_add_to_left(domino):  # tries to add given domino as is
                self.add_left_helper(domino)
                return True
            if self.valid_add_to_left(domino.flip()):  # tries to add flipped domino
                self.add_left_helper(domino.flip())
                return True
        return False

    def add_left(self, domino):
        """
        adds given domino to the left side of the board, if fails, flips domino.
        if unsuccessful returns False
        :param domino:given domino to add
        :return: True if able, False if not
        """
        if self.valid_add_to_left(domino):
            self.add_left_helper(domino)
            return True
        if self.valid_add_to_left(domino.flip()):
            self.add_left_helper(domino.flip())
            return True
        return False

    def add_right(self, domino):
        """
        adds given domino to the right side of the board, if fails, flips domino.
        if unsuccessful returns False
        :param domino:given domino to add
        :return: True if able, False if not
        """
        if self.valid_add_to_right(domino):
            self.add_right_helper(domino)
            return True
        if self.valid_add_to_right(domino.flip()):
            self.add_right_helper(domino.flip())
            return True
        return False

    def __contains__(self, key):
        """
        return True if the key is on the board and False if not
        :param key: item to find on board
        :return: True if on board and False if not
        """
        for obj in self.array:
            if obj.get_left() == key.get_left() and obj.get_right() == key.get_right():  # order does matter
                return True
        return False

    def __eq__(self, other):
        """
        checks if the two boards are identical, the order does matter.
        :param other: other board to compare to
        :return: True if identical, and False if not
        """
        if type(other) != type(self):  # checks type
            raise TypeError("input not Board")
        if self.max_capacity != other.max_capacity:  # checks max capacity of each board
            return False
        if len(self.array) != len(other.array):  # checks length
            return False

        for i in range(len(self.array)):  # order matters so cant use Collections method
            if self.array[i].get_right() != other.array[i].get_right() or \
                    self.array[i].get_left() != other.array[i].get_left():
                return False
        return True

    def __ne__(self, other):
        """
        checks if the boards are not identical, order does matter.
        :param other: other board to compare to
        :return: True if different, and False if alike
        """
        if type(other) != type(self):  # checks type
            raise TypeError("input not Board")
        if self.array == other.array:  # uses __eq__ method
            return False
        return True
