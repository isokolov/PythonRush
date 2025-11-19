# Очередь это просто
# Напишите программу, которая реализует очередь и демонстрирует ее основные свойства:
# FIFO (First In, First Out), операции enqueue, dequeue, и peek.
# Класс list использовать можно.

class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def enqueue(self, item):
        return self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None


# Демонстрация работы
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.peek()  # Front item: 1
q.dequeue()  # Dequeued: 1
q.dequeue()  # Dequeued: 2
q.peek()  # Front item: 3
q.dequeue()  # Dequeued: 3
q.dequeue()  # Queue is empty
