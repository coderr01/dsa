import random


class SkipListNode:
    def __init__(self, value =None, level = 0):
        self.value = value
        self.forward = [None] * level   # TO store the pointers (address) of upcoming nodes
        
