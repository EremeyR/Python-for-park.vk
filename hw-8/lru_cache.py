"""Simple LRUCache implementation"""


class LRUCache:
    """Simple LRUCache class"""
    class Node:
        """Node for doubly linked list"""
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.__prev = None
            self.__next = None

        @property
        def prev(self):
            """previous node getter"""
            return self.__prev

        @prev.setter
        def prev(self, node):
            """previous node setter"""
            self.__prev = node

        @property
        def next(self):
            """next node getter"""
            return self.__next

        @next.setter
        def next(self, node):
            """next node setter"""
            self.__next = node

    def __init__(self, limit=42):
        self.limit = limit
        self.size = 0

        self.dict = {}

        self.head = None
        self.tail = None

    def get(self, key):
        """LRUCache getter"""
        result_node = self.dict.get(key)
        if result_node:
            self.__rewrite(result_node.key, result_node.value)
            return result_node.value

        return None

    def set(self, key, value):
        """LRUCache setter"""
        if not self.dict.get(key):
            self.__add(key, value)
            # self.size += 1
        else:
            self.__rewrite(key, value)

        if self.size > self.limit:
            self.__del_last()
            # self.size -= 1

    def __add(self, key, value):
        if self.size == 0:
            self.head = self.Node(key, value)
            self.tail = self.head
        elif self.size == 1:
            self.head = self.Node(key, value)
            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            old_head = self.head
            self.head = self.Node(key, value)
            self.head.next = old_head
            old_head.prev = self.head

        self.dict[key] = self.head
        self.size += 1

    def __rewrite(self, key, value):
        old_node = self.dict[key]
        if old_node.next:
            old_node.next.prev = old_node.prev
        else:
            self.tail = old_node.prev

        if old_node.prev:
            old_node.prev.next = old_node.next
        else:
            self.head = old_node.next

        self.size -= 1

        self.__add(key, value)

    def __del_last(self):
        self.dict.pop(self.tail.key)
        self.tail.prev.next = None
        self.tail = self.tail.prev

        self.size -= 1
