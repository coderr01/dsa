# For the data and equation in the figure of revolution.

class PointerDiffNode:
    def __init__(self, data=None, pointerDiff=None):
        self.data = data
        self.pointerDiff = pointerDiff

    # Setter method for list
    def setData(self, data):
        self.data = data

    def setPointerDiff(self, prev, nxt):
        self.pointerDiff = prev ^ nxt

    # Getter method for list
    def getData(self):
        return self.data

    def getPointerDiff(self):
        return self.pointerDiff
