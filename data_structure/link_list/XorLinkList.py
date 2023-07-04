from .nodes_link_list.XorLinkListNode import XorLinkListNode as Node
import ctype


class XorLinkList:
    def __init__(self):
        self.head: Node or None = None
        self.tail: Node or None = None
        self.__nodes = []

    @staticmethod
    def __type_cast(address):
        """
        :param address: address of the desired value
        :return: the value present at the address
        """
        return ctype.cast(address, ctypes.py_object).value

    def isEmpty(self):
        """
        :return: True if link list is empty else False
        """
        return self.head is None

    def insertAtStart(self, value):
        node = Node(value)
        if self.head:
            self.head.npx = id(node) ^ self.head.npx
            node.npx = id(self.head)
            self.head = node
        else:
            self.head = node
            self.tail = node

        self.__nodes.append(node)

    # Method to insert node at end
    def insertAtEnd(self, value):
        node = Node(value)
        if self.tail:
            self.tail.npx = id(node) ^ self.tail.npx
            node.npx = id(self.tail)
            self.tail = node
        else:
            self.head = node
            self.tail = node

        self.__nodes.append(node)

    # Removing the node from the beginning
    def deleteFromStart(self):

        # If list is empty
        if self.isEmpty():
            return "List is Empty"
        elif self.head == self.tail:  # If list has only 1 node
            self.head = None
            self.tail = None
            return "Deleted last node"
        elif (0 ^ self.head.npx) == id(self.tail):  # If list has only 2 node
            self.head = self.tail
            self.head.npx = self.tail.npx = 0
        else:  # If list has only 3 node
            res = self.head.value
            next_node = self.__type_cast(0 ^ self.head.npx)
            address_of_next_to_next_node = (id(self.head) ^ next_node.npx)
            self.head = next_node
            self.head.npx = address_of_next_to_next_node
            return res

    # remove node from end
    def deleteFromEnd(self):
        # If list is empty
        if self.isEmpty():
            return "List is Empty"
        elif self.head == self.tail:  # If list has only 1 node
            self.head = None
            self.tail = None
            return "Deleted last node"
        elif (0 ^ self.head.npx) == id(self.tail):  # If list has only 2 node
            self.head = self.tail
            self.head.npx = self.tail.npx = 0
        else:  # If list has only 3 node
            previous_address = 0
            node = self.head
            next_address = 1
            while next_address:
                next_address = previous_address ^ self.node.npx
                if next_address:
                    previous_address = id(node)
                    node = self.__type_cast(next_address)
            res = node.value  # Node which need to be deleted
            previous_node = self.__type_cast(previous_address)
            next_node_address = previous_node.npx ^ id(node)  # Next node need to be deleted
            previous_node.npx = next_node_address ^ 0
            self.tail = previous_node
            return res

    def printList(self):
        if self.head:
            previous_address = 0
            node = self.head
            next_address = 1
            print(node.value, end=" ")
            while next_address:
                next_address = previous_address ^ node.npx
                if next_address:
                    previous_address = id(node)
                    node = self.__type_cast(next_address)
                    print(node.value, end=" ")
                else:
                    return
        else:
            print("List is empty")

    def printListReverse(self):
        if self.tail:
            previous_address = 0
            node = self.tail
            next_address = 1
            while next_address:
                next_address = previous_address ^ node.npx
                if next_address:
                    previous_address = id(node)
                    node = self.__type_cast(next_address)
                    print(node.value, end=" ")
                else:
                    return
        else:
            print("List is empty ..")

    def getLength(self):
        if self.isEmpty():
            return 0
        node = self.head
        previous_address, next_address, count = 0, 1, 1
        while next_address:
            next_address = previous_address ^ node.npx
            if next_address:
                previous_address = id(node)
                node = self.__type_cast(next_address)
                count += 1
        return count

        # Get the node by index value
