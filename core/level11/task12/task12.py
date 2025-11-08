# Перегрузка операторов индексации

# Напишите класс Matrix, который будет представлять двумерную матрицу и поддерживать перегрузку операторов индексации ([]).
# Реализуйте методы __getitem__ и __setitem__.

class Matrix:

# Write your code here
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __getitem__(self, key):
        row, col = key
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            raise IndexError("Index out of range")
        return self.data[row][col]

    def __setitem__(self, key, value):
        row, col = key
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            raise IndexError("Index out of range")
        self.data[row][col] = value

# Example usage:
matrix = Matrix(3, 3)
matrix[0, 0] = 1
print(matrix[0, 0])  # Вивід: 1
    # def __init__(self, key):
    #     self.h = key[0]
    #     self.w = key[1]
    #     self.data = [[0 for _ in range(key[1])] for _ in range(key[0])]
    #
    # def __getitem__(self, key):
    #     if key[0] >= self.h or key[1] >= self.w:
    #         raise IndexError
    #     return self.data[key[0]][key[1]]
    #
    # def __setitem__(self, key, val):
    #     if key[0] >= self.h or key[1] >= self.w:
    #         raise IndexError
    #     self.data[key[0]][key[1]] = val


# Напишите тут ваш код


# Пример использования
# matrix = Matrix(3, 3)
# matrix[0, 0] = 1
# print(matrix[0, 0])  # Вывод: 1
