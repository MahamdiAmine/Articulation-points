#!/usr/bin/env python3                                    #
# -.- coding: utf-8 -.-                                   #
###########################################################

from PyQt5 import QtCore, QtWidgets


class Ui_Dialog(object):
    #this class represents the Frame needed to ask the user to enter the max
    #NOTE: the default value of max weight is zero
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setStyleSheet("QPushButton:hover {background-color: #161CCB;color: #000000;qproperty-iconSize: 34px;}")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(230, 100, 131, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 90, 171, 41))
        self.label.setObjectName("label")
        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Please enter the number of nodes : "))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic;\"> Number of nodes :</span></p></body></html>"))

    def accept(self):
        txt=0
        try:
            txt = int(self.lineEdit.text())
        except Exception:
            print("Oops! That was no valid number! Try again...")
        return max(txt,0)


