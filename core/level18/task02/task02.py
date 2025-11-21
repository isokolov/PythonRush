# Снежинка Коха

# Напишите рекурсивный алгоритм для рисования снежинки Коха.
# Алгоритм должен использовать библиотеку turtle для рисования фрактальной кривой.

import turtle

def koch_curve(t, order, size):
# Напишите тут ваш код

def koch_snowflake(t, order, size):
# Напишите тут ваш код


screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

order = 3  # глубина фрактала
size = 300  # Сторона

koch_snowflake(t, order, size)

t.hideturtle()
screen.mainloop()
