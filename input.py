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
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.size = QtWidgets.QPushButton(self.widget1)
        self.size.setMaximumSize(QtCore.QSize(120, 30))
        self.size.setObjectName("size")
        self.verticalLayout.addWidget(self.size)

        self.tokens_spin = QtWidgets.QSpinBox(self.widget1)
        self.tokens_spin.setMaximumSize(QtCore.QSize(120, 30))
        self.tokens_spin.setMaximum(1000000)
        self.tokens_spin.setObjectName("tokens_spin")
        self.verticalLayout.addWidget(self.tokens_spin)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setMaximumSize(QtCore.QSize(120, 30))
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
        self.error.setText("ay klam")
        self.error.hide()
        self.container.addWidget(self.widget1)
        self.verticalLayout_2.addWidget(self.label_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(input_window)
        self.layoutWidget1.setGeometry(QtCore.QRect(80, 140, 241, 234))
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
        self.label.setText(_translate("input_window", "Memory size"))
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
    # def mem_init(self, mem_tokens):
    #     mem_segments = []
    #     seg_base = 0
    #     old = Process()
    #     for row in range (0, len(mem_tokens)):
    #         length = mem_tokens[row][0] - seg_base
    #         if(length > 0):
    #             mem_segments.append(Segment("Old Process", length, old, seg_base, False))
    #             seg_base = seg_base + length
    #         mem_segments.append(Segment("hole", mem_tokens[row][1], 0, mem_tokens[row][0], True))
    #         seg_base = seg_base + mem_tokens[row][1]
    #     length = int(self.size.text()) - seg_base
    #     if(length > 0):
    #         mem_segments.append(Segment("Old Process", length, old, seg_base, False))
    #     return mem_segments
    def clear(self):
        self.tokens_spin.setValue(0)
    def browse(self):
        self.tokens_spin.setValue(0)
        self.tokens_spin.setEnabled(0)
        filePath,_ = QFileDialog.getOpenFileName(input_window, "Open File", "~/Downloads/parser/Recursive-descent-parser", "*.txt")
        print(filePath)
        file = open(filePath, "r")
        tokens_list = list()
        for x in file:
            # print(x)
            x = x[0:len(x) - 1]
            line = x.split(",")
            # print(line[1])
            tokens_list.append(token(line[0], line[1]))
        initialize(tokens_list)
        for i in tokens_list:
            print(i.value, i.type)
        print(len(tokens_list))
        stmt_sequence(-1,-1,0)
        correction()
        draw(nodelist)
    def read_input(self):
        self.tokens_spin.setEnabled(1)
        error = ""
        # memory_size = str(self.size.text())
        # if(not memory_size.isdigit()):
        #     error = "Memory size must be a postive integer"
        # else:
        #     memory_size = int(memory_size)
        #     if(memory_size <= 0):
        #         error = "Memory size must be greater than 0"
        if(error == ""):
            tokens_list = list()
            no_tokens = int(self.tokens_spin.text())
            for row in range (0,no_tokens):
                token_type = str(self.tableWidget.item(row, 1).text())
                token_value = str(self.tableWidget.item(row, 0).text())

                # if(not hole_base.isdigit()):
                #     error = "Hole base must be a postive integer"
                #     break
                # else:
                #     hole_base = int(hole_base)
                #     if(hole_base < 0):
                #         error = "Hole base must be a postive integer"
                #         break
                #     if(row > 0):
                #         if(hole_base <= (tokens[row-1][0] + tokens[row-1][1])):
                #             error ="tokens must be separated"
                #             break
                # if(not hole_size.isdigit()):
                #     error = "Hole size must be a postive integer"
                #     break
                # else:
                #     hole_size = int(hole_size)
                #     if(hole_size <= 0):
                #         error = "Hole size must be greater than 0"
                #         break
                #     if(hole_size + hole_base > memory_size):
                #         error = "Out of bounds"
                #         break
                tokens_list.append(token(token_value, token_type))
            if(error == ""):
                self.error.hide()
                # tokens_list=[token('read','READ'),token ('x','IDENTIFIER'),token (';','SEMICOLON')]
                # ,token('if','IF'),
                # token('0','NUMBER'),token('<','LESSTHAN'),token ('x','IDENTIFIER'),token('then','THEN'),token ('fact','IDENTIFIER')
                # ,token (':=','ASSIGN'),token('1','NUMBER'),token (';','SEMICOLON'),token('repeat','REPEAT'),token ('fact','IDENTIFIER')
                # ,token (':=','ASSIGN'),token ('fact','IDENTIFIER'),token ('+','PLUS'),token ('x','IDENTIFIER'),token ('*','MULT'),token ('y','IDENTIFIER'),token ('-','MINUS'),token ('z','IDENTIFIER'),token ('+','PLUS'),token ('t','IDENTIFIER'),token ('/','DIV'),token ('g','IDENTIFIER'),token (';','SEMICOLON'),token ('x','IDENTIFIER'),token (':=','ASSIGN'),token ('x','IDENTIFIER'),token ('-','MINUS'),token('1','NUMBER')
                # ,token('until','UNTIL'),token ('x','IDENTIFIER'),token ('=','EQUAL'),token('0','NUMBER'),token (';','SEMICOLON'),token('write','WRITE'),token ('fact','IDENTIFIER'),token ('end','END')]
                initialize(tokens_list)
                for i in tokens_list:
                    print(i.value, i.type)
                print(len(tokens_list))
                stmt_sequence(-1,-1,0)
                correction()
                draw(nodelist)
                return
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