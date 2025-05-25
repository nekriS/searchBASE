# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QProgressBar,
    QPushButton, QSizePolicy, QTextEdit, QToolButton,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(630, 462)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(630, 462))
        MainWindow.setMaximumSize(QSize(630, 462))
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(630, 430))
        self.centralwidget.setMaximumSize(QSize(630, 430))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 40, 111, 24))
        self.linePass1 = QLineEdit(self.centralwidget)
        self.linePass1.setObjectName(u"linePass1")
        self.linePass1.setGeometry(QRect(163, 40, 301, 24))
        self.linePass1.setReadOnly(True)
        self.datePass1 = QLabel(self.centralwidget)
        self.datePass1.setObjectName(u"datePass1")
        self.datePass1.setGeometry(QRect(470, 40, 150, 24))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 141, 20))
        self.openfile = QCheckBox(self.centralwidget)
        self.openfile.setObjectName(u"openfile")
        self.openfile.setGeometry(QRect(20, 120, 181, 21))
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(False)
        self.progressBar.setGeometry(QRect(10, 400, 611, 23))
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)
        self.logblock = QTextEdit(self.centralwidget)
        self.logblock.setObjectName(u"logblock")
        self.logblock.setGeometry(QRect(10, 180, 611, 211))
        self.logblock.setReadOnly(True)
        self.nameOutput = QLineEdit(self.centralwidget)
        self.nameOutput.setObjectName(u"nameOutput")
        self.nameOutput.setGeometry(QRect(10, 150, 491, 24))
        self.checkButton = QPushButton(self.centralwidget)
        self.checkButton.setObjectName(u"checkButton")
        self.checkButton.setGeometry(QRect(510, 150, 111, 24))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 70, 141, 20))
        self.linePass2 = QLineEdit(self.centralwidget)
        self.linePass2.setObjectName(u"linePass2")
        self.linePass2.setGeometry(QRect(163, 90, 301, 24))
        self.linePass2.setReadOnly(True)
        self.pushButton2 = QPushButton(self.centralwidget)
        self.pushButton2.setObjectName(u"pushButton2")
        self.pushButton2.setGeometry(QRect(10, 90, 111, 24))
        self.datePass2 = QLabel(self.centralwidget)
        self.datePass2.setObjectName(u"datePass2")
        self.datePass2.setGeometry(QRect(470, 90, 150, 24))
        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setEnabled(False)
        self.toolButton.setGeometry(QRect(130, 90, 24, 24))
        self.toolButton_2 = QToolButton(self.centralwidget)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setEnabled(False)
        self.toolButton_2.setGeometry(QRect(130, 40, 24, 24))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(163, 20, 171, 20))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(163, 70, 171, 20))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(470, 20, 141, 20))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(470, 70, 141, 20))
        self.checkhand = QCheckBox(self.centralwidget)
        self.checkhand.setObjectName(u"checkhand")
        self.checkhand.setGeometry(QRect(210, 120, 131, 21))
        self.checknm = QCheckBox(self.centralwidget)
        self.checknm.setObjectName(u"checknm")
        self.checknm.setGeometry(QRect(340, 120, 131, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 630, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.datePass1.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b \u043d\u0435 \u043e\u0442\u043a\u0440\u044b\u0442", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0447\u0435\u043d\u044c \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432:", None))
        self.openfile.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043f\u043e\u0441\u043b\u0435 \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f", None))
        self.nameOutput.setText(QCoreApplication.translate("MainWindow", u"output_bom", None))
        self.checkButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0437\u0430 \u0434\u0430\u043d\u043d\u044b\u0445 SMT (html):", None))
        self.pushButton2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.datePass2.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b \u043d\u0435 \u043e\u0442\u043a\u0440\u044b\u0442", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f:", None))
        self.checkhand.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u044f\u0442\u044c HAND", None))
        self.checknm.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u044f\u0442\u044c NM", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
    # retranslateUi

