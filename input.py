# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'input.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtCore


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QFrame
from PyQt5.QtWidgets import QLineEdit, QFileDialog
from parser import stmt_sequence, correction, token, nodelist, initialize
from syntaxTree import draw
import math
class Ui_input_window(object):
    def setupUi(self, input_window):
        input_window.setObjectName("input_window")
        input_window.resize(414, 408)
        self.windowLayout = QtWidgets.QVBoxLayout(input_window)
        self.windowLayout.setObjectName("windowLayout")
        self.container = QtWidgets.QVBoxLayout()
        self.container.setObjectName("container")
        self.widget1 = QtWidgets.QWidget()
        self.widget1.setObjectName("widget1")
        self.widget1.maximumHeight()
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 30, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.size = QtWidgets.QPushButton(self.widget1)
        self.size.setMaximumSize(QtCore.QSize(80, 30))
        self.size.setObjectName("size")
        self.verticalLayout.addWidget(self.size)

        self.tokens_spin = QtWidgets.QSpinBox(self.widget1)
        self.tokens_spin.setMaximumSize(QtCore.QSize(80, 30))
        self.tokens_spin.setMaximum(1000000)
        self.tokens_spin.setObjectName("tokens_spin")
        self.verticalLayout.addWidget(self.tokens_spin)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setMaximumSize(QtCore.QSize(170, 30))
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setMaximumSize(QtCore.QSize(125, 30))
        self.label_2.setObjectName("label_2")
        self.error = QtWidgets.QLabel(input_window)
        self.error.setAlignment(QtCore.Qt.AlignCenter)
        self.error.setGeometry(QtCore.QRect(0, 10, 400, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setItalic(False)
        self.error.setFont(font)
        self.error.setObjectName("label")
        self.error.setStyleSheet("color: red")
        self.label.setStyleSheet("color: red")
        self.error.setText("All fields are required")
        self.error.hide()
        self.container.addWidget(self.widget1)
        self.verticalLayout_2.addWidget(self.label_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(input_window)
        self.layoutWidget1.setGeometry(QtCore.QRect(90, 140, 241, 234))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.layoutWidget1)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(113)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setMinimumSectionSize(21)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        
        self.clearButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.clearButton.setObjectName("clearButton")
        self.verticalLayout_3.addWidget(self.clearButton)

        self.container.addWidget(self.layoutWidget1)
        self.windowLayout.addLayout(self.container)
        self.tokens_spin.valueChanged.connect(self.set_rows)
        self.pushButton.clicked.connect(self.read_input)
        self.size.clicked.connect(self.browse)
        self.clearButton.clicked.connect(self.clear)
        self.retranslateUi(input_window)
        QtCore.QMetaObject.connectSlotsByName(input_window)
        input_window.setTabOrder(self.size, self.tokens_spin)
        input_window.setTabOrder(self.tokens_spin, self.tableWidget)
        input_window.setTabOrder(self.tableWidget, self.pushButton)
        input_window.setTabOrder(self.tableWidget, self.clearButton)

    def retranslateUi(self, input_window):
        _translate = QtCore.QCoreApplication.translate
        input_window.setWindowTitle(_translate("input_window", "Input"))
        # self.label.setText(_translate("input_window", "Memory size"))
        self.label_2.setText(_translate("input_window", "Number of tokens"))
        self.pushButton.setText(_translate("input_window", "Draw"))
        self.clearButton.setText(_translate("input_window", "Clear"))
        self.size.setText(_translate("input_window", "Browse"))
        self.tableWidget.horizontalHeaderItem(0).setText("Token value")
        item = self.tableWidget.horizontalHeaderItem(1).setText("Token type")

    def set_rows(self):
        self.tableWidget.setRowCount(self.tokens_spin.value())
        self.tableWidget.show()
        self.pushButton.show()
    def draw_syntax_tree(self,tokens):
        initialize(tokens)
        for i in tokens:
            print(i.value, i.type)
        print(len(tokens))
        stmt_sequence(-1,-1,0)
        correction()
        draw(nodelist)
    def clear(self):
        self.tokens_spin.setValue(0)
        self.tokens_spin.setEnabled(1)
        self.label.setText("")
        self.error.setText("")
        self.error.hide()
        self.filePath = ""
    def browse(self):
        self.filePath,_ = QFileDialog.getOpenFileName(input_window, "Open File", "~/Downloads/parser/Recursive-descent-parser", "*.txt")
        print(self.filePath)
        if(self.filePath != ""):
            self.tokens_spin.setValue(0)
            self.tokens_spin.setEnabled(0)
            files = self.filePath.split("/")
            file_name = files[len(files) - 1]
            self.label.setText(file_name)
    def read_input(self):
        self.tokens_spin.setEnabled(1)
        error = ""
        self.tokens_list = list()
        if(self.label.text() == ""):
            no_tokens = int(self.tokens_spin.text())
            for row in range (0,no_tokens):
                try:
                    token_type = str(self.tableWidget.item(row, 1).text())
                    token_value = str(self.tableWidget.item(row, 0).text())
                except Exception:
                    error = "Invalid Input"
                    break
                if token_type == "" or token_value == "":
                    error = "Invalid Input"
                    break
                self.tokens_list.append(token(token_value, token_type))
        else:
            file = open(self.filePath, "r")
            for x in file:
                x = x[0:len(x) - 1]
                line = x.split(",")
                if len(line) != 2:
                    error = "Invalid Input"
                    break
                for i in range (len(line)):
                    line[i] = line[i].strip()
                self.tokens_list.append(token(line[0], line[1]))
            self.filePath = ""
            self.label.setText("")
        if len(self.tokens_list) == 0:
            error = "Invalid Input"
        if error == "":
            self.error.hide()
            try:
                self.draw_syntax_tree(self.tokens_list)
            except Exception:
                self.error.setText("Syntax error")
                self.error.show()
        else:
            self.error.setText(error)
            self.error.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    input_window= QtWidgets.QWidget()
    ui = Ui_input_window()
    ui.setupUi(input_window)
    input_window.show()
    sys.exit(app.exec_())