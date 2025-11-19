# Двусвязный список

# Напишите программу, которая реализует двусвязный список с методами добавления, удаления и поиска элементов.
# Добавьте несколько элементов в список, удалите один из них и найдите элемент по значению.

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        # Write your code here
        new_node = Node(value)
        if not self.head:
            self.head, self.tail = new_node, new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def remove(self, value):
        # Write your code here
        if not self.head:
            return False

        cur = self.head
        while cur:
            if cur.value == value:
                if cur.prev is None and cur.next is None:
                    self.head = self.tail = None
                elif cur.prev is None:
                    self.head = cur.next
                    self.head.prev = None
                elif cur.next is None:
                    self.tail = cur.prev
                    self.tail.next = None
                else:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                return True
            cur = cur.next
        return False

    def find(self, value):
        # Write your code here
        cur = self.head

        while cur is not None:
            if cur.value == value:
                return cur
            cur = cur.next
        return None

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        return elements


# Demonstration of work
dll = DoublyLinkedList()
dll.add(1)
dll.add(2)
dll.add(3)
print("Список після додавання елементів:", dll.display())
dll.remove(2)
print("Список після видалення елемента 2:", dll.display())
result = dll.find(3)
print("Пошук елемента 3:", result.value if result else "Не знайдено")
