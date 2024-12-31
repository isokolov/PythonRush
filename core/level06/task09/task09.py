# Котовасия

# Напиши программу, которая хранит множество из 5 самых популярных имен котов.
# Пользователь должен пытаться угадать их. Когда он угадывает имя кота, оно удаляется из множества.
# Цель игры - угадать всех котов за как можно меньшее число попыток.

# Напишите тут ваш
cats_set = {'Mursik', 'Vaska', 'Murka', 'Chuck', 'Mars'}
count_guesses = 0
while not len(cats_set) == 0:
    your_guess = input("Guess a cat's name? ")
    count_guesses += 1
    if your_guess in cats_set:
        cats_set.remove(your_guess)
print(count_guesses)