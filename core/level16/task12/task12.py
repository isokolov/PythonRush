# Хеш-таблица на цепочках

# Напишите класс для реализации хеш-таблицы с использованием цепочек (chaining).
# Ваш класс должен включать методы для вставки, получения, поиска и удаления элементов.
# Также напишите функцию для демонстрации работы хеш-таблицы.
# Возможную коллизию хеш-функции нужно решить методом цепочек.

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        # Напишите тут ваш код
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = [(key,value)]
        else:
            for i, kv in enumerate(self.table[index]):
                k, v = kv
                if k == key:
                    self.table[index][i] = (key,value)
                    return
            self.table[index].append((key,value))

    def get(self, key):
        # Напишите тут ваш код
        index = self._hash(key)
        if self.table[index] is None:
            return None
        for k,v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        # Напишите тут ваш код
        index = self._hash(key)
        if self.table[index] is None:
            return
        for i, kv in enumerate(self.table[index]):
            k,v = kv
            if k == key:
                del self.table[index][i]
                return

    def search(self, key):
        # Напишите тут ваш код
        index = self._hash(key)
        if self.table[index] is None:
            return False
        for k,v in self.table[index]:
            if k == key:
                return True
        return False

def demo():
    ht = HashTable(10)
    ht.insert("key1", "value1")
    ht.insert("key2", "value2")
    ht.insert("key3", "value3")

    print("Get key1:", ht.get("key1"))  # Output: value1
    print("Get key2:", ht.get("key2"))  # Output: value2
    print("Get key4:", ht.get("key4"))  # Output: None

    print("Exists key1:", ht.search("key1"))  # Output: True
    print("Exists key4:", ht.search("key4"))  # Output: False

    print("Delete key1:", ht.delete("key1"))  # Output: True
    print("Get key1 after delete:", ht.get("key1"))  # Output: None

    ht.insert("key1", "value1_new")
    print("Get key1 after reinsert:", ht.get("key1"))  # Output: value1_new

demo()
