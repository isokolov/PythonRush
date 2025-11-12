# Асинхронный генератор

# Напишите асинхронный генератор, который будет генерировать числа от 0 до 2 с задержкой в 1 секунду между числами.
# Используйте этот генератор в асинхронной функции, чтобы вывести значения на экран.

# Напишите тут ваш код
import asyncio


async def async_gen():
    for i in range(3):
        await asyncio.sleep(1)
        yield i


async def main():
    async for value in async_gen():
        print(value)


asyncio.run(main())
