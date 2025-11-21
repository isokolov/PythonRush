# Перестановки множества

# Найти все уникальные перестановки элементов заданного множества.
# Подсказка: Используйте рекурсию или итеративные методы для генерации всех возможных упорядоченных комбинаций элементов.



def generate_permutations(elements):
# Напишите тут ваш код


def all_unique_permutations(input_set):
    elements = list(input_set)
    raw_permutations = generate_permutations(elements)
    unique_permutations = []
    for perm in raw_permutations:
        if perm not in unique_permutations:
            unique_permutations.append(perm)
    return unique_permutations

# Пример использования
input_set = {1, 2, 3}
permutations = all_unique_permutations(input_set)
for perm in permutations:
    print(perm)
