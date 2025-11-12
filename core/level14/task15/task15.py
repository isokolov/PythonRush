# Асинхронный контекстный менеджер

# Напишите асинхронный контекстный менеджер, который будет печатать сообщения при входе и выходе из контекста.
# Внутри контекста выполните асинхронную задержку на 2 секунды и выведите сообщение "Внутри контекста".

# Напишите тут ваш код
import asyncio


class AsyncContext:
    async def __aenter__(self):
        print("Enter in manager!")
        return self

    async def __aexit__(self, exc_type, exc, tb):
        print("Exit from manager!")


async def main():
    async with AsyncContext():
        await asyncio.sleep(2)
        print("Внутри контекста")


asyncio.run(main())
