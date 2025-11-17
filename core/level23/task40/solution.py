import requests
from bs4 import BeautifulSoup
import csv
import logging
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Логирование
logging.basicConfig(filename='scraper.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Настройка HTTP сессии с повторными попытками
session = requests.Session()
retry = Retry(total=5, backoff_factor=0.1, status_forcelist=[500, 502, 503, 504])
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)


# Функция для извлечения данных из таблицы
def extract_table_data(soup):
    table = soup.find('table')
    data = []
    if not table:
        logging.warning('No table found on page')
        return data

    headers = [header.text.strip() for header in table.find_all('th')]
    rows = table.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        if cols:
            data.append([col.text.strip() for col in cols])

    return [headers, data]

# Запись данных в CSV
def write_to_csv(filename, headers, data_rows):
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if headers:
            writer.writerow(headers)
        writer.writerows(data_rows)

# Основная функция скрейпинга
def scrape_website(base_url, num_pages):
    csv_file = 'scraped_data_csv'
    for page in range(1, num_pages + 1):
        try:
            url = f"{base_url}/page/{page}"
            response = session.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')

            headears, data_rows = extract_table_data(soup)

            if data_rows:
                write_to_csv(csv_file, headears if page == 1 else None, data_rows)

            logging.info(f"Successfully scraped page {page}")

        except requests.exceptions.HTTPError as errh:
            logging.error(f"HTTP Error: {errh} on page {page}")
        except requests.exceptions.ConnectionError as errc:
            logging.error(f"Error Connecting: {errc} on page {page}")
        except requests.exceptions.Timeout as errt:
            logging.error(f"Timeout Error: {errt} on page {page}")
        except requests.exceptions.RequestException as err:
            logging.error(f"An unexpected error occurred: {err} on page {page}")

            # Пауза между запросами
        time.sleep(1)


BASE_URL = 'http://example.com'  # замените на URL вашего сайта
NUM_PAGES = 5  # количество страниц для скрейпинга
scrape_website(BASE_URL, NUM_PAGES)
