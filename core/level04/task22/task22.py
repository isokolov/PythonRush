# Профиль кота

# Напишите функцию create_cat_profile(name: str, age: int, **kwargs: str) -> None, которая принимает имя и возраст кота в качестве обязательных параметров,
# а также произвольное количество именованных параметров (например, порода, цвет и т.д.).
# Функция должна выводить профиль кота, включая все переданные параметры.

# Напишите тут ваш код
def create_cat_profile(name: str, age: int, **kwargs: str) -> None:
    print(f"name : {name}, age: {age}")
    for key, value in kwargs.items():
        print(f"{key}, {value}")


create_cat_profile("Мурзик", 3, порода="Сиамский", цвет="Черный")
create_cat_profile("Барсик", 5, страна="Китай", хобби="Ловить мышей")