import os
import datetime

def log(text, log_object):
    # Получаем сегодняшнюю дату в формате YYYY-MM-DD
    today_date = datetime.datetime.now().strftime('%Y-%m-%d')

    # Создаем путь к каталогу и файлу
    log_directory = 'log'
    log_file_name = f'log_{today_date}.txt'
    log_file_path = os.path.join(log_directory, log_file_name)

    # Проверяем наличие каталога "log" и создаем его, если его нет
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Формируем строку для записи: "дата-время > текст"
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    log_entry = f"{today_date} {current_time} > {text}"

    # Проверяем existence файла и записываем данные
    with open(log_file_path, 'a', encoding='utf-8') as file:
        file.write(log_entry+"\n")

    if log_object != -1:
        log_object.append(log_entry)
    print(log_entry)