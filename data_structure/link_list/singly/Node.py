# Singly Link list

class Node:
    def __init__(self, data=None, data_pointer=None):
        self._data = data
        self._dataPointer: Node = data_pointer
        pass

    def setData(self, data):
        self._data = data

    def setDataPointer(self, pointer):
        self._dataPointer = pointer

    def getData(self):
        return self._data

    def getDataPointer(self):
        return self._dataPointer

    def hasNext(self):
        return self._dataPointer is not None
