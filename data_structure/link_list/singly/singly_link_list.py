# Imports
from link_list.singly.Node import Node
import logging

logging.basicConfig(
    filename="singly_list.log",
    format='%(asctime)s %(levelname)s:%(message)s',
    filemode='w',
    level=logging.DEBUG
)

logger = logging.getLogger(__name__)


# Singly link list
class SinglyLinkList:
    def __init__(self):
        self.length: int = 0
        self.head: Node or None = None
        # self.tail: Node = None

    class InsertNode:
        def __init__(self):
            pass

    def insertAtBeginning(self, data):
        new_node = self._getDataNode(data)
        if self.length: new_node.setDataPointer(self.head)
        self.head = new_node
        self._nodeAdded()

    def _nodeAdded(self):
        self.length += 1
        logger.info("New Node added")

    def _nodeDeleted(self):
        self.length -= 1
        logger.info("Node removed Successfully")

    def insertDataInPosition(self, data, position) -> None:
        new_node = self._getDataNode(data)
        count, current = 0, self.head
        while count < position - 1: count += 1; current = current.getDataPointer()
        new_node.setDataPointer(current.getDataPointer())
        current.setDataPointer(new_node)
        self._nodeAdded()

    def insertInPosition(self, data, position) -> None:
        invalid_position = position > self.length or position < 0
        if invalid_position: return None
        if not position:
            self.insertAtBeginning(data)
        elif position == self.length:
            self.insertAtEnd(data)
        else:
            self.insertDataInPosition(data, position)

    def insertAtEnd(self, data) -> None:
        new_node = self._getDataNode(data)
        current = self.head
        while current.getDataPointer() is not None: current = current.getDataPointer()
        current.setDataPointer(new_node)
        self._nodeAdded()

    def deleteFromBeginning(self):
        if not self.length: logger.info("Linked list is empty"); return
        self.head = self.head.getDataPointer()
        self._nodeDeleted()

    def deleteFromEnd(self):
        current = self.head
        count = 1
        while count < self.length: current = current.getDataPointer(); count += 1
        current.setDataPointer(None)
        self._nodeDeleted()

    # Delete Node by position
    def deleteByPosition(self, position):
        current = self.head
        count = 1
        while count < position: current = current.getDataPointer(); count += 1
        current.setDataPointer(current.getDataPointer().getDataPointer())
        self._nodeDeleted()

    # Delete Node by value
    def deleteByValue(self, value):
        current = self.head
        previous = self.head
        while current.getDataPointer() is not None:
            if current.getData() is value:
                previous.setDataPointer(current.getDataPointer())
                self._nodeDeleted()
                return
            else:
                previous = current
                current = current.getDataPointer()
        logger.warning("Value is not present")

    # Delete By node itself
    def deleteByNode(self, node: Node):
        current = self.head
        previous = self.head
        count = 0
        while count < self.length:
            if current != node:
                previous = current
                current = current.getDataPointer()
            else:
                previous.setDataPointer(current.getDataPointer())
                self._nodeDeleted()
                break
            count += 1

    def deleteList(self):
        self.head = None
        self.length = 0

    @staticmethod
    def _getDataNode(data) -> Node:
        return Node(data=data)


if __name__ == "__main__":
    logger.info("Running the Singly link list")
    single_link_list = SinglyLinkList()
    single_link_list.insertAtBeginning("First Node")
    logger.info("Node value is: "+single_link_list.head.getData())
