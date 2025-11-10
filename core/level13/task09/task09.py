# Выполнение GET-запроса с использованием http.client

# Напишите программу, которая выполняет GET-запрос на сервер, читает и выводит ответ.
# Программа должна обрабатывать возможные ошибки.

# Напишите тут ваш код
import http.client

try:
    conn = http.client.HTTPConnection("google.com")
    conn.request("GET", '/')

    res = conn.getresponse()
    t_res = res.read().decode('utf-8')
    print(t_res)
except http.client.HTTPException as e:
    print(f"Error as {e}")
except Exception as e:
    print(f"More errors")
finally:
    conn.close()
