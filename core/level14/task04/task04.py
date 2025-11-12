# Выполнение нескольких задач параллельно

# Напишите программу, которая использует asyncio.gather() для выполнения нескольких асинхронных задач параллельно
# и собирает их результаты.

# Напишите тут ваш код
import asyncio

async def task1(a, b):
    await asyncio.sleep(1)
    return a + b

async def task2(a, b):
    await asyncio.sleep(2)
    return a * b

async def main():
    results = await asyncio.gather(task1(5, 10), task2(5, 5))
    print(results)

asyncio.run(main())
