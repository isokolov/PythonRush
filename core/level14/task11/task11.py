# Управление циклом событий

# Напишите асинхронную программу, которая создает две задачи.
# Первая задача должна печатать "Первая задача" и ждать 2 секунды,
# вторая задача должна печатать "Вторая задача" и ждать 3 секунды.
# Используйте asyncio.create_task() для создания задач и выполните их параллельно, дождавшись завершения обеих.

# Напишите тут ваш код
import asyncio


async def task1():
    print("Первая задача")
    await asyncio.sleep(2)


async def task2():
    print("Вторая задача")
    await asyncio.sleep(3)


async def main():
    task_1 = asyncio.create_task(task1())
    task_2 = asyncio.create_task(task2())
    await task_1
    await task_2


asyncio.run(main())
