# Лига Плюща

# Напишите программу, которая создает словарь с информацией о студенте (имя, возраст, университет).
# Программа должна:
# Проверить наличие значения "MIT" с использованием метода values().
# Проверить наличие значения "Harvard" с использованием функции set().
# Проверить наличие значения 22 с использованием генератора.

# Напишите тут ваш код
student = {"name": "Jay", "age": 22, "university": "Harvard"}
print("MIT" in student.values())
print("Harvard" in set(student.values()))

if any(value == 22  for value in student.values()):
    print(f"Значение {student.get("age")} присутствует в словаре.")
else:
    print(f"Значение {student.get("age")} отсутствует в словаре.")
