import pandas as pd

class options:
    def __init__(self, 
                 bom_use_columns = "A, B, C, D, E, F", 
                 bom_skip_rows = 8,
                 bom_pn_number = 3,
                 bom_type_number = 5,
                 base_table_number = 1,
                 save_base2excel = False,
                 name_base2excel = "base.xlsx",
                 compare_method = "normal"):
        self.bom_use_columns = bom_use_columns # необходимые столбцы из перечня компонентов
        self.bom_skip_rows = bom_skip_rows # сколько строк при анализе необходимо удалить
        self.bom_pn_number = bom_pn_number # номер столбца, в котором находится парт номер
        self.bom_type_number = bom_type_number # номер столбца, в котором находится тип монтажа
        self.base_table_number = base_table_number # номер таблицы из базы
        self.save_base2excel = save_base2excel # сохранить ли базу в эксель
        self.name_base2excel = name_base2excel # название для базы при сохранении в эксель
        self.compare_method = compare_method # тип сравнения нормальный (с порогами) или с помощью нейронной сети

def open_files(name_bom, name_base, options):
    
    bom_table = pd.read_excel(name_bom, usecols=options.bom_use_columns, skiprows=options.bom_skip_rows)
    header_bom = bom_table.columns.tolist()
    name_pn_bom = header_bom[options.bom_pn_number]
    type_part_bom = type_part_bom[options.bom_type_number]

    base_table = pd.read_html(name_base, encoding='cp1251')[options.base_table_number]
    header_base = base_table.columns.tolist()
    base_table = base_table.drop([11, 10, 9, 8, 4, 3, 2, 0, 1])

    if options.save_base2excel:
        base_table.to_excel(options.name_base2excel, index=False)

    base_table['SMT'] = ""
    base_table['SMT Баланс'] = 0
    base_table['SMT Жаккара'] = ""
    base_table['SMT Левенштейна'] = ""
    base_table['Результат'] = 0

    for index_bom, row_bom in bom_table.iterrows():
        
        str1 = str(row_bom[name_pn_bom]).replace("nan", "")
        type_part = str(row_bom[type_part_bom]).replace("nan", "")

    return [bom_table, base_table]
        








if __name__ == "__main__":

    name_bom = ""
    name_base = ""
    options_1 = options()

    [bom_table, base_table] = open_files(name_bom, name_base, options_1)