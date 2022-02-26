class Collection:
    def __init__(self, array):
        """
        build a Collection with given list
        :param array: list of objects
        """
        self.array = array

    def get_collection(self):
        """
        returns the collection
        :return:
        """
        return self.array

    def add(self, item, option):
        """
        this method is realized in inheritance objects
        :param item: object to add the collection
        :param option: option to define another variable
        """
        raise NotImplementedError("Cannot add objects")  # all can do it raise Exception

    def __getitem__(self, i):
        """
        gets an index and returns the object in index i in collection
        :param i: index (int)
        :return: object from collection in index i
        """
        if i >= len(self.array) or i < 0:  # checks if index is in range of list length
            return None
        return self.array[i]

    def __eq__(self, other):
        """
        gets another object and compares it with itself, if identical returns True and False if not
        :param other: object to compare to
        :return: True if identical, otherwise False
        """
        if type(other) != type(self):  # checks if the type is the same
            raise TypeError("input type not a Collection")  # returns appropriate error or maybe false
        if len(self.array) != len(other.array):  # if they arent the same length then they cant be the same
            return False
        index = 0
        while index < len(self.array):  # goes over the lists and compares specific indexes
            if self.array[index] != other.array[index]:
                return False
            index += 1
        return True

    def __ne__(self, other):
        """
        gets another object and compares it with itself, if not identical returns True and False if not
        :param other: object to compare to
        :return: True if  not identical, otherwise False
        """
        if type(other) != type(self):  # checks if the type is the same
            raise TypeError("input type not a Collection")  # returns appropriate error or maybe false
        if self.array == other.array:  # uses __eq__ method to compare
            return False
        return True

    def __len__(self):
        """
        returns the length of the collection
        :return: length
        """
        return len(self.array)

    def __contains__(self, item):
        """
        checks if a given item is in the collection
        :param item: given object to check
        :return: if item is in collection, returns True, if not, False
        """
        for item_in_collection in self.array:
            if item_in_collection == item:
                return True
        return False

    def __str__(self):
        """
        returns a string representation of the collection with no spaces
        :return: collection as string
        """
        temp_array = ""
        for obj in self.array:
            temp_array += str(obj)
        return temp_array

    def __repr__(self):
        """
        returns a string representation of the collection with no spaces
        :return: collection as string
        """
        return self.__str__()  # uses __str__ function
