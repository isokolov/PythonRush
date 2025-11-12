# Асинхронное программирование

# Напишите асинхронную программу, которая выполняет 30 задач параллельно.
# Каждая задача должна ожидать 2 секунды и затем выводить своё сообщение "Task n done", где n - номер задачи.
# Используйте модуль asyncio.

# Напишите тут ваш код
import asyncio


async def worker(n):
    await asyncio.sleep(2)
    print(f"Task {n} done")


async def main():
    async with asyncio.TaskGroup() as tg:
        for n in range(1, 31):
            tg.create_task(worker(n))


asyncio.run(main())
