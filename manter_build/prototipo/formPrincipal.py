# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormPrincipal.ui'
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
from PySide6.QtWidgets import (QApplication, QListView, QMainWindow, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_formPrincipal(object):
    def setupUi(self, formPrincipal):
        if not formPrincipal.objectName():
            formPrincipal.setObjectName(u"formPrincipal")
        formPrincipal.resize(309, 363)
        self.centralwidget = QWidget(formPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.listViewTodos = QListView(self.centralwidget)
        self.listViewTodos.setObjectName(u"listViewTodos")
        self.listViewTodos.setGeometry(QRect(20, 10, 256, 291))
        formPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(formPrincipal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 309, 22))
        formPrincipal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(formPrincipal)
        self.statusbar.setObjectName(u"statusbar")
        formPrincipal.setStatusBar(self.statusbar)

        self.retranslateUi(formPrincipal)

        QMetaObject.connectSlotsByName(formPrincipal)
    # setupUi

    def retranslateUi(self, formPrincipal):
        formPrincipal.setWindowTitle(QCoreApplication.translate("formPrincipal", u"MainWindow", None))
    # retranslateUi

