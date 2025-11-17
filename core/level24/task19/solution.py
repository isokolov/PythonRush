from requests_html import HTMLSession
import time
import hashlib

# Функция для создания сессии и рендеринга страницы
def create_session():
    return HTMLSession()

# Функция для получения содержимого страницы по URL
def fetch_page_content(session, url):
    response = session.get(url)
    response.html.render()
    return response.html.html

# Функция для вычисления хеша содержимого страницы
def compute_content_hash(content):
    return hashlib.md5(content.encode('utf-8')).hexdigest()

# Функция для сохранения нового содержимого страницы в файл
def save_content_to_file(content, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Новое содержимое сохранено в {filename}.")

# Функция для проверки изменения контента страницы
def is_content_changed(current_hash, previous_hash):
    return current_hash != previous_hash

# Функция для мониторинга веб-страницы на наличие изменений
def monitor_website(session, url, check_interval, output_file):
    previous_content_hash = ''

    while True:
        # Получаем текущий контент страницы
        current_content = fetch_page_content(session, url)

        # Вычисляем хеш текущего контента
        current_content_hash = compute_content_hash(current_content)

        # Проверяем, изменился ли контент страницы
        if is_content_changed(current_content_hash, previous_content_hash):
            save_content_to_file(current_content, output_file)
            previous_content_hash = current_content_hash
        else:
            print("Изменений в содержимом не обнаружено.")

        # Ждем заданный интервал перед следующей проверкой
        time.sleep(check_interval)

# Главная функция, которая подготавливает данные для мониторинга
def main():
    url_to_monitor = 'https://example.com'  # URL веб-страницы для мониторинга
    interval = 60  # Интервал проверки в секундах
    output_filename = 'new_content.html'

    session = create_session()
    monitor_website(session, url_to_monitor, interval, output_filename)

# Запуск основной функции
main()
