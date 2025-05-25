import datetime
import os
import re

input_file = "extsdsd.xlsx"


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


print(get_name_file("BOM_HFR_test.xlsx"))
