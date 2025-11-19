# Люблю список еще больше

# Напишите программу, которая создает динамический массив (список)
# и демонстрирует его основные операции: добавление, удаление, доступ по индексу и изменение элемента.
# Класс list использовать нельзя.

class DynamicArray:
    def __init__(self):
        self.array = []

    def add(self, element):
        # Write your code here
        self.array.append(element)

    def remove(self, index):
        # Write your code here
        if len(self.array) == 0:
            raise IndexError("List is empty")
        if index < 0 or index >= len(self.array):
            raise IndexError("Index out of range")
        self.array.pop(index)

    def get(self, index):
        # Write your code here
        if index < 0 or index >= len(self.array):
            raise IndexError("Index out of range")
        return self.array[index]

    def set(self, index, element):
        # Write your code here
        if index < 0 or index >= len(self.array):
            raise IndexError("Index out of range")
        self.array[index] = element

    def __len__(self):
        return len(self.array)

    def __str__(self):
        return str(self.array)


# Приклади використання:
arr = DynamicArray()
arr.add(1)
arr.add(2)
arr.add(3)
print(arr)  # [1, 2, 3]

arr.remove(2)
print(arr)  # [1, 2]

print(arr.get(1))  # 2

arr.set(1, 5)
print(arr)  # [1, 5]

print(len(arr))  # 2
