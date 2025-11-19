# Сумма чисел

# Дан массив чисел и целевое значение суммы. Необходимо найти все пары чисел, которые в сумме дают целевое значение.

def find_pairs(nums, target):
    # Напишите тут ваш код
    seen = set()
    pairs = []
    for elem in nums:
        tmp_sum = target - elem
        if tmp_sum in seen:
            pairs.append((tmp_sum, elem))
        seen.add(elem)
    return pairs


# Пример использования
nums = [2, 4, 3, 5, 7, 8, 9]
target = 10
print(find_pairs(nums, target))
