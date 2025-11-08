# Преобразование данных.

# Напишите функцию convert_and_sum, которая принимает два аргумента в виде строк,
# преобразует их в целые числа и возвращает их сумму.
# Обработайте исключения, которые могут возникнуть при преобразовании строк в числа
# (например, если переданы некорректные значения).

# Напишите тут ваш код
def convert_and_sum(str1, str2):
    try:
        a = int(str1)
        b = int(str2)
        result = a + b
        return result
    except TypeError:
        return "Wrong type values"
    except ValueError:
        return "Некорректное значение"

print(convert_and_sum(3, 5))
print(convert_and_sum(3, 'a'))
print(convert_and_sum('3', '5'))
