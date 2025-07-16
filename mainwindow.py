VERSION = "0.0.3"
DATE = "15.07.2025"

# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtGui import QIcon, QColor
from PySide6.QtCore import QFileInfo
import os
from pathlib import Path
from datetime import datetime
import system as st
import functions as mf
from PySide6.QtCore import QThread, Signal, QAbstractTableModel, Qt
#from concurrent.futures import ThreadPoolExecutor
import search as sch
import pandas as pd



def resource_path(relative_path):
    """Получить абсолютный путь к ресурсу, работоспособный как для скрипта, так и для exe."""
    try:
        # PyInstaller создает временную директорию и хранит пути в _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class PandasModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])


        value = self._data.iloc[index.row(), index.column()]
        if role == Qt.BackgroundRole:
            try:

                #if isinstance(str(value), str) and "R-0402" in str(value):
                #    return QColor("#ffeeaa")

                if isinstance(float(value), (int, float)) and float(value) <= 0:
                    return QColor("#FFBCBC")

            except Exception:
                pass

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])
            elif orientation == Qt.Vertical:
                return str(self._data.index[section])
        return None



class Worker(QThread):
    # Определяем сигнал, который будем использовать для передачи данных в основной поток
    update_text_signal = Signal(str)
    update_bar_signal = Signal(int)

    def __init__(self, input_file="", base_file="", output_file="", open_file="", options_=mf.options(), parent=None):
        super().__init__(parent)
        self.input_file = input_file
        self.base_file = base_file
        self.output_file = output_file
        self.open_file = open_file
        self.options_ = options_


    def run(self):
        """Этот метод выполняется в отдельном потоке"""
        self.options_.log_object = self
        bom_table = mf.find_bom_in_base(self.input_file, self.base_file, self.options_, preset_list=self.presetlist)
        mf.draw_file(self.input_file, bom_table, self.output_file, self.open_file, self.options_, preset_list=self.presetlist)


class WorkerSearch(QThread):
    # Определяем сигнал, который будем использовать для передачи данных в основной поток
    update_text_signal = Signal(str)
    update_bar_signal = Signal(int)

    update_table_signal = Signal(pd.DataFrame)

    def __init__(self, search_line="", base_file="", options_=mf.options(), parent=None):
        super().__init__(parent)
        self.search_line = search_line
        self.base_file = base_file
        self.options_ = options_
        self._is_running = True

    def run(self):
        """Этот метод выполняется в отдельном потоке"""

        self.options_.log_object = self

        sch.search(self.base_file, self.search_line, self.options_)


    def stop(self):
        self._is_running = False


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        icon_path = resource_path("icon.png")
        self.setWindowIcon(QIcon(icon_path))
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.pushButton_clicked)
        self.ui.pushButton2.clicked.connect(self.pushButton2_clicked)
        self.ui.checkButton.clicked.connect(self.checkButton_clicked)
        self.ui.search.clicked.connect(self.search_button_clicked)
        self.ui.search_stop.clicked.connect(self.search_stop_button_clicked)
        self.ui.action.triggered.connect(self.show_about_dialog)

        self.setWindowTitle("searchBASE " + VERSION)


        opt = mf.options()

        for section in opt.config.keys():
            if "LIST_" in section:
                self.ui.preset_list.addItem(opt.config[section]["view_name"], userData=section)



        try:
            file_path = "SMT-iLogic.html"
            temp_time = self.get_time_modification(file_path)
            self.ui.linePass2.setText(f"{file_path}")
            self.ui.datePass2.setText(f"{temp_time}")
        except:
            pass

    def search_stop_button_clicked(self):
        try:
            self.worker.stop()
        except:
            pass

    def search_button_clicked(self):

        options = mf.options()

        self.ui.progressBar.setValue(0)

        search_line = self.ui.lineSearch.text()
        base_file = self.ui.linePass2.text()

        try:
            self.worker.stop()
        except:
            pass

        self.worker = WorkerSearch(search_line, base_file, options)
        self.worker.update_text_signal.connect(self.append_text)
        self.worker.update_bar_signal.connect(self.append_progress)
        self.worker.update_table_signal.connect(self.update_table_f)

        self.worker.start()


        pass

    def get_time_modification(self, file_path_str):
        """
        Возвращает время последней модификации файла
        """
        file_path = Path(file_path_str)
        modification_time = file_path.stat().st_mtime
        modification_date = datetime.fromtimestamp(modification_time)
        return modification_date.strftime("%Y-%m-%d %H:%M:%S")

    def open_file_dialog(self):
        """Открывает диалоговое окно для выбора файла"""
        options = QFileDialog.Options()  # Опции диалогового окна
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Выберите файл",
            "",  # Начальная директория (пустая строка означает текущую директорию)
            "Все файлы (*)",  # Фильтр типов файлов
            options=options
        )

        return file_path


    def pushButton_clicked(self):
        file_path = self.open_file_dialog()
        temp_time = self.get_time_modification(file_path)
        self.ui.linePass1.setText(f"{file_path}")
        self.ui.datePass1.setText(f"{temp_time}")

        short_name = QFileInfo(file_path).fileName()
        output_name = st.create_name_file(str(short_name),autosuffix=False, suffix_text=".xlsx")
        self.ui.nameOutput.setText(output_name)

    def pushButton2_clicked(self):
        file_path = self.open_file_dialog()
        temp_time = self.get_time_modification(file_path)
        self.ui.linePass2.setText(f"{file_path}")
        self.ui.datePass2.setText(f"{temp_time}")

    def checkButton_clicked(self):

        input_file = self.ui.linePass1.text()
        base_file = self.ui.linePass2.text()
        output_file = self.ui.nameOutput.text()
        open_file = self.ui.openfile.isChecked()

        if (".xls" in input_file) and not(".xlsx" in input_file):
            import win32com.client as win32
            fname = input_file.replace("/","\\")
            excel = win32.gencache.EnsureDispatch('Excel.Application')
            wb = excel.Workbooks.Open(fname)
            wb.SaveAs(fname+"x", FileFormat = 51)    #FileFormat = 51 is for .xlsx extension
            wb.Close()                               #FileFormat = 56 is for .xls extension
            excel.Application.Quit()
            input_file += "x"


        options = mf.options()

        options.check_hand = self.ui.checkhand.isChecked()
        options.check_nm = self.ui.checknm.isChecked()


        self.ui.progressBar.setValue(0)
        self.worker = Worker(input_file, base_file, output_file, open_file, options)
        self.worker.update_text_signal.connect(self.append_text)
        self.worker.update_bar_signal.connect(self.append_progress)
        self.worker.presetlist = self.ui.preset_list.currentData()
        self.worker.start()

    def update_table_f(self, model):


        self.ui.tableView.setModel(model)
        self.ui.tableView.resizeColumnsToContents()

    def append_text(self, text):

        self.ui.logblock.append(text)

    def append_progress(self, num):

        self.ui.progressBar.setValue(num)

    def show_about_dialog(self):
                """Показывает диалог 'О программе'"""
                QMessageBox.about(
                    self,
                    "О программе",
                    "Название программы: searchBASE    \n"
                    "Версия: " + VERSION + "\n"
                    "Автор: Лев Кириллов\n"
                    "Дата сборки: " + DATE + "\n"
                    "\n"
                    "Программа для поиска элементов и списков в таблицах .html."
                )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
