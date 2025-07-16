# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QGridLayout, QGroupBox, QHeaderView, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTableView, QTextEdit,
    QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(881, 670)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(817, 670))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u"icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setIconSize(QSize(50, 50))
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        icon1 = QIcon(QIcon.fromTheme(u"help-about"))
        self.action.setIcon(icon1)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(630, 430))
        self.centralwidget.setMaximumSize(QSize(63000, 43000))
        self.centralwidget.setAcceptDrops(False)
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(12, 20, 12, 20)
        self.linePass2 = QLineEdit(self.centralwidget)
        self.linePass2.setObjectName(u"linePass2")
        self.linePass2.setMinimumSize(QSize(20, 0))
        self.linePass2.setReadOnly(True)

        self.gridLayout.addWidget(self.linePass2, 4, 2, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 16))

        self.gridLayout.addWidget(self.label_5, 3, 2, 1, 1)

        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setEnabled(False)

        self.gridLayout.addWidget(self.toolButton, 4, 1, 1, 1)

        self.pushButton2 = QPushButton(self.centralwidget)
        self.pushButton2.setObjectName(u"pushButton2")
        self.pushButton2.setMinimumSize(QSize(150, 24))
        self.pushButton2.setMaximumSize(QSize(150, 24))

        self.gridLayout.addWidget(self.pushButton2, 4, 0, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 16))

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 2)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 3, 3, 1, 1)

        self.datePass2 = QLabel(self.centralwidget)
        self.datePass2.setObjectName(u"datePass2")
        self.datePass2.setMinimumSize(QSize(278, 0))
        self.datePass2.setMaximumSize(QSize(278, 16777215))

        self.gridLayout.addWidget(self.datePass2, 4, 3, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setMinimumSize(QSize(800, 500))
        self.tabWidget.setUsesScrollButtons(True)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_2 = QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(6)
        self.groupBox = QGroupBox(self.tab_3)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 100))

        self.gridLayout_2.addWidget(self.groupBox, 3, 0, 1, 3)

        self.tableView = QTableView(self.tab_3)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.CurrentChanged|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.tableView.setDefaultDropAction(Qt.CopyAction)
        self.tableView.setAlternatingRowColors(False)
        self.tableView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableView.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.gridLayout_2.addWidget(self.tableView, 4, 0, 1, 3)

        self.label = QLabel(self.tab_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setWeight(QFont.Medium)
        self.label.setFont(font)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)

        self.lineSearch = QLineEdit(self.tab_3)
        self.lineSearch.setObjectName(u"lineSearch")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineSearch.sizePolicy().hasHeightForWidth())
        self.lineSearch.setSizePolicy(sizePolicy2)
        self.lineSearch.setMinimumSize(QSize(0, 60))
        font1 = QFont()
        font1.setFamilies([u"GOST type B"])
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setKerning(True)
        self.lineSearch.setFont(font1)
        self.lineSearch.setStyleSheet(u"margin-top: 10px;\n"
"margin-bottom: 10px;\n"
"padding-left: 15px;\n"
"padding-bottom: 1px;\n"
"vertical-align: middle;\n"
"border-radius: 20;\n"
"border: 1px solid gray;\n"
"\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.lineSearch, 1, 1, 1, 1)

        self.search = QPushButton(self.tab_3)
        self.search.setObjectName(u"search")
        self.search.setMinimumSize(QSize(100, 60))
        self.search.setStyleSheet(u"QPushButton {\n"
"margin-top: 10px;\n"
"margin-bottom: 10px;\n"
"padding-bottom: 1px;\n"
"vertical-align: middle;\n"
"border-radius: 20;\n"
"border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #e3e3e3;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: white;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.search, 1, 0, 1, 1)

        self.search_stop = QPushButton(self.tab_3)
        self.search_stop.setObjectName(u"search_stop")
        self.search_stop.setMinimumSize(QSize(40, 60))
        self.search_stop.setStyleSheet(u"QPushButton {\n"
"margin-top: 10px;\n"
"margin-bottom: 10px;\n"
"padding-bottom: 1px;\n"
"vertical-align: middle;\n"
"border-radius: 20;\n"
"border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 143, 145);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: white;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.search_stop, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout = QVBoxLayout(self.tab_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 0, 5, 1, 2)

        self.openfile = QCheckBox(self.tab_2)
        self.openfile.setObjectName(u"openfile")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.openfile.sizePolicy().hasHeightForWidth())
        self.openfile.setSizePolicy(sizePolicy3)
        self.openfile.setMaximumSize(QSize(176, 16777215))
        self.openfile.setChecked(True)

        self.gridLayout_4.addWidget(self.openfile, 6, 0, 1, 2)

        self.linePass1 = QLineEdit(self.tab_2)
        self.linePass1.setObjectName(u"linePass1")
        sizePolicy2.setHeightForWidth(self.linePass1.sizePolicy().hasHeightForWidth())
        self.linePass1.setSizePolicy(sizePolicy2)
        self.linePass1.setMinimumSize(QSize(20, 0))
        self.linePass1.setReadOnly(True)

        self.gridLayout_4.addWidget(self.linePass1, 1, 2, 1, 3)

        self.checkButton = QPushButton(self.tab_2)
        self.checkButton.setObjectName(u"checkButton")

        self.gridLayout_4.addWidget(self.checkButton, 7, 6, 1, 1)

        self.checknm = QCheckBox(self.tab_2)
        self.checknm.setObjectName(u"checknm")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.checknm.sizePolicy().hasHeightForWidth())
        self.checknm.setSizePolicy(sizePolicy4)

        self.gridLayout_4.addWidget(self.checknm, 6, 3, 1, 2)

        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 0, 2, 1, 3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 6, 5, 1, 2)

        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy5)
        self.label_2.setMinimumSize(QSize(176, 0))
        self.label_2.setMaximumSize(QSize(176, 16777215))

        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 2)

        self.checkhand = QCheckBox(self.tab_2)
        self.checkhand.setObjectName(u"checkhand")
        self.checkhand.setMaximumSize(QSize(120, 16777215))

        self.gridLayout_4.addWidget(self.checkhand, 6, 2, 1, 1)

        self.logblock = QTextEdit(self.tab_2)
        self.logblock.setObjectName(u"logblock")
        self.logblock.setReadOnly(True)

        self.gridLayout_4.addWidget(self.logblock, 8, 0, 1, 7)

        self.nameOutput = QLineEdit(self.tab_2)
        self.nameOutput.setObjectName(u"nameOutput")

        self.gridLayout_4.addWidget(self.nameOutput, 7, 0, 1, 6)

        self.datePass1 = QLabel(self.tab_2)
        self.datePass1.setObjectName(u"datePass1")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.datePass1.sizePolicy().hasHeightForWidth())
        self.datePass1.setSizePolicy(sizePolicy6)
        self.datePass1.setMinimumSize(QSize(278, 0))

        self.gridLayout_4.addWidget(self.datePass1, 1, 5, 1, 2)

        self.pushButton = QPushButton(self.tab_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(176, 0))
        self.pushButton.setMaximumSize(QSize(176, 16777215))

        self.gridLayout_4.addWidget(self.pushButton, 1, 0, 1, 2)

        self.preset_list = QComboBox(self.tab_2)
        self.preset_list.setObjectName(u"preset_list")
        self.preset_list.setMaximumSize(QSize(176, 16777215))

        self.gridLayout_4.addWidget(self.preset_list, 2, 0, 1, 2)

        self.gridLayout_4.setColumnStretch(1, 1)
        self.gridLayout_4.setColumnStretch(2, 1)
        self.gridLayout_4.setColumnStretch(3, 1)
        self.gridLayout_4.setColumnStretch(4, 1)
        self.gridLayout_4.setColumnStretch(5, 1)
        self.gridLayout_4.setColumnStretch(6, 1)

        self.verticalLayout.addLayout(self.gridLayout_4)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(False)
        self.progressBar.setMinimumSize(QSize(0, 24))
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_2.addWidget(self.progressBar)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 881, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b:", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0437\u0430 \u0434\u0430\u043d\u043d\u044b\u0445 (html):", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f:", None))
        self.datePass2.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b \u043d\u0435 \u043e\u0442\u043a\u0440\u044b\u0442", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043f\u043e\u0438\u0441\u043a\u0430", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0440\u043e\u0441:", None))
        self.lineSearch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0441\u0442 \u0437\u0430\u043f\u0440\u043e\u0441\u0430", None))
        self.search.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.search_stop.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u0432 \u0431\u0430\u0437\u0435", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f:", None))
        self.openfile.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043f\u043e\u0441\u043b\u0435 \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f", None))
        self.checkButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c", None))
        self.checknm.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u044f\u0442\u044c NM", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0447\u0435\u043d\u044c \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432:", None))
        self.checkhand.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u044f\u0442\u044c HAND", None))
        self.nameOutput.setText(QCoreApplication.translate("MainWindow", u"output_bom", None))
        self.datePass1.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b \u043d\u0435 \u043e\u0442\u043a\u0440\u044b\u0442", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u0438\u0437 \u0444\u0430\u0439\u043b\u0430", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
    # retranslateUi

