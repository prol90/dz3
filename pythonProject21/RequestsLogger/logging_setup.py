import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
success_logger = logging.getLogger('success_responses')
bad_logger = logging.getLogger('bad_responses')
blocked_logger = logging.getLogger('blocked_responses')

# Создание файлов для логирования
success_handler = logging.FileHandler('success_responses.log')
bad_handler = logging.FileHandler('bad_responses.log')
blocked_handler = logging.FileHandler('blocked_responses.log')

# Установка уровней логирования для файлов
success_handler.setLevel(logging.INFO)
bad_handler.setLevel(logging.INFO)
blocked_handler.setLevel(logging.INFO)

# Форматирование логов
formatter = logging.Formatter('%(asctime)s - %(message)s')
success_handler.setFormatter(formatter)
bad_handler.setFormatter(formatter)
blocked_handler.setFormatter(formatter)

# Добавление обработчиков к логгерам
success_logger.addHandler(success_handler)
bad_logger.addHandler(bad_handler)
blocked_logger.addHandler(blocked_handler)
