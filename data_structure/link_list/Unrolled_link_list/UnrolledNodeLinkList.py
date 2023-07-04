from nodes_link_list.UnrolledLinkNodeLinkList import SingleNode as Node
from nodes_link_list.UnrolledLinkNodeLinkList import UnrolledLinkListBlockNode as Block
import ctype

block_size = 2  # Number of nodes in block is block_size
block_head = None  # Head of the block is block head


class UnrolledNodeLinkList:
    def __init__(self, node_capacity):
        self.head = None
        self.node_capacity = node_capacity

    @staticmethod
    def __type_cast(address):
        """
        :param address: address of the desired value
        :return: the value present at the address
        """
        return ctype.cast(address, ctypes.py_object).value

    def searchElement(self, block_head, node_count):
        """
        :param block_head:
        :param node_count: Total number of nodes in completely filled blocks of unrolled link list
        :return:
        """
        # ---------- Find the block -------------------
        block_number = (node_count + block_size - 1) // block_size
        current_block = block_head
        block_number -= 1
        while block_number:
            current_block = self.__type_cast(p.next_address)
            block_number -= 1

        found_block = current_block
        # ----------------------------------------

        # ----------- Find the node --------------
        current_node = current_block.head
        node_count = node_count % block_size
        if not node_count:
            node_count = block_size

        node_count = current_block.node_count + 1 - node_count
        node_count -= 1
        while node_count:
            current_node = self.__type_cast(q.next_address)
            node_count -= 1

        found_node = current_node
        # -----------------------------------------
        return found_block, found_node

    def shift(self, A: Block):
        B = A
        global block_head
        while A.node_count > block_size:
            if not A.next_address:
                A.next = id(Block())
                B = self.__type_cast(A.next_address)
                temp = self.__type_cast(A.head.next_address)
                A.head.next_address = self.__type_cast(A.head.next_address).next_address
                B.head = temp
                temp.next_address = temp
            else:
                B = self.__type_cast(A.next_address)
                temp = self.__type_cast(A.head.next_address)
                A.head.next_address = self.__type_cast(temp.next_address).next_address
                temp.next_address = B.head.next_address
                B.head.next_address - id(temp)
                B.head = temp

            A.node_count -= 1
            B.node_count += 1

        A = B

    def addElement(self, k, value):
        global block_head
        if not block_head:  # Unrolled link list is empty
            block_head = Block()
            block_head.head = Node(value)
            block_head.head.next_address = id(block_head.head)
            block_head.node_count += 1
        elif k == 0:
            new_node = Node(value)
            p = block_head.head
            q = p.next_address
            p.next_address = id(new_node)
            new_node.next_address = q
            block_head.head = self.__type_cast(p.next_address)
            block_head.node_count += 1
            self.shift(block_head)
        else:
            r, p = self.searchEelment(block_head, k)
            q = p
            while q.next_address != id(p):
                new_node = Node(value)
                q = self.__type_cast(q.next_address)
                q.next_address = id(new_node)
                new_node.next_address = id(p)
                r.node_count += 1
                self.shift(r)
        return block_head
