# Обработка исключений Future

# Напишите программу, которая создает объект Future и устанавливает для него исключение через 2 секунды.
# Используйте метод set_exception для установки исключения и обработайте это исключение после его возникновения.

# Напишите тут ваш код
import asyncio


async def set_fut_res(fut, delay=2):
    await asyncio.sleep(delay)
    fut.set_exception(ValueError("Fut exception."))


async def main():
    loop = asyncio.get_running_loop()
    fut = loop.create_future()
    asyncio.create_task(set_fut_res(fut))
    try:
        res = await fut
    except ValueError as e:
        print(f"Huston we have exception - {e}")


asyncio.run(main())
