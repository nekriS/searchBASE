import datetime as dt
import pandas as pd
import system as st
import fnmatch
from mainwindow import PandasModel 
import time

def search(name_base, search_line, options):

    print(name_base)
    print(search_line)
    
    start_time = dt.datetime.now()
    base_table = pd.read_html(name_base, encoding='cp1251')[options.base_table_number]

    header_base = base_table.columns.tolist()
    #for i_column in options.base_drop_column:
    #    base_table = base_table.drop(columns=[header_base[i_column]])
    base_table = base_table.fillna("")

    output_table = pd.DataFrame()
    i = 1
    j = 1
    last_proc = 0

    for index, row in base_table.iterrows():
        if not(options.log_object._is_running):
            break

        i += 1
        #if search_line in row['Component']:
        if fnmatch.fnmatch(row['Component'], f"*{search_line}*") or fnmatch.fnmatch(row['Comment'], f"*{search_line}*") or fnmatch.fnmatch(row[header_base[6]], f"*{search_line}*"):
            #print(index)
            output_table = output_table._append(row, ignore_index=True)

            model = PandasModel(output_table)
            time.sleep(0.2)
            options.log_object.update_table_signal.emit(model)
            j += 1
        proc = round(i/(len(base_table)+1) * 10)
        if not(last_proc == proc):
            print(proc)
            options.log_object.update_bar_signal.emit(proc*10)
        last_proc = proc

        if j == 100:
            break

        

            #time.sleep(1)
    options.log_object.update_bar_signal.emit(100)
    
    #return output_table


if __name__ == "__main__":
    pass
