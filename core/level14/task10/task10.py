# Запуск и остановка цикла событий

# Напишите программу, которая запускает цикл событий в бесконечном режиме.
# Запланируйте остановку цикла через 3 секунды, используя метод call_later.
# Публикация состояния запущен ли цикл до и после вызова метода stop().

# Напишите тут ваш код
import asyncio
from asyncio import AbstractEventLoop

def my_callback(loop: AbstractEventLoop):
    print("Callback executed after delay")
    loop.stop()

loop = asyncio.new_event_loop()
loop.call_later(3, my_callback, loop)

print("Loop running?", loop.is_running())
loop.run_forever()
print("Loop running?", loop.is_running())
