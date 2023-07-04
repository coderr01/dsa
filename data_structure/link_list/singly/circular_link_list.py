from link_list.singly.singly_link_list import SinglyLinkList
from link_list.singly.Node import Node
import logging

logging.basicConfig(
    # filename="circular_list.log",
    format='%(asctime)s %(levelname)s:%(message)s',
    # filemode='w',
    level=logging.DEBUG
)

logger = logging.getLogger(__name__)


class CircularLinkList:
    def __init__(self):
        self.length = 0
        self.head: Node or None = None
        self.tail: Node or None = None
        self._insertNode = self._InsertNode()
        self._deleteNode = self._DeleteNode()

    @staticmethod
    def _getDataNode(data) -> Node:
        return Node(data=data)

    class _InsertNode:
        def __init__(self, outer_self):
            self._outer: CircularLinkList = outer_self

        def insertAtStart(self, data):
            new_node = CircularLinkList._getDataNode(data)
            if self._outer.length: new_node.setDataPointer(self._outer.head)
            last_node = self._outer.getNodeByPosition(self._outer.length)
            last_node.setDataPointer(new_node)
            self._outer.head = new_node
            self._nodeAdded()

        def insertAtEnd(self, data):
            new_node = CircularLinkList._getDataNode(data)
            current = self._outer.getNodeByPosition(self._outer.length)
            current.setDataPointer(new_node)
            self._nodeAdded()

        def insertDataInPosition(self, data, position) -> None:
            new_node = CircularLinkList._getDataNode(data)
            count, current = 0, self._outer.head
            while count < position - 1: count += 1; current = current.getDataPointer()
            new_node.setDataPointer(current.getDataPointer())
            current.setDataPointer(new_node)
            self._nodeAdded()

        def insertInPosition(self, data, position) -> None:
            invalid_position = position > self._outer.length or position < 0
            if invalid_position: return None
            if not position:
                self.insertAtStart(data)
            elif position == self._outer.length:
                self.insertAtEnd(data)
            else:
                self.insertDataInPosition(data, position)

        def _nodeAdded(self):
            self._outer.length += 1
            logger.info("New Node added")

    def getNodeByPosition(self, position) -> Node or None:
        if not self.length >= position > 0:
            logger.error("Given an invalid position")
            return
        current = self.head
        count = 1
        while count < position:
            current = current.getNext()
            count += 1
        return current

    class _DeleteNode:
        def __init__(self, outer_self):
            self._outer = outer_self

        def _nodeDeleted(self):
            self._outer.length -= 1
            logger.info("Node Deleted")

        def deleteAtStart(self):
            self._outer.head = self._outer.head.getDataPointer() if self._outer.length >= 2 else None
            last_node = self._outer.getNodeByPosition(self._outer.length-1)
            last_node.setDataPointer(self._outer.head)
            self._nodeDeleted()

        def deleteAtEnd(self):
            node = self._outer.getNodeByPosition(self._outer.length-1)
            node.setDataPointer(self._outer.head)
            self._nodeDeleted()

        def deleteAtPosition(self, position):
            node = self._outer.getNodeByPosition(position-1)
            node.setDataPointer(node.getDataPointer().getDataPointer())
            self._nodeDeleted()

