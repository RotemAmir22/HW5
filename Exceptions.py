class Exceptions(Exception):
    """
    Father exception class that bequeaths to custom exceptions two methods:
    1. __init__ -> saves message to print with exception error message
    2. __str__ -> base template of error message
    """

    def __init__(self, msg):
        """
        gets a message to print with raised exception
        :param msg: inputted message
        """
        self.msg = msg

    def __str__(self):
        """
        configures error message
        :return: exception error and given message from builder
        """
        return "ERROR " + self.msg


class EmptyBoardException(Exceptions):
    """raised when the board is empty"""
    pass


class FullBoardException(Exceptions):
    """raised when the board is full, cannot add additional domino"""
    pass


class NoSuchDominoException(Exceptions):
    """raised when wanted domino to be removed is not in the collection"""
    pass


class InvalidNumberException(Exceptions):
    """raised when number inputted is not in range"""
    pass
