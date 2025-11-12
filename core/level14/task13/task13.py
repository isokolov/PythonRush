# Использование объекта Future

# Напишите программу, которая создает объект Future и устанавливает для него результат через 3 секунды.
# Используйте метод set_result для установки результата и выведите результат объекта Future после его завершения.

# Напишите тут ваш код
import asyncio


async def set_fut_res(fut, delay=3):
    await asyncio.sleep(3)
    fut.set_result("Fut result.")


async def main():
    loop = asyncio.get_running_loop()
    fut = loop.create_future()
    asyncio.create_task(set_fut_res(fut))
    res = await fut
    print(res)


asyncio.run(main())
