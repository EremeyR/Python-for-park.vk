"""Simple LRUCache implementation with logging"""


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

    def __init__(self, logger, limit=42):
        self.limit = limit
        self.size = 0

        self.dict = {}

        self.head = None
        self.tail = None

        self.logger = logger

    def get(self, key):
        """LRUCache getter"""
        result_node = self.dict.get(key)
        if result_node:
            self.__rewrite(result_node.key, result_node.value)

            self.logger.info(f"success getting: key: '{key}',"
                             f" value: '{result_node.value}'")
            return result_node.value

        self.logger.info(f"key '{key}' not found")
        return None

    def set(self, key, value):
        """LRUCache setter"""
        if not self.dict.get(key):
            self.__add(key, value)
        else:
            self.__rewrite(key, value)

        if self.size > self.limit:
            self.__del_last()

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

        self.logger.info(f"the value '{value}' for the key '{key}' was added")

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

        self.logger.info(f"the value for the key '{key}'"
                         f" was rewritten to '{value}'")

    def __del_last(self):
        self.dict.pop(self.tail.key)
        self.tail.prev.next = None
        self.tail = self.tail.prev

        self.size -= 1

        self.logger.info("last element was deleted")
