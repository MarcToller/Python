# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formPrincipal.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableView,
    QWidget)

class Ui_formPrincipal(object):
    def setupUi(self, formPrincipal):
        if not formPrincipal.objectName():
            formPrincipal.setObjectName(u"formPrincipal")
        formPrincipal.resize(521, 650)
        self.centralwidget = QWidget(formPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableViewTodos = QTableView(self.centralwidget)
        self.tableViewTodos.setObjectName(u"tableViewTodos")
        self.tableViewTodos.setGeometry(QRect(10, 10, 501, 561))
        self.pushButtonIniciar = QPushButton(self.centralwidget)
        self.pushButtonIniciar.setObjectName(u"pushButtonIniciar")
        self.pushButtonIniciar.setGeometry(QRect(30, 581, 75, 24))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(130, 581, 75, 24))
        formPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(formPrincipal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 521, 22))
        formPrincipal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(formPrincipal)
        self.statusbar.setObjectName(u"statusbar")
        formPrincipal.setStatusBar(self.statusbar)

        self.retranslateUi(formPrincipal)

        QMetaObject.connectSlotsByName(formPrincipal)
    # setupUi

    def retranslateUi(self, formPrincipal):
        formPrincipal.setWindowTitle(QCoreApplication.translate("formPrincipal", u"MainWindow", None))
        self.pushButtonIniciar.setText(QCoreApplication.translate("formPrincipal", u"Iniciar", None))
        self.pushButton_2.setText(QCoreApplication.translate("formPrincipal", u"Parar", None))
    # retranslateUi

