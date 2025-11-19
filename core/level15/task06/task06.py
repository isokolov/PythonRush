# Стек это не так уж и просто

# Напишите программу, которая реализует стек и демонстрирует его основные свойства:
# LIFO (Last In, First Out), операции push, pop, и peek.

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def push(self, elem):
        return self.items.append(elem)

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    # Напишите тут ваш код


# Демонстрация работы стека
stack = Stack()
print("Стек пуст:", stack.is_empty())

stack.push(1)
stack.push(2)
stack.push(3)
print("Верхний элемент стека:", stack.peek())

print("Выталкивание элемента:", stack.pop())
print("Выталкивание элемента:", stack.pop())
print("Верхний элемент стека:", stack.peek())

print("Стек пуст:", stack.is_empty())
print("Выталкивание элемента:", stack.pop())
print("Стек пуст:", stack.is_empty())
