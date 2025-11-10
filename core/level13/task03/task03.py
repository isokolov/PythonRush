# Использование энкодера

# Напишите программу, которая сериализует объект Python, содержащий дату и время, в JSON-строку
# с использованием пользовательского кодера для преобразования объектов datetime в строковый формат ISO.

# Напишите тут ваш код
import json
from datetime import datetime, timezone


class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        return super().default(o)


data = {
    "event": "Start",
    "timestamp": datetime(2020, 1, 1, 12, 0, tzinfo=timezone.utc)
}

json_str = json.dumps(data, cls=CustomEncoder, ensure_ascii=False, indent=4)
print(json_str)
