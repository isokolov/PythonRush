# Отступник на максималках

#Исправьте отступы в следующем коде, чтобы он корректно выводил статус в зависимости от количества набранных баллов.

score = int(input("Введите количество набранных баллов: "))
if score >= 90:
    print("Отлично")
else:
    if score >= 75 and score < 90:
        print("Хорошо")
    else:
        if score >= 50 and score < 75:
            print("Удовлетворительно")
        else:
            if score < 50:
                print("Неудовлетворительно")