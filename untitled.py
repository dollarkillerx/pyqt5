# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Formc(object):
    def setupUi(self, Formc):
        Formc.setObjectName("Formc")
        Formc.resize(439, 338)
        self.onebutton = QtWidgets.QPushButton(Formc)
        self.onebutton.setGeometry(QtCore.QRect(170, 190, 75, 23))
        self.onebutton.setObjectName("onebutton")

        self.retranslateUi(Formc)
        QtCore.QMetaObject.connectSlotsByName(Formc)

    def retranslateUi(self, Formc):
        _translate = QtCore.QCoreApplication.translate
        Formc.setWindowTitle(_translate("Formc", "你好Qt"))
        self.onebutton.setText(_translate("Formc", "PushButton"))
