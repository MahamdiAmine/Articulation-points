#!/usr/bin/env python3                                    #
# -.- coding: utf-8 -.-                                   #
###########################################################

import time
from PyQt5.QtWidgets import QTableWidget, QWidget, QHBoxLayout, QHeaderView
from ui.Ui_nodeNbr import Ui_Dialog as DialogForm
from ui.Ui_Error import Ui_Error as ErrorForm
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def __init__(self):
        self.table = QTableWidget()
        self.css = '''/*  Author mahamdi amine
                           Github https://github.com/MahamdiAmine */

                            QPushButton:hover {
                                    background-color: #161CCB;
                                    color: #000000; 
                                    qproperty-iconSize: 34px;     
                            }

                           QWidget { 
                                /*background-color: C65528;*/
                                color: rgba(39, 102, 21, 0.88)
                            }

                            QPushButton:pressed {
                                background-color: #bbdefb;
                            }
                            '''
        self.stylesheetTables = "QHeaderView::section{Background-color:#224966; border - radius: 14 px;}"
        css = '''/*  Author mahamdi amine
                           Github https://github.com/MahamdiAmine */

                            QPushButton:hover {
                                    background-color: #161CCB;
                                    color: #000000; 
                                    qproperty-iconSize: 34px;     
                            }

                           QWidget { 
                                /*background-color: C65528;*/
                                color: rgba(39, 102, 21, 0.88)
                            }

                            QPushButton:pressed {
                                background-color: #bbdefb;
                            }
                            '''
        # self.matrix=[]
        self.nodeNbr=6

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(734, 572)
        MainWindow.setStyleSheet(self.css)# apply the styleSheet
        self.matrix = [[0 for x in range(self.nodeNbr)] for x in range(self.nodeNbr)]
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.drawButton = QtWidgets.QPushButton(self.centralwidget)
        self.drawButton.setGeometry(QtCore.QRect(50, 230, 161, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drawButton.sizePolicy().hasHeightForWidth())
        self.drawButton.setSizePolicy(sizePolicy)
        self.drawButton.setObjectName("drawButton")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(610, 480, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Carlito")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.exitButton.setFont(font)
        self.exitButton.setObjectName("exitButton")
        self.calculateButton = QtWidgets.QPushButton(self.centralwidget)
        self.calculateButton.setGeometry(QtCore.QRect(50, 300, 331, 61))
        self.calculateButton.setObjectName("calculateLabel")
        # self.calculateButton.hide()
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(310, 440, 61, 31))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber.hide()
        self.copyrightLabel = QtWidgets.QLabel(self.centralwidget)
        self.copyrightLabel.setGeometry(QtCore.QRect(150, 520, 431, 31))
        self.copyrightLabel.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.copyrightLabel.setOpenExternalLinks(True)
        self.copyrightLabel.setObjectName("copyrightLabel")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(10, 10, 701, 61))
        self.titleLabel.setObjectName("titleLabel")
        self.articulationPointLabel = QtWidgets.QLabel(self.centralwidget)
        self.articulationPointLabel.setGeometry(QtCore.QRect(390, 430, 141, 41))
        self.articulationPointLabel.setObjectName("apLabel")
        self.articulationPointLabel.hide()
        self.progressBarLabel = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBarLabel.setGeometry(QtCore.QRect(170, 390, 391, 23))
        self.progressBarLabel.setProperty("value", 24)
        self.progressBarLabel.setObjectName("progressBarLabel")
        self.progressBarLabel.hide()
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(80, 70, 591, 81))
        self.textBrowser.setObjectName("textBrowser")
        self.nodeNbrButton = QtWidgets.QPushButton(self.centralwidget)
        self.nodeNbrButton.setGeometry(QtCore.QRect(220, 170, 261, 31))
        self.nodeNbrButton.setObjectName("viewGraphButton")
        self.thereisLaber = QtWidgets.QLabel(self.centralwidget)
        self.thereisLaber.setGeometry(QtCore.QRect(220, 430, 81, 41))
        self.thereisLaber.setObjectName("thereisLaber")
        self.viewAPButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewAPButton.setGeometry(QtCore.QRect(430, 280, 231, 61))
        self.viewAPButton.setObjectName("viewAPButton")
        self.viewAPButton.hide()
        self.viewGraphButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewGraphButton.setGeometry(QtCore.QRect(430, 280, 231, 61))
        self.viewGraphButton.setObjectName("viewGraphButton")
        self.viewGraphButton.hide()
        self.nodenbrLabel = QtWidgets.QLabel(self.centralwidget)
        self.nodenbrLabel.setGeometry(QtCore.QRect(510, 168, 67, 41))
        self.nodenbrLabel.setObjectName("nodenbrLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TP 2: Articulation points in graph."))
        self.drawButton.setText(_translate("MainWindow", "Draw the graph -->"))
        self.drawButton.clicked.connect(self.drawGraph)
        self.drawButton.hide()
        self.exitButton.setText(_translate("MainWindow", "EXIT"))
        self.exitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.calculateButton.setText(_translate("MainWindow", "Calculate the number of articulation points -->"))
        self.calculateButton.clicked.connect(self.calculate)
        self.calculateButton.hide()
        self.copyrightLabel.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"https://github.com/MahamdiAmine/MahamdiAmine.github.io/blob/master/LICENSE.md\"><span style=\" text-decoration: underline; color:#0000ff;\">Copyright © 2018 Mahamdi Mohammed and Boukabene Randa .</span></a></p><p><br/></p></body></html>"))
        self.titleLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">TP 2 :  Calculate the number of articulation points in non oriented graph .</span></p></body></html>"))
        self.articulationPointLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">  articulation points </span></p></body></html>"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   Hence the name, One Music is the best free band website template which you can use for all sorts of music projects of your own. Along with covering band sites, you can also be a solo artist or even a small agency and enjoy the benefits of the amazing One Music. It is an HTML website template, fully responsive, flexible, SEO optimized and cross-browser compatible. One Music has a modern web design with a zoom-in slideshow, loads content on the scroll and includes an audio player.</p></body></html>"))
        self.nodeNbrButton.setText(_translate("MainWindow", "Please Enter the number of nodes -->"))
        self.nodeNbrButton.clicked.connect(self.dialog_nodeNbr)
        self.thereisLaber.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">There is :</span></p></body></html>"))
        self.thereisLaber.hide()
        self.viewAPButton.setText(_translate("MainWindow", "View the articulation points -->"))
        self.viewGraphButton.setText(_translate("MainWindow", "View the graph -->"))
        self.nodenbrLabel.setStyleSheet("font: 30pt Comic Sans MS")
        self.nodenbrLabel.setText(_translate("MainWindow", str(self.nodeNbr)))


    def dialog_nodeNbr(self):
        #open the Frame that asks the user tp enter the max value
        self.nodenbrLabel.setSizePolicy(30,30)
        self.nodenbrLabel.setText(str(self.nodeNbr))
        self.nodenbrLabel.show()
        self.calculateButton.show()
        self.drawButton.show()
        dialog = QtWidgets.QDialog()
        dialog.setWindowIcon(QtGui.QIcon("./img/check_mark.png"))
        dialog.ui = DialogForm()
        dialog.ui.setupUi(dialog)
        dialog.setFixedSize(415,320)
        dialog.exec_()
        dialog.show()
        text=dialog.ui.accept()
        self.nodeNbr=text
        self.nodenbrLabel.setText(str(text))

    def openError(self):
        #open the error caused by invalid number entered by the user
        dialog = QtWidgets.QDialog()
        dialog.ui = ErrorForm()
        dialog.ui.setupUi(dialog)
        dialog.setFixedSize(415,320)
        dialog.exec_()
        dialog.show()

    def drawGraph(self):
        #setup the table when the user wants the add objects
        def __init__(self, parent=None):
            super().__init__(parent)
        self.table.setWindowIcon(QtGui.QIcon("./img/check_mark.png"))
        self.table.setFixedSize(700,600)#fix the size
        self.table.setWindowTitle("Draw your graph ")
        self.table.setColumnCount(self.nodeNbr)
        self.table.setRowCount(self.nodeNbr)
        header_labels=[]
        for counter in range(0,self.nodeNbr):
            header_labels.insert(counter,str(counter))
            self.table.horizontalHeader().setSectionResizeMode(counter, QHeaderView.Stretch)
            self.table.verticalHeader().setSectionResizeMode(counter, QHeaderView.Stretch)
        self.table.setHorizontalHeaderLabels(header_labels)
        self.table.setVerticalHeaderLabels(header_labels)
        self.table.setStyleSheet(self.stylesheetTables)
        for row in range(0, self.nodeNbr):
            for col in range(0, self.nodeNbr):
                check_box = QtWidgets.QCheckBox(parent=self.table)
                #if the check box state is changed ,onStateChanged method is invoked
                check_box.clicked.connect(lambda checked, row_pos=row, col_pos=col: self.onStateChanged(checked, row_pos, col_pos))
                cell_widget = QWidget()
                lay_out = QHBoxLayout(cell_widget)
                lay_out.addWidget(check_box)
                lay_out.setAlignment(QtCore.Qt.AlignCenter)
                lay_out.setContentsMargins(0, 0, 0, 0)
                cell_widget.setLayout(lay_out)
                self.table.setCellWidget(row, col, cell_widget)
        self.table.show()

    def onStateChanged(self, checked, row, col):
        #handle the event when the user check the check box
        # create new cell to update the table i.e:make the table symmetrical
        cell_widget = QWidget()
        lay_out = QHBoxLayout(cell_widget)
        cb = QtWidgets.QCheckBox(parent=self.table)
        if checked:
            value=1
            cb.setChecked(True)
        else:
            value=0
            cb.setChecked(False)
        self.matrix[row][col] = value
        lay_out.addWidget(cb)
        lay_out.setAlignment(QtCore.Qt.AlignCenter)
        lay_out.setContentsMargins(0, 0, 0, 0)
        cell_widget.setLayout(lay_out)
        self.table.setCellWidget(col, row, cell_widget)

    def calculate(self):
        # calculate the results and update the progress bar
        self.progressBarLabel.show()
        for i in range(33):  # progress bar level =33
            time.sleep(0.01)
            self.progressBarLabel.setValue(i)
        self.lcdNumber.show()
        self.thereisLaber.show()
        self.articulationPointLabel.show()