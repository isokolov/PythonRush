# Использование Future

# Напишите асинхронную функцию, которая принимает объект Future
# и устанавливает для него результат после задержки в 1 секунду.
# Создайте цикл событий, объект Future и используйте функцию для установки результата.
# Затем выведите результат Future на экран.

# Напишите тут ваш код
import asyncio

async def set_future(fut: asyncio.Future, value):
    await asyncio.sleep(1)
    fut.set_result(value)

async def main():
    loop = asyncio.get_running_loop()
    fut = loop.create_future()
    await set_future(fut, "Hello bro")
    print(fut.result())

asyncio.run(main())
