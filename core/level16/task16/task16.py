# Общий подмассив

# Даны два массива чисел. Необходимо найти элементы первого массива, которые существуют во втором массиве.



def common_subarray(arr1, arr2):
    set2 = set(arr2)
    sub = []
    for elem in arr1:
        if elem in set2:
            sub.append(elem)
    return sub


# Пример использования
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]

result = common_subarray(arr1, arr2)
print(result)
