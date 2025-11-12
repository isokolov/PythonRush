# Использование прокси-сервера с модулем http.client

# Напишите программу, которая отправляет GET-запрос через прокси-сервер с использованием библиотеки http.client.

# Напишите тут ваш код
import http.client

proxy_host = '11.12.2.12'
proxy_port = 8000

conn = http.client.HTTPConnection(proxy_host,proxy_port)

dest_url = 'httpbin.org'
dest_path = '/ip'


conn.set_tunnel(dest_url)
conn.request('GET', dest_path)

resp = conn.getresponse()
print(resp.status, resp.reason)
print(resp.read().decode('utf-8'))
conn.close()
