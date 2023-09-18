class DoubleLinkedList:
    def _init_(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_head(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def delete_head(self):
        if not self.head:
            print("NO HAY CABEZAA")
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self.size -= 1

    def delete_tail(self):
        if not self.tail:
            print("NO HAY COLA")
            return

        if self.tail == self.head:
            self.tail = None
            self.head = None

        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.size -= 1

    def delete_ab_pos(self, pos):

        if pos == 0:
            self.delete_head()
            return

        current = self.head
        i = 0

        while current and i < pos:
            current = current.next
            i += 1

        if current == self.tail:
            self.delete_tail()
            return

        current.prev.next = current.next
        current.next.prev = current.prev

        self.size -= 1

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value, end="")
            current = current.next


class Node:
    def _init_(self, value):
        self.value = value
        self.next = None
        self.prev = None
