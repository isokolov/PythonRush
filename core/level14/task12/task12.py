# Отмена задачи

# Напишите асинхронную программу, которая создает задачу, выполняющую ожидание 5 секунд.
# Запустите её, подождите 1 секунду, затем отмените задачу и выведите сообщение о её отмене.
# Обработайте исключение CancelledError.

# Напишите тут ваш код
import asyncio


async def main():
    task_1 = asyncio.create_task(asyncio.sleep(5))
    await asyncio.sleep(1)
    task_1.cancel()
    try:
        await task_1
    except asyncio.CancelledError:
        print("It was cancelled.")


asyncio.run(main())
