# Метод sleep()

# Напишите асинхронную функцию, которая принимает строку и задержку в секундах, затем выводит строку после указанной задержки.
# Создайте две задачи, каждая из которых вызывает эту функцию с разными строками и задержками.
# Запустите их одновременно, используя метод asyncio.run().

# Напишите тут ваш код
import asyncio

str_ = input("Your string: ")
delay_ = int(input("Enter your delay: "))


async def task1(user_str, user_delay):
    await asyncio.sleep(user_delay)
    print(user_str)


async def main():
    str_ = "First_String"
    delay_ = 2
    str_2 = "Second_String"
    delay_2 = 3
    task_1 = asyncio.create_task(task1(str_, delay_))
    task_2 = asyncio.create_task(task1(str_2, delay_2))
    done, pending = await asyncio.wait([task_1, task_2])
    for task in done:
        print(task.result())


asyncio.run(main())
