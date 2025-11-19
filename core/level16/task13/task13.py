# Поиск дубликатов

# Дан массив чисел. Необходимо найти и вернуть все дубликаты в массиве.

def find_duplicates(nums):
    set_ = set()
    dups = []
    for elem in nums:
        if elem in set_:
            dups.append(elem)
        else:
            set_.add(elem)
    return dups


# Пример использования:
nums = [1, 2, 3, 2, 4, 5, 6, 3, 7, 8, 1]
print(find_duplicates(nums))  # Output: [2, 3, 1]
