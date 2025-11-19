# Хеш-таблица без коллизий

# Напишите класс для реализации хеш-таблицы с использованием цепочек (chaining).
# Ваш класс должен включать методы для вставки и получения элементов.
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

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        # Напишите тут ваш код
        index = self._hash_function(key)
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
        index = self._hash_function(key)
        if self.table[index] is None:
            return None
        for k,v in self.table[index]:
            if k == key:
                return v
        return None

    def test(self):
        self.insert('apple', 1)
        self.insert('banana', 2)
        self.insert('grape', 3)
        self.insert('apple', 4)

        print(self.get('apple'))  # Output: 4
        print(self.get('banana'))  # Output: 2
        print(self.get('grape'))  # Output: 3
        print(self.get('pear'))  # Output: None


ht = HashTable(10)
ht.test()
# ht.insert('apple', 1)
# ht.insert('banana', 2)
# ht.insert('grape', 3)
# ht.insert('apple', 4)
#
# print(ht.get('apple'))   # Output: 4
# print(ht.get('banana'))  # Output: 2
# print(ht.get('grape'))   # Output: 3
# print(ht.get('pear'))    # Output: None
