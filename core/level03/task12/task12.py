# Оценщик

# Напишите программу, которая запрашивает у пользователя количество набранных баллов и выводит его оценку по следующей шкале:
# 90 и выше: "Отлично"
# 75-89: "Хорошо"
# 50-74: "Удовлетворительно"
# Менее 50: "Неудовлетворительно"
# Используйте оператор if elif else.

# Напишите тут ваш код
number = int(input("Enter your score: "))
if number >= 90:
    print("Отлично")
elif number >= 75 and number <= 89:
    print("Хорошо")
elif number >= 50 and number <= 74:
    print("Удовлетворительно")
else:
    print("Неудовлетворительно")