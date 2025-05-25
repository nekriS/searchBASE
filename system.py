import os
import datetime
import re

def get_time_difference(start_time: datetime.datetime, end_time: datetime.datetime) -> str:
    """
    Возвращает разницу между двумя временными метками в формате 'HH:MM:SS'.

    :param start_time: Начальное время (datetime)
    :param end_time: Конечное время (datetime)
    :return: Разница в формате 'HH:MM:SS'
    """
    delta = end_time - start_time
    total_seconds = int(delta.total_seconds())

    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def log(text, log_object=-1):

    if text != "" and text != " ":
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
            log_object.update_text_signal.emit(log_entry)
            #log_object.append(log_entry)
        print(log_entry)


def create_name_file(input_file, verified = True, date = True, suffix = True, suffix_text = ""):
    if input_file.find('.') != -1:
        k = input_file.find('.')
        if suffix:
            suffix_text = input_file[k:]
        input_file = input_file[:k]

    today_date = datetime.datetime.now().strftime('_%Y_%m_%d')
    if verified:
        input_file += "_verified"
    if date:
        input_file += str(today_date)

    return input_file + suffix_text



def get_name_file(filename):
    if not os.path.isfile(filename):
        new_filename = filename
    else:
        match = re.match(r"^(.*?)(?:\((\d+)\))?(\.\w+)$", filename)
        if match:
            base, num, ext = match.groups()
            counter = int(num) + 1 if num else 1
        else:
            base, ext = os.path.splitext(filename)
            counter = 1
        
        # Формируем новое имя с инкрементом
        new_filename = f"{base}({counter}){ext}"
        while os.path.isfile(new_filename):
            counter += 1
            new_filename = f"{base}({counter}){ext}"
    return new_filename
