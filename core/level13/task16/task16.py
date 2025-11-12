# Отправка почты с использованием SMTP
import smtplib

# Напишите программу, которая подключается к SMTP-серверу, аутентифицируется и отправляет письмо.

# Напишите тут ваш код

smtp_server = 'smtp.gmail.com'
smtp_port = 587
user = 'em@gmail.com'
passw = 'pass'

from_ = 'your_email@gmail.com'
to_ = 'rec_email@gmail.com'

subj = 'Theme'
body = 'Email_text'

message = f"From: {from_}\nTo: {to_}\nSubject: {subj}\n\n{body}"

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    server.login(user, passw)
    server.sendmail(from_, to_, message)
    print("Good")
except Exception as e:
    print(f"Error {e}")
finally:
    server.quit()
