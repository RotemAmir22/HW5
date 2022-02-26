import copy

from Exceptions import InvalidNumberException


class Domino:
    def __init__(self, left, right):
        """
        creates a domino block with 2 numbers -> right and left side
        :param left: number in the range [0,6] (int)
        :param right: number in the range [0,6] (int)
        """
        if not (0 <= left <= 6):  # checks if in range
            raise InvalidNumberException("input left number out of range; range -> [0-6]")
        if not (0 <= right <= 6):  # checks if in range
            raise InvalidNumberException("input right number out of range; range -> [0-6]")
        self.__left_side = left  # private attribute
        self.__right_side = right  # private attribute

    def get_left(self):
        """
        returns a copy of the left number of the domino block
        :return: int
        """
        return copy.copy(self.__left_side)

    def get_right(self):
        """
        returns a copy of the right number of the domino block
        :return: int
        """
        return copy.copy(self.__right_side)

    def __str__(self):
        """
        converts the domino to a string representation in specific format:
        [ left_side | right_side ] (no spaces)
        :return: string of domino block in format
        """
        return "[" + str(self.get_left()) + "|" + str(self.get_right()) + "]"

    def __repr__(self):
        """
        prints the string representation of domino block
        :return: string of domino block in format
        """
        return self.__str__()  # uses __str__ function

    def __eq__(self, other):
        """
        gets two domino blocks and returns True if they are identical
        doesnt matter what side of the block the values are.
        :param other: compares itself to this Domino block
        :return: if identical returns True and if not, False
        """
        if type(other) != type(self):  # checks they are the same type
            raise TypeError("input type not Domino")
        if self.get_left() == other.get_left() and self.get_right() == other.get_right():  # order doesnt matter
            return True
        elif self.get_left() == other.get_right() and self.get_right() == other.get_left():
            return True
        return False

    def __ne__(self, other):
        """
        checks if two domino blocks are not identical, if not, returns True, if they are returns False
        :param other: compares itself to this Domino block
        :return: if not identical returns True and if they are, False
        """
        if type(other) != type(self):  # checks they are the same type
            raise TypeError("input type not Domino")
        if self == other:  # uses __eq__ method
            return False
        return True

    def __gt__(self, other):
        """
        compare the sum of itself to another Domino block.
        if the its own sum is larger-> returns True, if not, returns False
        sum: left side + right side
        :param other: another Domino to compare to
        :return: True if its sum is larger than the other Domino, else False.
        """
        if type(other) != type(self):  # checks type
            raise TypeError("input type not Domino")
        if (self.get_right() + self.get_left()) > (other.get_right() + other.get_left()):
            return True
        return False

    def __contains__(self, key):
        """
        gets a key and checks if the Domino has this value
        :param key: given number
        :return: True if the Domino has this number, False if not
        """
        if not (0 <= key <= 6):  # checks if in range
            raise InvalidNumberException("input left number out of range; range -> [0-6]")
        if self.__left_side == key or self.__right_side == key:  # if at least one side has the key
            return True
        return False

    def flip(self):
        """
        flips the Domino:
        new left side = old right side
        new right side = old left side
        :return: new Domino with new sides
        """
        return Domino(self.__right_side, self.__left_side)
