# Создание и получение цикла событий

# Напишите программу, которая создает новый цикл событий, устанавливает его как текущий и печатает его.
# Затем создайте еще один новый цикл событий и снова установите его как текущий.
# Убедитесь, что вы правильно меняете циклы событий.

# Напишите тут ваш код
import asyncio

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
print(asyncio.get_event_loop())

new_loop = asyncio.new_event_loop()
asyncio.set_event_loop(new_loop)
print(asyncio.get_event_loop())

loop.close()
new_loop.close()
