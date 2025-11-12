# Чтение почты с POP3-сервера

# Напишите программу, которая подключается к POP3-серверу, аутентифицируется,
# получает список писем и отображает содержимое последнего письма.

# Напишите тут ваш код
import poplib

username = "your_email@example.com"
password = "pass"

pop3_server = 'pop.gmail.com'
m_b = poplib.POP3_SSL(pop3_server, 995)

m_b.user(username)
m_b.pass_(password)

messages = m_b.list()

if len(messages[1]) > 0:
    resp, lines, octets = m_b.retr(len(messages[1]))
    message = '\n'.join(line.decode('utf-8') for line in lines)
    print(message)

m_b.quit()
