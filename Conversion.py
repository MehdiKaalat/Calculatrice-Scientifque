from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class conversionWindow(object):
    def calculatrice(self):
        from calculatrice import Ui_MainWindow
        self.window1 = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window1)
        self.window1.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(610, 900)
        MainWindow.setMinimumSize(QtCore.QSize(610, 900))
        MainWindow.setMaximumSize(QtCore.QSize(610, 900))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 611, 921))
        self.widget.setStyleSheet("background-color: rgb(233, 243, 253);")
        self.widget.setObjectName("widget")
        self.But_Con = QtWidgets.QPushButton(self.widget)
        self.But_Con.setGeometry(QtCore.QRect(200, 330, 230, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.But_Con.setFont(font)
        self.But_Con.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.But_Con.setStyleSheet("border: none;\n"
"margin-right: 3px;\n"
"padding: 5px 0;\n"
"color: rgb(80, 138, 198);\n"
"background-color: rgb(162, 208, 250);\n"
"border-radius:3px;")
        self.But_Con.setObjectName("But_Con")
        self.Label_bin = QtWidgets.QLabel(self.widget)
        self.Label_bin.setGeometry(QtCore.QRect(250, 50, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.Label_bin.setFont(font)
        self.Label_bin.setStyleSheet("background-color: rgb(204, 229, 255);\n"
"border-radius:5px;\n"
"border-color: black;")
        self.Label_bin.setText("")
        self.Label_bin.setObjectName("Label_bin")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.widget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(50, 460, 511, 431))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.But_AC = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.But_AC.sizePolicy().hasHeightForWidth())
        self.But_AC.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.But_AC.setFont(font)
        self.But_AC.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.But_AC.setStyleSheet("background-color: rgb(235, 237, 238);\n"
"border: none;\n"
"background-color:rgb(162, 208, 250);\n"
"color:  rgb(80, 138, 198);\n"
"border-radius:3px;\n"
"padding: 3px 0;")
        self.But_AC.setObjectName("But_AC")
        self.gridLayout_2.addWidget(self.But_AC, 5, 0, 1, 1)
        self.But_5 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.But_5.sizePolicy().hasHeightForWidth())
        self.But_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.But_5.setFont(font)
        self.But_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.But_5.setStyleSheet("background-color: rgb(235, 237, 238);\n"
"border: none;\n"
"background-color: rgb(204, 229, 255);\n"
"color: rgb(24, 62, 99);\n"
"border-radius:3px;\n"
"padding: 3px 0;")
        self.But_5.setObjectName("But_5")
        self.gridLayout_2.addWidget(self.But_5, 3, 1, 1, 1)
        self.But_6 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.But_6.sizePolicy().hasHeightForWidth())
        self.But_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.But_6.setFont(font)
        self.But_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.But_6.setStyleSheet("background-color: rgb(235, 237, 238);\n"
"border: none;\n"
"background-color: rgb(204, 229, 255);\n"
"color: rgb(24, 62, 99);\n"
"border-radius:3px;\n"
"padding: 3px 0;")
        self.But_6.setObjectName("But_6")
        self.gridLayout_2.addWidget(self.But_6, 3, 2, 1, 1)
        self.But_4 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.But_4.sizePolicy().hasHeightForWidth())
        self.But_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.But_4.setFont(font)
        self.But_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.But_4.setStyleSheet("background-color: rgb(235, 237, 238);\n"
"border: none;\n"
"background-color: rgb(204, 229, 255);\n"
"color: rgb(24, 62, 99);\n"
"border-radius:3px;\n"
"padding: 3px 0;")
        self.But_4.setObjectName("But_4")
        self.gridLayout_2.addWidget(self.But_4, 3, 0, 1, 1)
        self.But_B = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.But_B.sizePolicy().hasHeightForWidth())
        self.But_B.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.But_B.setFont(font)
        self.But_B.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.But_B.setStyleSheet("background-color: rgb(235, 237, 238);\n"
"border: none;\n"
"background-color: rgb(204, 229, 255);\n"
"color: rgb(24, 62, 99);\n"
"border-radius:3px;\n"
"padding: 3px 0;")
        self.But_B.setObjectName("But_B")
        self.gridLayout_2.addWidget(self.But_B, 1, 1, 1, 1)
        self.But_8 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.But_8.sizePolicy().hasHeightForWidth())
        self.But_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.But_8.setFont(font)
        self.But_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.But_8.setStyleSheet("background-color: rgb(235, 237, 238);\n"
"border: none;\n"
"background-color: rgb(204, 229, 255);\n"
"color: rgb(24, 62, 99);\n"
"border-radius:3px;\n"
"padding: 3px 0;")
        self.But_8.setObjectName("But_8")
        self.gridLayout_2.addWidget(self.But_8, 2, 1, 1, 1)
        self.But_0 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.But_0.sizePolicy().hasHeightForWidth())
        self.But_0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.But_0.setFont(font)
        self.But_0.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.But_0.setStyleSheet("background-color: rgb(235, 237, 238);\n"
"border: none;\n"
"background-color: rgb(204, 229, 255);\n"
"color: rgb(24, 62, 99);\n"
"border-radius:3px;\n"
"padding: 3px 0;")
        self.But_0.setObjectName("But_0")
        self.gridLayout_2.addWidget(self.But_0, 5, 1, 1, 1)
        self.But_2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.But_2.sizePolicy().hasHeightForWidth())
        self.But_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.But_2.setFont(font)
        self.But_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.But_2.setStyleSheet("background-color: rgb(235, 237, 238);\n"
"border: none;\n"
"background-color: rgb(204, 229, 255);\n"
"color: rgb(24, 62, 99);\n"
"border-radius:3px;\n"
"padding: 3px 0;")
        self.But_2.setObjectName("But_2")
        self.gridLayout_2.addWidget(self.But_2, 4, 1, 1, 1)
        self.But_3 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.But_3.sizePolicy().hasHeightForWidth())
        self.But_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.But_3.setFont(font)
        self.But_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.But_3.setStyleSheet("background-color: rgb(235, 237, 238);\n"
"border: none;\n"
"background-color: rgb(204, 229, 255);\n"
"color: rgb(24, 62, 99);\n"
"border-radius:3px;\n"
"padding: 3px 0;")
        self.But_3.setObjectName("But_3")
        self.gridLayout_2.addWidget(self.But_3, 4, 2, 1, 1)
        self.But_1 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.But_1.sizePolicy().hasHeightForWidth())
        self.But_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.But_1.setFont(font)
        self.But_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.But_1.setStyleSheet("background-color: rgb(235, 237, 238);\n"
"border: none;\n"
"background-color: rgb(204, 229, 255);\n"
"color: rgb(24, 62, 99);\n"
"border-radius:3px;\n"
"padding: 3px 0;")
        self.But_1.setObjectName("But_1")
        self.gridLayout_2.addWidget(self.But_1, 4, 0, 1, 1)
        self.But_Del = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.But_Del.sizePolicy().hasHeightForWidth())
        self.But_Del.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.But_Del.setFont(font)
        self.But_Del.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.But_Del.setStyleSheet("background-color: rgb(235, 237, 238);\n"
"border: none;\n"
"background-color:rgb(162, 208, 250);\n"
"color:  rgb(80, 138, 198);\n"
"border-radius:3px;\n"
"padding: 3px 0;")
        self.But_Del.setObjectName("But_Del")
        self.gridLayout_2.addWidget(self.But_Del, 5, 2, 1, 1)
        self.But_7 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.But_7.sizePolicy().hasHeightForWidth())
        self.But_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.But_7.setFont(font)
        self.But_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.But_7.setStyleSheet("background-color: rgb(235, 237, 238);\n"
"border: none;\n"
"background-color: rgb(204, 229, 255);\n"
"color: rgb(24, 62, 99);\n"
"border-radius:3px;\n"
"padding: 3px 0;")
        self.But_7.setObjectName("But_7")
        self.gridLayout_2.addWidget(self.But_7, 2, 0, 1, 1)
        self.But_9 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.But_9.sizePolicy().hasHeightForWidth())
        self.But_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.But_9.setFont(font)
        self.But_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.But_9.setStyleSheet("background-color: rgb(235, 237, 238);\n"
"border: none;\n"
"background-color: rgb(204, 229, 255);\n"
"color: rgb(24, 62, 99);\n"
"border-radius:3px;\n"
"padding: 3px 0;")
        self.But_9.setObjectName("But_9")
        self.gridLayout_2.addWidget(self.But_9, 2, 2, 1, 1)
        self.But_E = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.But_E.sizePolicy().hasHeightForWidth())
        self.But_E.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.But_E.setFont(font)
        self.But_E.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.But_E.setStyleSheet("background-color: rgb(235, 237, 238);\n"
"border: none;\n"
"background-color: rgb(204, 229, 255);\n"
"color: rgb(24, 62, 99);\n"
"border-radius:3px;\n"
"padding: 3px 0;")
        self.But_E.setObjectName("But_E")
        self.gridLayout_2.addWidget(self.But_E, 0, 1, 1, 1)
        self.But_F = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.But_F.sizePolicy().hasHeightForWidth())
        self.But_F.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.But_F.setFont(font)
        self.But_F.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.But_F.setStyleSheet("background-color: rgb(235, 237, 238);\n"
"border: none;\n"
"background-color: rgb(204, 229, 255);\n"
"color: rgb(24, 62, 99);\n"
"border-radius:3px;\n"
"padding: 3px 0;")
        self.But_F.setObjectName("But_F")
        self.gridLayout_2.addWidget(self.But_F, 0, 2, 1, 1)
        self.But_C = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.But_C.sizePolicy().hasHeightForWidth())
        self.But_C.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.But_C.setFont(font)
        self.But_C.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.But_C.setStyleSheet("background-color: rgb(235, 237, 238);\n"
"border: none;\n"
"background-color: rgb(204, 229, 255);\n"
"color: rgb(24, 62, 99);\n"
"border-radius:3px;\n"
"padding: 3px 0;")
        self.But_C.setObjectName("But_C")
        self.gridLayout_2.addWidget(self.But_C, 1, 2, 1, 1)
        self.But_D = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.But_D.sizePolicy().hasHeightForWidth())
        self.But_D.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.But_D.setFont(font)
        self.But_D.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.But_D.setStyleSheet("background-color: rgb(235, 237, 238);\n"
"border: none;\n"
"background-color: rgb(204, 229, 255);\n"
"color: rgb(24, 62, 99);\n"
"border-radius:3px;\n"
"padding: 3px 0;")
        self.But_D.setObjectName("But_D")
        self.gridLayout_2.addWidget(self.But_D, 0, 0, 1, 1)
        self.But_A = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.But_A.sizePolicy().hasHeightForWidth())
        self.But_A.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.But_A.setFont(font)
        self.But_A.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.But_A.setStyleSheet("background-color: rgb(235, 237, 238);\n"
"border: none;\n"
"background-color: rgb(204, 229, 255);\n"
"color: rgb(24, 62, 99);\n"
"border-radius:3px;\n"
"padding: 3px 0;")
        self.But_A.setObjectName("But_A")
        self.gridLayout_2.addWidget(self.But_A, 1, 0, 1, 1)
        self.Label_oct = QtWidgets.QLabel(self.widget)
        self.Label_oct.setGeometry(QtCore.QRect(250, 110, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.Label_oct.setFont(font)
        self.Label_oct.setStyleSheet("background-color: rgb(204, 229, 255);\n"
"border-radius:5px;\n"
"border-color: black;")
        self.Label_oct.setText("")
        self.Label_oct.setObjectName("Label_oct")
        self.Label_Dec = QtWidgets.QLabel(self.widget)
        self.Label_Dec.setGeometry(QtCore.QRect(250, 170, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.Label_Dec.setFont(font)
        self.Label_Dec.setStyleSheet("background-color: rgb(204, 229, 255);\n"
"border-radius:5px;\n"
"border-color: black;")
        self.Label_Dec.setText("")
        self.Label_Dec.setObjectName("Label_Dec")
        self.Label_Hex = QtWidgets.QLabel(self.widget)
        self.Label_Hex.setGeometry(QtCore.QRect(250, 230, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.Label_Hex.setFont(font)
        self.Label_Hex.setStyleSheet("background-color: rgb(204, 229, 255);\n"
"border-radius:5px;\n"
"border-color: black;")
        self.Label_Hex.setText("")
        self.Label_Hex.setObjectName("Label_Hex")
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setGeometry(QtCore.QRect(50, 60, 95, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2.setGeometry(QtCore.QRect(50, 120, 95, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_3.setGeometry(QtCore.QRect(50, 180, 110, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_4.setGeometry(QtCore.QRect(50, 240, 180, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.But_Con_2 = QtWidgets.QPushButton(self.widget)
        self.But_Con_2.setGeometry(QtCore.QRect(200, 380, 230, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.But_Con_2.setFont(font)
        self.But_Con_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.But_Con_2.setStyleSheet("border: none;\n"
"margin-right: 3px;\n"
"padding: 5px 0;\n"
"color: rgb(80, 138, 198);\n"
"background-color: rgb(162, 208, 250);\n"
"border-radius:3px;")
        self.But_Con_2.setObjectName("But_Con_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.But_0.clicked.connect(self.method0)
        self.But_1.clicked.connect(self.method1)
        self.But_2.clicked.connect(self.method2)
        self.But_3.clicked.connect(self.method3)
        self.But_4.clicked.connect(self.method4)
        self.But_5.clicked.connect(self.method5)
        self.But_6.clicked.connect(self.method6)
        self.But_7.clicked.connect(self.method7)
        self.But_8.clicked.connect(self.method8)
        self.But_9.clicked.connect(self.method9)
        self.But_A.clicked.connect(self.methodA)
        self.But_B.clicked.connect(self.methodB)
        self.But_C.clicked.connect(self.methodC)
        self.But_D.clicked.connect(self.methodD)
        self.But_E.clicked.connect(self.methodE)
        self.But_F.clicked.connect(self.methodF)
        self.But_AC.clicked.connect(self.method_AC)
        self.But_Del.clicked.connect(self.method_Del)
        self.But_Con.clicked.connect(self.convert)
        self.radioButton_3.clicked.connect(self.method_rad3)
        self.radioButton.clicked.connect(self.method_rad1)
        self.radioButton_2.clicked.connect(self.method_rad2)
        self.radioButton_4.clicked.connect(self.method_rad4)
        self.But_Con_2.clicked.connect(self.calculatrice)
        self.But_Con_2.clicked.connect(MainWindow.close)
    def method_rad3(self):
            self.Label_bin.setText("")
            self.Label_oct.setText("")
            self.Label_Hex.setText("")
            self.Label_Dec.setText("")

    def method_rad4(self):
            self.Label_bin.setText("")
            self.Label_oct.setText("")
            self.Label_Hex.setText("")
            self.Label_Dec.setText("")

    def method_rad2(self):
            self.Label_bin.setText("")
            self.Label_oct.setText("")
            self.Label_Hex.setText("")
            self.Label_Dec.setText("")

    def method_rad1(self):
            self.Label_bin.setText("")
            self.Label_oct.setText("")
            self.Label_Hex.setText("")
            self.Label_Dec.setText("")

    def method0(self):

            if self.radioButton_3.isChecked() == True:
                    text = self.Label_Dec.text()
                    self.Label_Dec.setText(text + "0")
            elif self.radioButton.isChecked() == True:
                    text = self.Label_bin.text()
                    self.Label_bin.setText(text + "0")
            elif self.radioButton_2.isChecked() == True:
                    text = self.Label_oct.text()
                    self.Label_oct.setText(text + "0")
            elif self.radioButton_4.isChecked() == True:
                    text = self.Label_Hex.text()
                    self.Label_Hex.setText(text + "0")

    def method1(self):
            if self.radioButton_3.isChecked() == True:
                    text = self.Label_Dec.text()
                    self.Label_Dec.setText(text + "1")
            elif self.radioButton.isChecked() == True:
                    text = self.Label_bin.text()
                    self.Label_bin.setText(text + "1")
            elif self.radioButton_2.isChecked() == True:
                    text = self.Label_oct.text()
                    self.Label_oct.setText(text + "1")
            elif self.radioButton_4.isChecked() == True:
                    text = self.Label_Hex.text()
                    self.Label_Hex.setText(text + "1")

    def method2(self):
            if self.radioButton_3.isChecked() == True:
                    text = self.Label_Dec.text()
                    self.Label_Dec.setText(text + "2")
            elif self.radioButton_2.isChecked() == True:
                    text = self.Label_oct.text()
                    self.Label_oct.setText(text + "2")
            elif self.radioButton_4.isChecked() == True:
                    text = self.Label_Hex.text()
                    self.Label_Hex.setText(text + "2")

    def method3(self):
            if self.radioButton_3.isChecked() == True:
                    text = self.Label_Dec.text()
                    self.Label_Dec.setText(text + "3")
            elif self.radioButton_2.isChecked() == True:
                    text = self.Label_oct.text()
                    self.Label_oct.setText(text + "3")
            elif self.radioButton_4.isChecked() == True:
                    text = self.Label_Hex.text()
                    self.Label_Hex.setText(text + "3")

    def method4(self):
            if self.radioButton_3.isChecked() == True:
                    text = self.Label_Dec.text()
                    self.Label_Dec.setText(text + "4")
            elif self.radioButton_2.isChecked() == True:
                    text = self.Label_oct.text()
                    self.Label_oct.setText(text + "4")
            elif self.radioButton_4.isChecked() == True:
                    text = self.Label_Hex.text()
                    self.Label_Hex.setText(text + "4")

    def method5(self):
            if self.radioButton_3.isChecked() == True:
                    text = self.Label_Dec.text()
                    self.Label_Dec.setText(text + "5")
            elif self.radioButton_2.isChecked() == True:
                    text = self.Label_oct.text()
                    self.Label_oct.setText(text + "5")
            elif self.radioButton_4.isChecked() == True:
                    text = self.Label_Hex.text()
                    self.Label_Hex.setText(text + "5")

    def method6(self):
            if self.radioButton_3.isChecked() == True:
                    text = self.Label_Dec.text()
                    self.Label_Dec.setText(text + "6")
            elif self.radioButton_2.isChecked() == True:
                    text = self.Label_oct.text()
                    self.Label_oct.setText(text + "6")
            elif self.radioButton_4.isChecked() == True:
                    text = self.Label_Hex.text()
                    self.Label_Hex.setText(text + "6")

    def method7(self):
            if self.radioButton_3.isChecked() == True:
                    text = self.Label_Dec.text()
                    self.Label_Dec.setText(text + "7")
            elif self.radioButton_2.isChecked() == True:
                    text = self.Label_oct.text()
                    self.Label_oct.setText(text + "7")
            elif self.radioButton_4.isChecked() == True:
                    text = self.Label_Hex.text()
                    self.Label_Hex.setText(text + "7")

    def method8(self):
            if self.radioButton_3.isChecked() == True:
                    text = self.Label_Dec.text()
                    self.Label_Dec.setText(text + "8")
            elif self.radioButton_4.isChecked() == True:
                    text = self.Label_Hex.text()
                    self.Label_Hex.setText(text + "8")

    def method9(self):
            if self.radioButton_3.isChecked() == True:
                    text = self.Label_Dec.text()
                    self.Label_Dec.setText(text + "9")
            elif self.radioButton_4.isChecked() == True:
                    text = self.Label_Hex.text()
                    self.Label_Hex.setText(text + "9")

    def methodA(self):
            if self.radioButton_4.isChecked() == True:
                    text = self.Label_Hex.text()
                    self.Label_Hex.setText(text + "A")

    def methodB(self):
            if self.radioButton_4.isChecked() == True:
                    text = self.Label_Hex.text()
                    self.Label_Hex.setText(text + "B")

    def methodC(self):
            if self.radioButton_4.isChecked() == True:
                    text = self.Label_Hex.text()
                    self.Label_Hex.setText(text + "C")

    def methodD(self):
            if self.radioButton_4.isChecked() == True:
                    text = self.Label_Hex.text()
                    self.Label_Hex.setText(text + "D")

    def methodE(self):
            if self.radioButton_4.isChecked() == True:
                    text = self.Label_Hex.text()
                    self.Label_Hex.setText(text + "E")

    def methodF(self):
            if self.radioButton_4.isChecked() == True:
                    text = self.Label_Hex.text()
                    self.Label_Hex.setText(text + "F")

    def method_AC(self):
            self.Label_bin.setText("")
            self.Label_oct.setText("")
            self.Label_Hex.setText("")
            self.Label_Dec.setText("")

    def method_Del(self):
            if self.radioButton_3.isChecked() == True:
                    text = self.Label_Dec.text()
                    self.Label_Dec.setText(text[:len(text) - 1])
                    self.Label_bin.setText("")
                    self.Label_oct.setText("")
                    self.Label_Hex.setText("")
            elif self.radioButton.isChecked() == True:
                    text = self.Label_bin.text()
                    self.Label_bin.setText(text[:len(text) - 1])
                    self.Label_oct.setText("")
                    self.Label_Hex.setText("")
                    self.Label_Dec.setText("")
            elif self.radioButton_2.isChecked() == True:
                    text = self.Label_oct.text()
                    self.Label_oct.setText(text[:len(text) - 1])
                    self.Label_bin.setText("")
                    self.Label_Hex.setText("")
                    self.Label_Dec.setText("")
            elif self.radioButton_4.isChecked() == True:
                    text = self.Label_Hex.text()
                    self.Label_Hex.setText(text[:len(text) - 1])
                    self.Label_bin.setText("")
                    self.Label_oct.setText("")
                    self.Label_Dec.setText("")

    def convert(self):
            # Check which radio button is selected
            if self.radioButton_3.isChecked():
                    text = int(self.Label_Dec.text())

                    # Convert the value to binary, octal, and hexadecimal
                    bin_value = bin(int(text))[2:]
                    oct_value = oct(int(text))[2:]
                    hex_value = hex(int(text))[2:]

                    # Set the converted values in the appropriate labels
                    self.Label_bin.setText(bin_value)
                    self.Label_oct.setText(oct_value)
                    self.Label_Hex.setText(hex_value)

            if self.radioButton.isChecked():
                    text = self.Label_bin.text()
                    # Convert the value to decimal, octal, and hexadecimal
                    dec_value = int(text, 2)
                    oct_value = oct(dec_value)[2:]
                    hex_value = hex(dec_value)[2:]

                    # Set the converted values in the appropriate labels
                    self.Label_Dec.setText(str(dec_value))
                    self.Label_oct.setText(oct_value)
                    self.Label_Hex.setText(hex_value)
            if self.radioButton_2.isChecked():
                    text = self.Label_oct.text()
                    # Convert the value to decimal, binary, and hexadecimal
                    dec_value = int(text, 8)
                    bin_value = bin(dec_value)[2:]
                    hex_value = hex(dec_value)[2:]

                    # Set the converted values in the appropriate labels
                    self.Label_Dec.setText(str(dec_value))
                    self.Label_bin.setText(bin_value)
                    self.Label_Hex.setText(hex_value)
            if self.radioButton_4.isChecked():
                    text = self.Label_Hex.text()
                    # Convert the value to decimal, binary, and octal
                    dec_value = int(text, 16)
                    bin_value = bin(dec_value)[2:]
                    oct_value = oct(dec_value)[2:]

                    # Set the converted values in the appropriate labels
                    self.Label_Dec.setText(str(dec_value))
                    self.Label_bin.setText(bin_value)
                    self.Label_oct.setText(oct_value)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Conversion entre les bases"))
        icon = QIcon("logo.png")
        MainWindow.setWindowIcon(icon)
        self.But_Con.setText(_translate("MainWindow", "Convertir"))
        self.But_AC.setText(_translate("MainWindow", "AC"))
        self.But_5.setText(_translate("MainWindow", "5"))
        self.But_6.setText(_translate("MainWindow", "6"))
        self.But_4.setText(_translate("MainWindow", "4"))
        self.But_B.setText(_translate("MainWindow", "B"))
        self.But_8.setText(_translate("MainWindow", "8"))
        self.But_0.setText(_translate("MainWindow", "0"))
        self.But_2.setText(_translate("MainWindow", "2"))
        self.But_3.setText(_translate("MainWindow", "3"))
        self.But_1.setText(_translate("MainWindow", "1"))
        self.But_Del.setText(_translate("MainWindow", "DEL"))
        self.But_7.setText(_translate("MainWindow", "7"))
        self.But_9.setText(_translate("MainWindow", "9"))
        self.But_E.setText(_translate("MainWindow", "E"))
        self.But_F.setText(_translate("MainWindow", "F"))
        self.But_C.setText(_translate("MainWindow", "C"))
        self.But_D.setText(_translate("MainWindow", "D"))
        self.But_A.setText(_translate("MainWindow", "A"))
        self.radioButton.setText(_translate("MainWindow", "Binaire"))
        self.radioButton_2.setText(_translate("MainWindow", "Octal"))
        self.radioButton_3.setText(_translate("MainWindow", "Décimal"))
        self.radioButton_4.setText(_translate("MainWindow", "Héxa-Décimal"))
        self.But_Con_2.setText(_translate("MainWindow", "Retour"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = conversionWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
