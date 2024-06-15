import requests
from logging_setup import success_logger, bad_logger, blocked_logger

# Список сайтов для проверки
websites = [
     'https://www.youtube.com/'
     'https://wikipedia.org',
     'https://yahoo.com',
     'https://yandex.ru',
     'https://whatsapp.com',
]

# Функция для проверки сайтов
def check_website(url):
    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:

            success_logger.info(f"Successful response from {url}")
        else:

            bad_logger.info(f"Bad response from {url} with status code {response.status_code}")
    except requests.exceptions.RequestException as e:

        blocked_logger.info(f"Failed to connect to {url}: {e}")


# Проверка каждого сайта из списка
for website in websites:
    check_website(website)

