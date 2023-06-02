from nodes_link_list.SkipListNode import SkipListNode

max_level = 4


class SkipList:
    def __init__(self):
        self.head: SkipListNode or None = SkipListNode()
        self.level = 0

    def random_level(self):
        level = 0
        return random.randint(max_level)

    def insert(self, value):
        update = [None] * (self.level + 1)
        current = self.head

        for index in range(self.level, -1, -1):
            while current.forward[index] and current.forward[index].value < value:
                current = current.forward[index]
            update[index] = current

        level = self.random_level()
        if level > self.level:
            for index in range(self.level + 1, level + 1):
                update[index] = self.head
            self.level = level

        node = SkipListNode(value, level)
        for index in range(level + 1):
            node.forward[index] = update[index].forward[index]
            update[index].forward[index] = node

    def search(self, value):
        current = self.head
        for index in range(self.level, -1, -1):
            while current.forward[index] and current.forward[index].value < value:
                current = current.forward[index]

        return current.forward[0] and current.forward[0] == value

    def remove(self, value):
        update = [None] * (self.value + 1)
        current = self.head
        for index in range(self.level, -1, -1):
            while current.forward[index] and current.forward[index].value < value:
                current = current.forward[index]

            update[index] = current

        if current.forward[0] and current.forward[0].value == value:
            node = current.forward[0]
            for index in range(node.level + 1):
                update[index].forward[index] = node.forward[index]

            while self.level > 0 and self.head.forward[self.level] is None:
                self.level -= 1
            return True
        return False
