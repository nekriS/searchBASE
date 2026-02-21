
import Levenshtein
import re
from collections import Counter

def jaccard_similarity(vec1, vec2):
    intersection = sum([min(a, b) for a, b in zip(vec1, vec2)])
    union = sum([max(a, b) for a, b in zip(vec1, vec2)])
    return intersection / union if union != 0 else 0

def create_count_vectors(str1, str2):
    # Токенизация как в CountVectorizer (по не-алфанумерическим символам)
    token_pattern = r"(?u)\b\w\w+\b"
    
    tokens1 = re.findall(token_pattern, str1.lower())
    tokens2 = re.findall(token_pattern, str2.lower())
    
    all_tokens = sorted(set(tokens1 + tokens2))
    
    counter1 = Counter(tokens1)
    counter2 = Counter(tokens2)
    
    vec1 = [counter1.get(token, 0) for token in all_tokens]
    vec2 = [counter2.get(token, 0) for token in all_tokens]
    
    return vec1, vec2

def compare(str1="", str2="", method="content", replace_list=[["NPO", "NP0"]], ignore_len=3):
    if len(replace_list) > 0:
        for replace_item in replace_list:
            str1 = str1.replace(replace_item[0], replace_item[1])
            str2 = str2.replace(replace_item[0], replace_item[1])
    similarity = 0
    match method:
        case 'Levenshtein':
            distance = Levenshtein.distance(str1, str2)
            similarity = 1 - Levenshtein.distance(str1, str2) / max(len(str1), len(str2))
        case 'Jacquard':
            try:
                vectors = create_count_vectors(str1, str2)
                #vectors = vectorizer.toarray()
                similarity = jaccard_similarity(vectors[0], vectors[1])
            except:
                similarity = 0
        case 'content':
            if len(str2) < ignore_len:
                return 0
            if str1.find('-') == 1:
                str1_ = str1[1:].replace('-','')
                if (str1_ in str2) or (str2 in str1):
                    similarity = 1
            if (str1 in str2) or (str2 in str1):
                similarity = 1
    return similarity

def nmax(nums):
    maxx = max(nums)
    for i in range(0, len(nums) + 1):
        if nums[i] == maxx:
            return maxx, i

def find_all_occurrences(text, substring):
    start = 0
    indices = []
    while True:
        index = text.find(substring, start)
        if index == -1:  
            break
        indices.append(index)
        start = index + 1
    return indices

def isRLC_(part_number):
    elements = ['R', 'C', 'L']
    packages = ['0603', '0402', '0201', '0805', '1206', '1210']
    split_part_number = part_number.split('-')
    if split_part_number[0] in elements:
        pos_ = find_all_occurrences(part_number, '-')
        if len(pos_) > 1:
            if part_number[pos_[0]+1:pos_[1]] in packages:
                return [True, part_number[pos_[0]+1:pos_[1]]]
    elif split_part_number[0] in packages:
        pos_ = find_all_occurrences(part_number, '-')
        if len(pos_) > 1:
            if part_number[0:pos_[0]] in packages:
                return [True, part_number[0:pos_[0]]]
    return [False, ""]


def index(string, mask, target):
    try:
        return string[mask.index(target)]
    except:
        return ""

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def isRLC(part_number, options, mask=""):

    split_part_number = part_number.split('-')

    packages = ['0603', '0402', '0201', '0805', '1206', '1210']
    dies = ['NPO', 'NP0', 'X7R', 'X5R', 'X5S', 'X6S', 'X6S', 'X6T', 'X7S', 'X7T', 'X7U', 'X8R', 'C0G', 'U2J', 'X8L', 'X8M', 'X8N', 'X5T', 'ZLM', 'X8G']

    if mask == "":
        cap_mask = options.cap_mask.split('-')
        res_mask = options.res_mask.split('-')
    else:
        cap_mask = mask.split('-')
        res_mask = mask.split('-')

    type_ = index(split_part_number, cap_mask, "TYPE")
    size_ = index(split_part_number, cap_mask, "SIZE")
    die_ = index(split_part_number, cap_mask, "DIE")
    vol_ = index(split_part_number, cap_mask, "VOL")
    val_ = index(split_part_number, cap_mask, "VALUE TOL")

    if type_ == "C" and (is_number(vol_.upper().replace("V",""))) and (die_ in dies):
        return [True, type_, size_, die_, float(vol_.upper().replace("V","")), val_]
    elif (type_ == "") and (size_ in packages) and (is_number(vol_.upper().replace("V",""))) and (die_ in dies):
        return [True, "C", size_, die_, float(vol_.upper().replace("V","")), val_]
    

    type_ = index(split_part_number, res_mask, "TYPE")
    size_ = index(split_part_number, res_mask, "SIZE")
    val_ = index(split_part_number, res_mask, "VALUE TOL")

    if type_ == "R":
        return [True, type_, size_, val_]
    elif (type_ == "") and (size_ in packages):
        return [True, "R", size_, val_]
    

    return [False, ""]





    


        
    


def set_column_autowidth(ws, columns, reserve=1.2):
    """
    Устанавливает оптимальную ширину столбцов на основе содержимого.
    """
    for column_cells in ws.columns:
        max_length = 0
        column = column_cells[0].column_letter  # Получаем букву столбца (A, B, C, ...)
        
        if column in columns:
            # Находим максимальную длину текста в столбце
            for cell in column_cells:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass
        
            # Устанавливаем ширину столбца с небольшим запасом
            adjusted_width = (max_length + 2) * reserve  # Можно изменить коэффициент для более комфортного отображения
            ws.column_dimensions[column].width = adjusted_width

def move_column(ws, column_index, move, skip=0):
    """
    Перемещает столбец на move вправо.
    
    :param ws: Рабочий лист (Worksheet)
    :param column_index: Индекс столбца, который нужно переместить (начиная с 1)
    :param move: Смещение
    """
    max_row = ws.max_row  # Получаем максимальное количество строк
    
    # Копируем значения из исходного столбца в новый столбец
    for row in range(1+skip, max_row + 1):
        original_value = ws.cell(row=row, column=column_index).value
        ws.cell(row=row, column=column_index + move).value = original_value
    
    # Очищаем исходный столбец
    for row in range(1+skip, max_row + 1):
        ws.cell(row=row, column=column_index).value = None



import re

def parse_component_value(value_str):
    """
    Парсит строку с номиналом компонента и возвращает численное значение в базовых единицах.
    
    Поддерживаемые форматы:
    - 10R1 → 10.1 (омы)
    - 12K3 → 12300 (омы)
    - 10uF → 0.00001 (фарады)
    - 4K7 → 4700 (омы)
    - 100n → 1e-7 (фарады или генри)
    
    Args:
        value_str: Строка с номиналом (например, "10R1", "12K3", "10uF")
    
    Returns:
        float: Численное значение в базовых единицах (омы, фарады, генри)
    
    Raises:
        ValueError: Если строка не может быть распарсена
    """
    value_str = value_str.replace(",",".").strip()
    
    # Словарь префиксов и их множителей
    prefixes = {
        'R': 1,       # Омы (для резисторов)
        'K': 1e3,     # Кило
        'M': 1e6,     # Мега
        'G': 1e9,     # Гига
        'p': 1e-12,   # Пико
        'P': 1e-12,
        'n': 1e-9,    # Нано
        'N': 1e-9,
        'u': 1e-6,    # Микро
        'μ': 1e-6,    # Микро (символ мю)
        'm': 1e-3,    # Милли
    }
    
    # Единицы измерения для удаления
    units = ['F', 'f', 'H', 'h', 'Ω', 'ohm', 'OHM', 'Ohm']
    
    # Удаляем единицы измерения
    clean_str = value_str
    for unit in units:
        clean_str = clean_str.replace(unit, '')
    
    # Поиск префикса
    prefix = None
    prefix_pos = -1
    
    for p in prefixes:
        if p in clean_str:
            pos = clean_str.find(p)
            if prefix_pos == -1 or pos < prefix_pos:
                prefix = p
                prefix_pos = pos
    
    if prefix is None:
        try:
            return float(clean_str)
        except ValueError:
            return -10000000
    
    # Разбор числовой части
    before = clean_str[:prefix_pos]
    after = clean_str[prefix_pos + 1:]
    
    if before and after:
        number_str = before + '.' + after
    elif before:
        number_str = before
    elif after:
        number_str = after
    else:
        return -10000000
    
    try:
        number = float(number_str)
    except ValueError:
        return -10000000
    
    return number * prefixes[prefix]