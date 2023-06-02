# Single Node
class SingleNode:
    def __init__(self, value):
        self.value = value
        self.next_address: int or None = None


# Block of nodes
block_size = 2


class UnrolledLinkListBlockNode:
    def __init__(self):
        self.block_head: SingleNode or None = None  # Head of inner nodes
        self.next_address: int or None = None
        self.node_count: int = 0
