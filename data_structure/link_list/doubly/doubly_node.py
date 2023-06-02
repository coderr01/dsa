# Doubly link-list node

class DoublyNode:
    def __init__(self, data=None):
        self._data = data
        self._previous = None
        self._next = None

    def setData(self, data):
        self._data = data

    def setPrevious(self, previous):
        self._previous = previous

    def setNext(self, next_node):
        self._next = next_node

    def getData(self):
        return self._data

    def getPrevious(self):
        return self._previous

    def getNext(self):
        return self._next

    def hasNext(self):
        return self._next is not None

    def hasPrevious(self):
        return self._previous is not None

    def __str__(self):
        return "DoublyNode(data={data}, has_previous={pre}, has_next={nxt})".format(
            data=self._data, nxt=self.hasNext(), pre=self.hasPrevious()
        )