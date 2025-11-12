# АКМ для работы с файлами

# Используйте библиотеку aiofiles для создания асинхронного контекстного менеджера,
# который будет открывать файл, записывать в него строку "Асинхронная запись в файл" и закрывать файл.

# Напишите тут ваш код
import asyncio
import aiofiles


async def main():
    async with aiofiles.open("ex.txt", mode='w') as file:
        await file.write("Асинхронная запись в файл")


asyncio.run(main())
