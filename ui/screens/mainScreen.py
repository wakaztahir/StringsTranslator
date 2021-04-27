# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from ui.components.CheckableComboBox import CheckableComboBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(350, 563)
        MainWindow.setStyleSheet(u"/*-----QWidget-----*/\n"
                                 "QWidget\n"
                                 "{\n"
                                 "	background-color: #fff;\n"
                                 "	color: red;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "/*-----QLabel-----*/\n"
                                 "QLabel\n"
                                 "{\n"
                                 "	background-color: transparent;\n"
                                 "	color: #454544;\n"
                                 "	font-weight: bold;\n"
                                 "	font-size: 13px;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "/*-----QPushButton-----*/\n"
                                 "QPushButton\n"
                                 "{\n"
                                 "	background-color: #5c55e9;\n"
                                 "	color: #fff;\n"
                                 "	font-size: 13px;\n"
                                 "	font-weight: bold;\n"
                                 "	border-top-right-radius: 15px;\n"
                                 "	border-top-left-radius: 0px;\n"
                                 "	border-bottom-right-radius: 0px;\n"
                                 "	border-bottom-left-radius: 15px;\n"
                                 "	padding: 10px;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QPushButton::disabled\n"
                                 "{\n"
                                 "	background-color: #5c5c5c;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QPushButton::hover\n"
                                 "{\n"
                                 "	background-color: #5564f2;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QPushButton::pressed\n"
                                 "{\n"
                                 "	background-color: #3d4ef2;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "/*-----QCheckBox-----*/\n"
                                 "QCheckBox\n"
                                 "{\n"
                                 "	background-color: transparent;\n"
                                 "	color: #5c55e9;\n"
                                 "	font-size: 10px;\n"
                                 "	font-weight: bold;\n"
                                 "	border: no"
                                 "ne;\n"
                                 "	border-radius: 5px;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "/*-----QCheckBox-----*/\n"
                                 "QCheckBox::indicator\n"
                                 "{\n"
                                 "    background-color: #323232;\n"
                                 "    border: 1px solid darkgray;\n"
                                 "    width: 12px;\n"
                                 "    height: 12px;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QCheckBox::indicator:checked\n"
                                 "{\n"
                                 "    image:url(\"./ressources/check.png\");\n"
                                 "	background-color: #5c55e9;\n"
                                 "    border: 1px solid #5c55e9;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QCheckBox::indicator:unchecked:hover\n"
                                 "{\n"
                                 "    border: 1px solid #5c55e9;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QCheckBox::disabled\n"
                                 "{\n"
                                 "	color: #656565;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QCheckBox::indicator:disabled\n"
                                 "{\n"
                                 "	background-color: #656565;\n"
                                 "	color: #656565;\n"
                                 "    border: 1px solid #656565;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "/*-----QLineEdit-----*/\n"
                                 "QLineEdit\n"
                                 "{\n"
                                 "	background-color: #c2c7d5;\n"
                                 "	color: #2a547f;\n"
                                 "	border: none;\n"
                                 "	padding: 5px;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "/*-----QListView-----*/\n"
                                 "QListView\n"
                                 "{\n"
                                 "	background-color: #5c55e9;\n"
                                 "	color: #fff;\n"
                                 "	font-size: 14px;\n"
                                 ""
                                 "	font-weight: bold;\n"
                                 "	show-decoration-selected: 0;\n"
                                 "	border-radius: 4px;\n"
                                 "	padding-left: -15px;\n"
                                 "	padding-right: -15px;\n"
                                 "	padding-top: 5px;\n"
                                 "\n"
                                 "} \n"
                                 "\n"
                                 "\n"
                                 "QListView:disabled \n"
                                 "{\n"
                                 "	background-color: #5c5c5c;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QListView::item\n"
                                 "{\n"
                                 "	background-color: #454e5e;\n"
                                 "	border: none;\n"
                                 "	padding: 10px;\n"
                                 "	border-radius: 0px;\n"
                                 "	padding-left : 10px;\n"
                                 "	height: 32px;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QListView::item:selected\n"
                                 "{\n"
                                 "	color: #000;\n"
                                 "	background-color: #fff;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QListView::item:!selected\n"
                                 "{\n"
                                 "	color:white;\n"
                                 "	background-color: transparent;\n"
                                 "	border: none;\n"
                                 "	padding-left : 10px;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QListView::item:!selected:hover\n"
                                 "{\n"
                                 "	color: #fff;\n"
                                 "	background-color: #5564f2;\n"
                                 "	border: none;\n"
                                 "	padding-left : 10px;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "/*-----QTreeView-----*/\n"
                                 "QTreeView \n"
                                 "{\n"
                                 "	background-color: #fff;\n"
                                 "	show-decoration-selected: 0;\n"
                                 "	color: #454544;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QT"
                                 "reeView:disabled\n"
                                 "{\n"
                                 "	background-color: #242526;\n"
                                 "	show-decoration-selected: 0;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QTreeView::item \n"
                                 "{\n"
                                 "	border-top-color: transparent;\n"
                                 "	border-bottom-color: transparent;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QTreeView::item:hover \n"
                                 "{\n"
                                 "	background-color: #bcbdbb;\n"
                                 "	color: #000;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QTreeView::item:selected \n"
                                 "{\n"
                                 "	background-color: #5c55e9;\n"
                                 "	color: #fff;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QTreeView::item:selected:active\n"
                                 "{\n"
                                 "	background-color: #5c55e9;\n"
                                 "	color: #fff;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QTreeView::item:selected:disabled\n"
                                 "{\n"
                                 "	background-color: #525251;\n"
                                 "	color: #656565;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QTreeView::branch:has-children:!has-siblings:closed,\n"
                                 "QTreeView::branch:closed:has-children:has-siblings \n"
                                 "{\n"
                                 "	image: url(://tree-closed.png);\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "QTreeView::branch:open:has-children:!has-siblings,\n"
                                 "QTreeView::branch:open:has-children:has-siblings  \n"
                                 "{\n"
                                 "	image: url(://tree-open.png);\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "/*"
                                 "-----QTableView & QTableWidget-----*/\n"
                                 "QTableView\n"
                                 "{\n"
                                 "    background-color: #fff;\n"
                                 "	border: 1px solid gray;\n"
                                 "    color: #454544;\n"
                                 "    gridline-color: gray;\n"
                                 "    outline : 0;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QTableView::disabled\n"
                                 "{\n"
                                 "    background-color: #242526;\n"
                                 "    border: 1px solid #32414B;\n"
                                 "    color: #656565;\n"
                                 "    gridline-color: #656565;\n"
                                 "    outline : 0;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QTableView::item:hover \n"
                                 "{\n"
                                 "    background-color: #bcbdbb;\n"
                                 "    color: #000;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QTableView::item:selected \n"
                                 "{\n"
                                 "	background-color: #5c55e9;\n"
                                 "    color: #fff;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QTableView::item:selected:disabled\n"
                                 "{\n"
                                 "    background-color: #1a1b1c;\n"
                                 "    border: 2px solid #525251;\n"
                                 "    color: #656565;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QTableCornerButton::section\n"
                                 "{\n"
                                 "	background-color: #ced5e3;\n"
                                 "	border: none;\n"
                                 "    color: #fff;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QHeaderView::section\n"
                                 "{\n"
                                 "	color: #2a547f;\n"
                                 "	border: 0px;\n"
                                 "	background-color: #ce"
                                 "d5e3;\n"
                                 "	padding: 5px;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QHeaderView::section:disabled\n"
                                 "{\n"
                                 "    background-color: #525251;\n"
                                 "    color: #656565;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QHeaderView::section:checked\n"
                                 "{\n"
                                 "    color: #fff;\n"
                                 "    background-color: #5c55e9;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QHeaderView::section:checked:disabled\n"
                                 "{\n"
                                 "    color: #656565;\n"
                                 "    background-color: #525251;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QHeaderView::section::vertical::first,\n"
                                 "QHeaderView::section::vertical::only-one\n"
                                 "{\n"
                                 "    border-top: 1px solid #353635;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QHeaderView::section::vertical\n"
                                 "{\n"
                                 "    border-top: 1px solid #353635;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QHeaderView::section::horizontal::first,\n"
                                 "QHeaderView::section::horizontal::only-one\n"
                                 "{\n"
                                 "    border-left: 1px solid #353635;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QHeaderView::section::horizontal\n"
                                 "{\n"
                                 "    border-left: 1px solid #353635;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "/*-----QScrollBar-----*/\n"
                                 "QScrollBar:horizontal \n"
                                 "{\n"
                                 "    background-color: transpare"
                                 "nt;\n"
                                 "    height: 8px;\n"
                                 "    margin: 0px;\n"
                                 "    padding: 0px;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QScrollBar::handle:horizontal \n"
                                 "{\n"
                                 "    border: none;\n"
                                 "	min-width: 100px;\n"
                                 "    background-color: #7e92b7;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QScrollBar::add-line:horizontal, \n"
                                 "QScrollBar::sub-line:horizontal,\n"
                                 "QScrollBar::add-page:horizontal, \n"
                                 "QScrollBar::sub-page:horizontal \n"
                                 "{\n"
                                 "    width: 0px;\n"
                                 "    background-color: #d8dce6;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QScrollBar:vertical \n"
                                 "{\n"
                                 "    background-color: transparent;\n"
                                 "    width: 8px;\n"
                                 "    margin: 0;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QScrollBar::handle:vertical \n"
                                 "{\n"
                                 "    border: none;\n"
                                 "	min-height: 100px;\n"
                                 "    background-color: #7e92b7;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QScrollBar::add-line:vertical, \n"
                                 "QScrollBar::sub-line:vertical,\n"
                                 "QScrollBar::add-page:vertical, \n"
                                 "QScrollBar::sub-page:vertical \n"
                                 "{\n"
                                 "    height: 0px;\n"
                                 "    background-color: #d8dce6;\n"
                                 "\n"
                                 "}\n"
                                 "")
        self.actionClearCaches = QAction(MainWindow)
        self.actionClearCaches.setObjectName(u"actionClearCaches")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.apiBox = QGroupBox(self.centralwidget)
        self.apiBox.setObjectName(u"apiBox")
        self.apiBox.setGeometry(QRect(20, 10, 311, 91))
        self.apiBox.setStyleSheet(u"color: rgb(92, 85, 233);")
        self.gTranslate = QRadioButton(self.apiBox)
        self.gTranslate.setObjectName(u"gTranslate")
        self.gTranslate.setGeometry(QRect(30, 20, 111, 17))
        self.gTranslate.setStyleSheet(u"color: rgb(92, 85, 233);")
        self.gTranslate.setChecked(True)
        self.awsTranslate = QRadioButton(self.apiBox)
        self.awsTranslate.setObjectName(u"awsTranslate")
        self.awsTranslate.setGeometry(QRect(30, 40, 101, 17))
        self.awsTranslate.setStyleSheet(u"color: rgb(92, 85, 233);")
        self.deepTranslate = QRadioButton(self.apiBox)
        self.deepTranslate.setObjectName(u"deepTranslate")
        self.deepTranslate.setGeometry(QRect(30, 60, 101, 17))
        self.deepTranslate.setStyleSheet(u"color: rgb(92, 85, 233);")
        self.translateBtn = QPushButton(self.centralwidget)
        self.translateBtn.setObjectName(u"translateBtn")
        self.translateBtn.setGeometry(QRect(250, 480, 81, 34))
        self.translateBtn.setStyleSheet(u"background-color: rgb(255, 191, 191);\n"
                                        "background-color: rgb(255, 0, 58);")
        self.fileText = QLineEdit(self.centralwidget)
        self.fileText.setObjectName(u"fileText")
        self.fileText.setGeometry(QRect(110, 140, 151, 21))
        self.chooseFileBtn = QPushButton(self.centralwidget)
        self.chooseFileBtn.setObjectName(u"chooseFileBtn")
        self.chooseFileBtn.setGeometry(QRect(270, 140, 61, 34))
        self.statusBox = QTextBrowser(self.centralwidget)
        self.statusBox.setObjectName(u"statusBox")
        self.statusBox.setGeometry(QRect(30, 310, 301, 161))
        self.statusBox.setStyleSheet(u"color: rgb(40, 40, 40);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(31, 140, 31, 21))
        self.threadSpinner = QSpinBox(self.centralwidget)
        self.threadSpinner.setObjectName(u"threadSpinner")
        self.threadSpinner.setGeometry(QRect(110, 260, 151, 21))
        self.threadSpinner.setValue(1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 260, 61, 21))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 110, 51, 21))
        self.sourceText = QLineEdit(self.centralwidget)
        self.sourceText.setObjectName(u"sourceText")
        self.sourceText.setGeometry(QRect(110, 110, 151, 21))
        self.chooseSave = QPushButton(self.centralwidget)
        self.chooseSave.setObjectName(u"chooseSave")
        self.chooseSave.setGeometry(QRect(270, 170, 61, 34))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(31, 170, 51, 21))
        self.outputText = QLineEdit(self.centralwidget)
        self.outputText.setObjectName(u"outputText")
        self.outputText.setGeometry(QRect(110, 170, 151, 21))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 210, 81, 21))
        self.langsBox = CheckableComboBox(self.centralwidget)
        self.langsBox.setObjectName(u"langsBox")
        self.langsBox.setGeometry(QRect(110, 210, 151, 22))
        self.allCheck = QCheckBox(self.centralwidget)
        self.allCheck.setObjectName(u"allCheck")
        self.allCheck.setGeometry(QRect(270, 210, 70, 21))
        self.allCheck.setChecked(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 350, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionClearCaches)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Strings Translator", None))
        self.actionClearCaches.setText(QCoreApplication.translate("MainWindow", u"Clear Caches", None))
        # if QT_CONFIG(tooltip)
        self.actionClearCaches.setToolTip(
            QCoreApplication.translate("MainWindow", u"Clears Information File , To Start Translation From Beginning",
                                       None))
        # endif // QT_CONFIG(tooltip)
        self.apiBox.setTitle(QCoreApplication.translate("MainWindow", u"Translation API", None))
        self.gTranslate.setText(QCoreApplication.translate("MainWindow", u"Google Translate", None))
        self.awsTranslate.setText(QCoreApplication.translate("MainWindow", u"AWS Translate", None))
        self.deepTranslate.setText(QCoreApplication.translate("MainWindow", u"Deep Translate", None))
        self.translateBtn.setText(QCoreApplication.translate("MainWindow", u"Translate", None))
        self.chooseFileBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.statusBox.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"All Set , Click Translate to Start !", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Threads", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Source", None))
        self.sourceText.setText(QCoreApplication.translate("MainWindow", u"en", None))
        self.chooseSave.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Output", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Languages", None))
        self.allCheck.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi
