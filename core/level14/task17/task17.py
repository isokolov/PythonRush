# Асинхронный итератор

# Напишите асинхронный итератор, который будет возвращать числа от 1 до 5 с задержкой в 1 секунду между числами.
# Используйте этот итератор в асинхронной функции, чтобы вывести числа на экран.

# Напишите тут ваш код
import asyncio


class AsyncIter:
    def __init__(self):
        self.current = 0
        self.end = 5

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current >= self.end:
            raise StopAsyncIteration

        await asyncio.sleep(1)
        self.current += 1
        return self.current


async def main():
    async for number in AsyncIter():
        print(number)


asyncio.run(main())
