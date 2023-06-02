from nodes_link_list.UnrolledArrayNodeLinkList import UnrolledArrayNode as Node
import logging
import ctypes

logging.basicConfig(
    # filename="circular_list.log",
    format='%(asctime)s %(levelname)s:%(message)s',
    # filemode='w',
    level=logging.DEBUG
)

logger = logging.getLogger(__name__)

block_size = 2
block_head = None


class UnrolledArrayLinkList:
    def __init__(self):
        self.head:Node or None = None
        self.node_capacity = 0

    def isEmpty(self):
        return self.head is None

    @staticmethod
    def __type_cast(address):
        """
        :param address: address of the desired value
        :return: the value present at the address
        """
        if not address:
            return
        return ctypes.cast(address, ctypes.py_object).value

    @staticmethod
    def addNodeElement(value, node=None):
        node = node if node else Node()
        node.array.append(value)
        node.elemCount += 1
        node.array.sort()
        return node

    def getLastNode(self):
        if self.isEmpty():
            return None
        current = self.head
        while current.next:
            if not current.isFull():
                return current
            current = self.__type_cast(current.next)
        return current

    def insertAtEnd(self, value):
        """
        :param value: Insert the value at the end
        :return: True
        """
        current_node = self.getLastNode()
        if not current_node:
            self.head = UnrolledArrayLinkList.addNodeElement(value)
        elif current_node.isFull():
            new_node = UnrolledArrayLinkList.addNodeElement(value)
            new_node.next = current_node.next
            current_node.next = id(new_node)
        else:
            current_node = UnrolledArrayLinkList.addNodeElement(current_node, value)

    def insertInBetween(self, block_number, position, value):
        if self.isEmpty():
            self.head = UnrolledArrayLinkList.addNodeElement(value)
        else:
            curr_node = self.head
            prev_node = None
            while curr_node is not None:
                if block_number == 1:
                    if curr_node.elemCount < 4:
                        if position <= curr_node.elemCount:
                            curr_node.array.insert(position - 1, value)
                            curr_node.elemCount += 1
                            return
                        elif position <= 4:
                            curr_node.array.append(value)
                            curr_node.elemCount += 1
                            return
                        else:
                            break
                    else:
                        break
                block_number -= 1
                prev_node = curr_node
                curr_node = curr_node.next

            if curr_node is not None:
                self.shift(prev_node, curr_node)
                self.insert(key, block_number, position)

    def shift(self, prev_node, curr_node):
        while len(curr_node.keys) >= curr_node.maxCount:
            mid = curr_node.max_capacity // 2
            new_node = Node()
            new_node.keys = curr_node.keys[mid:]
            curr_node.keys = curr_node.keys[:mid]
            new_node.next = curr_node.next
            curr_node.next = new_node
            if prev_node is not None:
                prev_node.next = new_node
            prev_node = curr_node
            curr_node = new_node

    def search(self, key):
        curr_node = self.head
        while curr_node is not None:
            if key in curr_node.keys:
                return True
            curr_node = curr_node.next
        return False

    def display(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.array)
            curr_node = curr_node.next

    def deleteFromStart(self):
        if self.isEmpty():
            print("List is empty. No elements to delete.")
        else:
            if self.head.elemCount > 1:
                self.head.array.pop(0)
                self.head.elemCount -= 1
            else:
                self.head = self.__type_cast(self.head.next)

    def deleteFromEnd(self):
        if self.isEmpty():
            print("List is empty. No elements to delete.")
        else:
            curr_node = self.head
            prev_node = None
            while curr_node.next is not None:
                prev_node = curr_node
                curr_node = self.__type_cast(curr_node.next)
            if curr_node.elemCount > 1:
                curr_node.array.pop()
                curr_node.elemCount -= 1
            else:
                if prev_node is None:
                    self.head = None
                else:
                    prev_node.next = None

    def deleteInBetween(self, block_number, position):
        if self.isEmpty():
            print("List is empty. No elements to delete.")
        else:
            curr_node = self.head
            prev_node = None
            while curr_node is not None:
                if block_number == 1:
                    if 1 <= position <= curr_node.elemCount:
                        curr_node.array.pop(position - 1)
                        curr_node.elemCount -= 1
                        if curr_node.elemCount == 0:
                            if prev_node is None:
                                self.head = None
                            else:
                                prev_node.next = curr_node.next
                        return
                    else:
                        break
                block_number -= 1
                prev_node = curr_node
                curr_node = self.__type_cast(curr_node.next)

            print("Invalid block number or position.")


if __name__ == "__main__":
    # Example usage:
    # Example usage:
    linked_list = UnrolledArrayLinkList()
    linked_list.insertInBetween(1, 1, 1)
    linked_list.insertInBetween(1, 2, 2)
    linked_list.insertInBetween(1, 3, 3)
    linked_list.insertInBetween(2, 1, 4)
    linked_list.insertInBetween(2, 2, 5)
    linked_list.insertInBetween(2, 3, 6)
    linked_list.insertInBetween(3, 1, 7)

    linked_list.display()
    # Output: [1, 2, 3]
    #         [4, 5, 6]
    #         [7]

    linked_list.deleteFromStart()
    linked_list.deleteFromEnd()
    linked_list.deleteInBetween(2, 2)

    linked_list.display()