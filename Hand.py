from Collection import Collection
from Exceptions import NoSuchDominoException


class Hand(Collection):

    def add(self, domino, index=None):
        """
        gets a domino to add the hand and add it in the given index.
        if no index given then add to the right side of the hand
        :param domino: given domino
        :param index: default value is None, if no then add to given index
        """
        if index is None:
            self.array.append(domino)
        else:
            self.array.insert(index, domino)

    def remove_domino(self, domino):
        """
        gets a specific domino and removes it from the hand collection
        :param domino: given domino to remove
        :return: index of given domino in list, if no domino exists-> raises an exception: NoSuchDominoException
        """
        for index in range(len(self.array)):
            if self.array[index] == domino:
                self.array.pop(index)
                return index
        raise NoSuchDominoException("this domino is not in the hand collection")
