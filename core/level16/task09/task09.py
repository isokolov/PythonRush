# Хеш-таблица

# Напишите класс для реализации хеш-таблицы.
# Ваш класс должен включать методы для вставки и получения элементов.
# Возможность коллизии хеш-функции можно не учитывать.

# Напишите тут ваш код


class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * self.size

    def _hash(self, key):
        # Напишите тут ваш код
        return hash(key) % self.size

    def insert(self, key, value):
        # Напишите тут ваш код
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = [(key,value)]
        else:
            for i,kv in enumerate(self.table[index]):
                k,v = kv
                if k == key:
                    self.table[index][i] == (key,value)
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
# Пример использования
ht = HashTable()
ht.insert("apple", 1)
ht.insert("banana", 2)
print(ht.get("apple"))  # Output: 1
print(ht.get("banana"))  # Output: 2
print(ht.get("cherry"))  # Output: None
