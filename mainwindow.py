VERSION = "0.0.1"
DATE = "25.05.2025"

# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtGui import QIcon
from PySide6.QtCore import QFileInfo
import os
from pathlib import Path
from datetime import datetime
import system as st
import mainFunction as mf
from PySide6.QtCore import QThread, Signal
#from concurrent.futures import ThreadPoolExecutor


def resource_path(relative_path):
    """Получить абсолютный путь к ресурсу, работоспособный как для скрипта, так и для exe."""
    try:
        # PyInstaller создает временную директорию и хранит пути в _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Worker(QThread):
    # Определяем сигнал, который будем использовать для передачи данных в основной поток
    update_text_signal = Signal(str)

    def __init__(self, input_file, base_file, output_file, parent=None):
        super().__init__(parent)
        self.input_file = input_file
        self.base_file = base_file
        self.output_file = output_file

    def run(self):
        """Этот метод выполняется в отдельном потоке"""



        options = mf.options()
        options.save_bom2excel = False
        options.log_object = self

        bom_table = mf.find_bom_in_base(self.input_file, self.base_file, options)
        mf.draw_file(self.input_file, bom_table, self.output_file, True)

        #for i in range(5):
        #    time.sleep(1)  # имитация долгой операции
            #message = f"Обработка... {i + 1}/5\n"
              # отправляем данные в GUI


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

        self.setWindowTitle("checkBOM " + VERSION)

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
        output_name = st.create_name_file(str(short_name))
        self.ui.nameOutput.setText(output_name)

    def pushButton2_clicked(self):
        file_path = self.open_file_dialog()
        temp_time = self.get_time_modification(file_path)
        self.ui.linePass2.setText(f"{file_path}")
        self.ui.datePass2.setText(f"{temp_time}")

    def checkButton_clicked(self):





        #with ThreadPoolExecutor() as executor:
        #    future = executor.submit(mf.find_bom_in_base, input_file, base_file, options)
        #    bom_table = future.result()
        #t1 = threading.Thread(target=mf.find_bom_in_base, args=(input_file, base_file, options))
        #t1.start()
        #t1.join()
        input_file = self.ui.linePass1.text()
        base_file = self.ui.linePass2.text()
        output_file = self.ui.nameOutput.text()

        self.worker = Worker(input_file, base_file, output_file)
        self.worker.update_text_signal.connect(self.append_text)
        self.worker.start()

    def append_text(self, text):
            """Метод вызывается из потока через сигнал и добавляет текст в QTextEdit"""
            self.ui.logblock.append(text)

        #print(input_file, base_file, output_file)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
