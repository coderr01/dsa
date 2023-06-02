from doubly_node import DoublyNode
import logging

logging.basicConfig(
    # filename="singly_list.log",
    format='%(asctime)s %(levelname)s:%(message)s',
    # filemode='w',
    level=logging.DEBUG
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class DoublyLinkList:
    def __init__(self):
        self.head: DoublyNode or None = None
        self.tail: DoublyNode or None = None
        self.length = 0
        self.insertNode = self._InsertNode(self)
        self.deleteNode = self._DeleteNode(self)

    class _InsertNode:
        def __init__(self, outer_self):
            self._outer_self = outer_self

        def insertAtStart(self, data):
            new_node = DoublyLinkList._getNodeByData(data)
            if self._outer_self.length:
                self._outer_self.head.setPrevious(new_node)
                new_node.setNext(self._outer_self.head)
            self._outer_self.head = new_node
            self._nodeAdded()

        def _nodeAdded(self):
            self._outer_self.length += 1
            logger.info("New Node added")

        def insertAtEnd(self, data):
            new_node = DoublyLinkList._getNodeByData(data)
            current_node = self._outer_self.getNodeByPosition(self._outer_self.length)
            new_node.setPrevious(current_node)
            current_node.setNext(new_node)
            self._nodeAdded()

        def insertAtPosition(self, data, position):
            # if self._validatePosition(position): return
            if position == 1: self.insertAtStart(data); return
            if position == self._outer_self.length: self.insertAtEnd(data); return
            new_node = DoublyLinkList._getNodeByData(data=data)
            current = self._outer_self.getNodeByPosition(position)
            logger.info("Currently node at position: {pos} is {node}".format(pos=position, node=current))
            new_node.setNext(current)
            new_node.setPrevious(current.getPrevious())
            current.getPrevious().setNext(new_node)
            current.setPrevious(new_node)
            self._nodeAdded()

        def _validatePosition(self, position) -> bool:
            valid_condition = self._outer_self.length >= position > 0
            if not valid_condition:
                logger.error("Invalid position to enter the node")
            return valid_condition

    class _DeleteNode:
        def __init__(self, outer_self):
            self._outer_self = outer_self

        def _nodeDeleted(self):
            self._outer_self.length -= 1
            logger.info("Node deleted Successfully")

        def deleteFromBeginning(self):
            self._outer_self.head = self._outer_self.head.getNext()
            self._nodeDeleted()

        def deleteFromEnd(self):
            current_node = self._outer_self.getNodeByPosition(self._outer_self.length - 1)
            current_node.setNext(None)
            self._nodeDeleted()

        def deleteFromPosition(self, position):
            current = self._outer_self.getNodeByPosition(position)
            logger.info("Node which we need to delete. "+str(current))
            current.getPrevious().setNext(current.getNext())
            current.getNext().setPrevious(current.getPrevious())
            self._nodeDeleted()

    @staticmethod
    def _getNodeByData(data):
        return DoublyNode(data=data)

    def getNodeByPosition(self, position):
        if not self.length >= position > 0:
            logger.error("Given an invalid position")
            return
        current = self.head
        count = 1
        while count < position:
            current = current.getNext()
            count += 1
        return current

    def printLinkList(self):
        current = self.head
        while current:
            logger.info(current)
            current = current.getNext()


def main():
    doubly = DoublyLinkList()
    doubly.insertNode.insertAtStart("Pikachu")
    doubly.insertNode.insertAtEnd(5)
    doubly.insertNode.insertAtEnd(6)
    doubly.insertNode.insertAtPosition(24, 1)
    doubly.insertNode.insertAtEnd(0)
    doubly.printLinkList()
    doubly.deleteNode.deleteFromPosition(2)
    doubly.printLinkList()


if __name__ == "__main__":
    main()
