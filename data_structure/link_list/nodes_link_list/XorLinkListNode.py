# to get address of variable we use 'id(variable)' in python
"""
    TO get value from address
    suppose bag = 45
    address of bag = id(45)
    address = id(45)
    -----------------------
    value from address
    import ctype
    bag_value = ctypes.cast(address, ctypes.py_object).value
"""


class XorLinkListNode:
    def __init__(self, value):
        self.value = value
        self.npx = 0            # Xor of previous and next address

