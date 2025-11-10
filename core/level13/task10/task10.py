# Выполнение POST-запроса с использованием http.client

# Напишите программу, которая выполняет POST-запрос на сервер с передачей данных и выводит ответ.
# Программа должна обрабатывать возможные ошибки.

# Напишите тут ваш код
import http.client
import json

dat = json.dumps({"k1": 1,
                  "k2": 2
                  })
head = {
    'Content-Type': 'application/json'
}

try:
    conn = http.client.HTTPConnection("httpbin.org")
    conn.request("POST", '/', body=dat, headers=head)

    res = conn.getresponse()
    t_res = res.read().decode('utf-8')
    print(t_res)
except Exception as e:
    print(f"More errors")
finally:
    conn.close()
