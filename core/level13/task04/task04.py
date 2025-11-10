# Использование декодера

# Напишите программу, которая десериализует JSON-строку в объект Python с использованием
# пользовательского декодера для преобразования строк ISO в объекты datetime.

# Напишите тут ваш код
import json
from datetime import datetime


def custom_decoder(dct):
    if 'timestamp' in dct:
        dct['timestamp'] = datetime.fromisoformat(dct['timestamp'])
    return dct


json_str = '''
{
    "event": "Start",
    "timestamp": "2020-01-01T12:00:00+00:00"
}
'''

data = json.loads(json_str, object_hook=custom_decoder)
print(data)
