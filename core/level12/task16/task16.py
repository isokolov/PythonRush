# Сериализация с помощью yaml

# Напишите программу, которая сериализует и десериализует объект Python с использованием модуля yaml.
# Объектом для сериализации будет словарь, содержащий информацию о фильме: название, режиссёр и год выпуска.

# Напишите тут ваш код
import yaml

# Пример словаря с информацией о фильме
film_info = {
    'название': 'Inception',
    'режиссёр': 'Christopher Nolan',
    'год выпуска': 2010
}

# Напишите тут ваш код
yaml_string = yaml.dump(film_info)
print(yaml_string)

loaded_data = yaml.load(yaml_string, Loader=yaml.FullLoader)
print(loaded_data)
