# Timezone.

# Напишите программу, которая конвертирует текущее время из часового пояса UTC в заданный пользователем часовой пояс.
# Программа должна:
# Получить текущее время в часовом поясе UTC.
# Запросить у пользователя смещение в часах относительно UTC.
# Создать объект часового пояса с заданным смещением.
# Конвертировать текущее время в заданный часовой пояс.
# Вывести текущее время в UTC и в заданном часовом поясе.

# Напишите тут ваш код
import datetime

current_time = datetime.datetime.now(datetime.timezone.utc)
time_delta_utc = int(input('Time Delta UTC: '))
future_tz = datetime.timezone(datetime.timedelta(hours=time_delta_utc))
future_time = current_time.astimezone(future_tz)

print(current_time)
print(future_time)