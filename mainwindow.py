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
import os
from pathlib import Path
from datetime import datetime

def resource_path(relative_path):
    """Получить абсолютный путь к ресурсу, работоспособный как для скрипта, так и для exe."""
    try:
        # PyInstaller создает временную директорию и хранит пути в _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        icon_path = resource_path("icon.png")
        self.setWindowIcon(QIcon(icon_path))
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.pushButton_clicked)
        self.ui.pushButton2.clicked.connect(self.pushButton2_clicked)

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
        temp_time = self.get_time_modification(file_path);
        self.ui.linePass1.setText(f"{file_path}")
        self.ui.datePass1.setText(f"{temp_time}")

    def pushButton2_clicked(self):
        file_path = self.open_file_dialog()
        temp_time = self.get_time_modification(file_path);
        self.ui.linePass1.setText(f"{file_path}")
        self.ui.datePass1.setText(f"{temp_time}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
