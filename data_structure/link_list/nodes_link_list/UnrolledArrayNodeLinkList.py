maxCount = 4


class UnrolledArrayNode:

    def __init__(self):
        self.elemCount = 0
        self.array: list = [0] * maxCount
        self.next = None

    @staticmethod
    @property
    def maxCount() -> int:
        return 4

    def isFull(self):
        return self.elemCount == maxCount

    def is_underflow(self):
        return self.elemCount < maxCount // 2

