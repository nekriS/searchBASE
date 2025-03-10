import pandas as pd
import utility as ut
import system as st

MINIMAL_LEN = 2

class options:
    def __init__(self, 
                 bom_use_columns = "A, B, C, D, E, F", 
                 bom_skip_rows = 8,
                 bom_pn_number = 3,
                 bom_type_number = 5,
                 save_bom2excel = False,
                 name_bom2excel = "bom.xlsx",
                 base_table_number = 1,
                 base_pn_number = 3,
                 base_drop_column = [11, 10, 9, 8, 4, 3, 2, 0, 1],
                 base_balance_number = 2,
                 base_1c_number = 3,
                 base_comm_number = 1,
                 save_base2excel = False,
                 name_base2excel = "base.xlsx",
                 compare_method = "normal",
                 quiet_mode = False):
        self.bom_use_columns = bom_use_columns # необходимые столбцы из перечня компонентов
        self.bom_skip_rows = bom_skip_rows # сколько строк при анализе необходимо удалить
        self.bom_pn_number = bom_pn_number # номер столбца, в котором находится парт номер
        self.bom_type_number = bom_type_number # номер столбца, в котором находится тип монтажа
        self.save_bom2excel = save_bom2excel # 
        self.name_bom2excel = name_bom2excel # 
        self.base_table_number = base_table_number # номер таблицы из базы
        self.base_pn_number = base_pn_number # номер столбца, в котором находится парт номер
        self.base_drop_column = base_drop_column # номера столбцов, которые необходимо выкинуть
        self.base_balance_number = base_balance_number # 
        self.base_1c_number = base_1c_number # 
        self.base_comm_number = base_comm_number # 
        self.save_base2excel = save_base2excel # сохранить ли базу в эксель
        self.name_base2excel = name_base2excel # название для базы при сохранении в эксель
        self.compare_method = compare_method # тип сравнения нормальный (с порогами) или с помощью нейронной сети
        self.quiet_mode = quiet_mode # включает тихий режим (отключает сообщения отладки)



def find_bom_in_base(name_bom, name_base, options):
    
    bom_table = pd.read_excel(name_bom, usecols=options.bom_use_columns, skiprows=options.bom_skip_rows)
    header_bom = bom_table.columns.tolist()
    name_pn_bom = header_bom[options.bom_pn_number]
    type_part_bom = type_part_bom[options.bom_type_number]

    base_table = pd.read_html(name_base, encoding='cp1251')[options.base_table_number]
    base_table = base_table.drop(options.base_drop_column)
    header_base = base_table.columns.tolist()
    name_pn_base = header_base[options.base_pn_number]
    name_comm_base = header_base[options.base_comm_number]
    name_1c_base = header_base[options.base_1c_number]
    name_balance = header_base[options.base_balance_number]

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

        if not(options.quiet_mode):
            print(str1)

        result = 0
        balance = 0
        name_base = ""

        components_Lev = []
        components_Jac = []
        components_All = []

        if (len(type_part) > MINIMAL_LEN) and (len(str1) > MINIMAL_LEN):
            for index_base, row_base in base_table.iterrows():

                balance = row_base[name_balance]
                str2 = str(row_base[name_pn_base])
                str2_comm = str(row_base[name_comm_base])
                str2_1c = str(row_base[name_1c_base])

                strs = [str2, str2_comm, str2_1c]
                coef_Lev, i_Lev = ut.nmax([ut.compare(str1, str2, 'Levenshtein'), ut.compare(str1, str2_comm, 'Levenshtein'), ut.compare(str1, str2_1c, 'Levenshtein')])
                coef_Jac, i_Jac = ut.nmax([ut.compare(str1, str2, 'Jacquard'), ut.compare(str1, str2_comm, 'Jacquard'), ut.compare(str1, str2_1c, 'Jacquard')])
                coef_equ, i_equ =  ut.nmax([ut.compare(str1, str2), ut.compare(str1, str2_comm), ut.compare(str1, str2_1c)])

                if coef_equ == 1:
                    if ut.compare(str1, str2, 'Levenshtein') > 0.9 and ut.compare(str1, str2, 'Jacquard') > 0.6:
                        result = 2
                        name_base = str2
                        break
                    elif ut.compare(str1, str2, 'Jacquard') > 0.3:
                        result = 1
                        name_base = str2
                        break
                if (coef_Lev > 0.5) and (coef_Jac > 0.5): 
                    components_All.append([coef_Lev, coef_Jac, str2, strs[i_Lev]])
                else:
                    if (coef_Lev > 0.5):
                        if ut.isRLC(str1)[0]:
                            if ut.isRLC(str1)[1] in str2:
                                components_Lev.append([coef_Lev, str2, strs[i_Lev]])
                        else:
                            components_Lev.append([coef_Lev, str2, strs[i_Lev]])
                    if (coef_Jac > 0.5):
                        components_Jac.append([coef_Jac, str2, strs[i_Jac]])

            components_Lev = sorted(components_Lev, key=lambda x: x[0], reverse=True)
            components_Jac = sorted(components_Jac, key=lambda x: x[0], reverse=True)
            components_All = sorted(components_All, key=lambda x: x[0], reverse=True)

            if result == 0:
                if options.compare_method == "normal":
                    if (len(components_All) > 0):
                        if components_All[0][0] > 0.9 and components_All[0][1] > 0.6:
                            result = 1
                            name_smt = str(components_All[0][2])
                        else:
                            if (len(components_Lev) > 0) or (len(components_Jac) > 0):
                                if components_Lev[0][0] > 0.95:
                                    result = 1
                                    name_smt = str(components_Lev[0][1])
                                else:
                                    result = -1
                            else:
                                result = -2
                    else:
                        if (len(components_Lev) > 0) or (len(components_Jac) > 0):
                            if components_Lev[0][0] > 0.95:
                                result = 1
                                name_smt = str(components_Lev[0][1])
                            else:
                                result = -1
                        else:
                            result = -2

            if result < 0:
                bom_table.at[index_bom, 'SMT Левенштейна'] = str(components_Lev)
                bom_table.at[index_bom, 'SMT Жаккара'] = str(components_Jac)

            bom_table.at[index_bom, 'SMT'] = name_smt
            bom_table.at[index_bom, 'Результат'] = result
            bom_table.at[index_bom, 'SMT Баланс'] = balance

    if options.save_bom2excel:
        bom_table.to_excel(options.name_bom2excel, index=False)

    return bom_table
        








if __name__ == "__main__":

    name_bom = ""
    name_base = ""
    options_1 = options()

    bom_table = find_bom_in_base(name_bom, name_base, options_1)