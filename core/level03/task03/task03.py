# Рост в футах и дюймах

# Напишите программу, которая переводит рост пользователя, заданный в сантиметрах, в футы и дюймы.
# Значение роста задано в переменной height_cm. Один дюйм равен 2.54 см, один фут равен 12 дюймам.
# Ваша задача — вычислить количество полных футов в данном росте и остаток перевести в дюймы.
# Результат выведите на экран.

height_cm = float(input("Введите рост в сантиметрах: "))

# Константы
cm_per_inch = 2.54
inch_per_foot = 12

# Напишите тут ваш 
height_foot = height_cm // (2.54 * 12)
# print(height_foot)
rest_inch = (height_cm - height_foot * 2.54 * 12) // 2.54
print(round(height_foot,0), round(rest_inch, 2))