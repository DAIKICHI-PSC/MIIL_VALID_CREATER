# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MIIL_VALID_CREATER_GUI.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(431, 642)
        MainWindow.setMinimumSize(QSize(431, 642))
        MainWindow.setMaximumSize(QSize(431, 642))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label1 = QLabel(self.centralwidget)
        self.label1.setObjectName(u"label1")
        self.label1.setEnabled(False)
        self.label1.setGeometry(QRect(680, 280, 281, 141))
        self.groupBox1 = QGroupBox(self.centralwidget)
        self.groupBox1.setObjectName(u"groupBox1")
        self.groupBox1.setGeometry(QRect(10, 80, 211, 81))
        self.pushButton1 = QPushButton(self.groupBox1)
        self.pushButton1.setObjectName(u"pushButton1")
        self.pushButton1.setGeometry(QRect(10, 17, 93, 51))
        self.pushButton2 = QPushButton(self.groupBox1)
        self.pushButton2.setObjectName(u"pushButton2")
        self.pushButton2.setEnabled(False)
        self.pushButton2.setGeometry(QRect(110, 17, 93, 51))
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(290, 170, 131, 421))
        self.listWidget3 = QListWidget(self.groupBox)
        self.listWidget3.setObjectName(u"listWidget3")
        self.listWidget3.setGeometry(QRect(10, 20, 111, 261))
        self.pushButton9 = QPushButton(self.groupBox)
        self.pushButton9.setObjectName(u"pushButton9")
        self.pushButton9.setGeometry(QRect(10, 320, 111, 28))
        self.pushButton8 = QPushButton(self.groupBox)
        self.pushButton8.setObjectName(u"pushButton8")
        self.pushButton8.setGeometry(QRect(10, 290, 111, 28))
        self.pushButton12 = QPushButton(self.groupBox)
        self.pushButton12.setObjectName(u"pushButton12")
        self.pushButton12.setGeometry(QRect(10, 350, 111, 28))
        self.pushButton14 = QPushButton(self.groupBox)
        self.pushButton14.setObjectName(u"pushButton14")
        self.pushButton14.setGeometry(QRect(10, 380, 111, 28))
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(150, 170, 131, 421))
        self.listWidget2 = QListWidget(self.groupBox_2)
        self.listWidget2.setObjectName(u"listWidget2")
        self.listWidget2.setGeometry(QRect(10, 20, 111, 261))
        self.pushButton6 = QPushButton(self.groupBox_2)
        self.pushButton6.setObjectName(u"pushButton6")
        self.pushButton6.setGeometry(QRect(10, 290, 111, 28))
        self.pushButton7 = QPushButton(self.groupBox_2)
        self.pushButton7.setObjectName(u"pushButton7")
        self.pushButton7.setGeometry(QRect(10, 320, 111, 28))
        self.pushButton11 = QPushButton(self.groupBox_2)
        self.pushButton11.setObjectName(u"pushButton11")
        self.pushButton11.setGeometry(QRect(10, 350, 111, 28))
        self.pushButton13 = QPushButton(self.groupBox_2)
        self.pushButton13.setObjectName(u"pushButton13")
        self.pushButton13.setGeometry(QRect(10, 380, 111, 28))
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 170, 131, 421))
        self.listWidget1 = QListWidget(self.groupBox_3)
        self.listWidget1.setObjectName(u"listWidget1")
        self.listWidget1.setGeometry(QRect(10, 20, 111, 261))
        self.pushButton4 = QPushButton(self.groupBox_3)
        self.pushButton4.setObjectName(u"pushButton4")
        self.pushButton4.setGeometry(QRect(10, 290, 111, 28))
        self.pushButton5 = QPushButton(self.groupBox_3)
        self.pushButton5.setObjectName(u"pushButton5")
        self.pushButton5.setGeometry(QRect(10, 320, 111, 28))
        self.pushButton10 = QPushButton(self.groupBox_3)
        self.pushButton10.setObjectName(u"pushButton10")
        self.pushButton10.setGeometry(QRect(10, 350, 111, 28))
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 10, 411, 61))
        self.pushButton3 = QPushButton(self.groupBox_4)
        self.pushButton3.setObjectName(u"pushButton3")
        self.pushButton3.setGeometry(QRect(310, 20, 93, 28))
        self.lineEdit1 = QLineEdit(self.groupBox_4)
        self.lineEdit1.setObjectName(u"lineEdit1")
        self.lineEdit1.setEnabled(False)
        self.lineEdit1.setGeometry(QRect(10, 20, 291, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 431, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MIIL VALID CREATER", None))
        self.label1.setText("")
        self.groupBox1.setTitle(QCoreApplication.translate("MainWindow", u"PICTURE", None))
        self.pushButton1.setText(QCoreApplication.translate("MainWindow", u"SHOW", None))
        self.pushButton2.setText(QCoreApplication.translate("MainWindow", u"HIDE", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"VALID", None))
        self.pushButton9.setText(QCoreApplication.translate("MainWindow", u"TO FILE", None))
        self.pushButton8.setText(QCoreApplication.translate("MainWindow", u"TO TRAIN", None))
        self.pushButton12.setText(QCoreApplication.translate("MainWindow", u"SORT", None))
        self.pushButton14.setText(QCoreApplication.translate("MainWindow", u"CHECK PIC", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"TRAIN", None))
        self.pushButton6.setText(QCoreApplication.translate("MainWindow", u"TO VALID", None))
        self.pushButton7.setText(QCoreApplication.translate("MainWindow", u"TO FILE", None))
        self.pushButton11.setText(QCoreApplication.translate("MainWindow", u"SORT", None))
        self.pushButton13.setText(QCoreApplication.translate("MainWindow", u"CHECK PIC", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"FILE", None))
        self.pushButton4.setText(QCoreApplication.translate("MainWindow", u"TO TRAIN", None))
        self.pushButton5.setText(QCoreApplication.translate("MainWindow", u"TO VALID", None))
        self.pushButton10.setText(QCoreApplication.translate("MainWindow", u"SORT", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"PARAMETER FILE", None))
        self.pushButton3.setText(QCoreApplication.translate("MainWindow", u"OPEN", None))
    # retranslateUi

