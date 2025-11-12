# Создание и выполнение асинхронных функций

# Напишите программу, которая создает и выполняет несколько асинхронных функций,
# каждая из которых использует оператор await для ожидания завершения другой асинхронной функции.

# Напишите тут ваш код
import asyncio

async def async_sum(a, b):
    return a + b

async def async_mul(a, b):
    return a * b

async def main():
    task1 = await async_sum(5, 10)
    task2 = await async_mul(5, 5)
    print("Results:", task1, task2)

asyncio.run(main())

