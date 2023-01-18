from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLineEdit, QSizePolicy
from Matrice import MatriceWindow
from resoudre import ResoudreWindow
from Conversion import conversionWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from math import *
import numpy as np
import numpy.linalg as alg
import io
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from numpy import linspace
import sympy as sp

class Ui_MainWindow(object):
    def conversion(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = conversionWindow()
        self.ui.setupUi(self.window2)
        self.window2.show()
    def resoudre(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = ResoudreWindow()
        self.ui.setupUi(self.window2)
        self.window2.show()
    def matrice(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = MatriceWindow()
        self.ui.setupUi(self.window2)
        self.window2.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(610, 900)
        MainWindow.setMinimumSize(QtCore.QSize(610, 900))
        MainWindow.setMaximumSize(QtCore.QSize(610, 900))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(233, 243, 253);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_18.setStyleSheet("border: none;\n"
"color: rgb(80, 138, 198);\n"
"background-color: rgb(162, 208, 250);\n"
"border-radius:3px;")
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout.addWidget(self.pushButton_18, 13, 2, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_20.sizePolicy().hasHeightForWidth())
        self.pushButton_20.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_20.setStyleSheet("border: none;\n"
"color: rgb(80, 138, 198);\n"
"background-color: rgb(162, 208, 250);\n"
"border-radius:3px;")
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout.addWidget(self.pushButton_20, 13, 4, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet("background-color: rgb(235, 237, 238);\n"
"border: none;\n"
"background-color: rgb(204, 229, 255);\n"
"color: rgb(24, 62, 99);\n"
"border-radius: 3px;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 11, 2, 1, 1)
        self.pushButton_30 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_30.sizePolicy().hasHeightForWidth())
        self.pushButton_30.setSizePolicy(sizePolicy)
        self.pushButton_30.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_30.setStyleSheet("border: none;\n"
"padding: 5px 0;\n"
"margin-button: 0;\n"
"color: rgb(80, 138, 198);\n"
"background-color: rgb(162, 208, 250);\n"
"border-radius:3px;")
        self.pushButton_30.setObjectName("pushButton_30")
        self.gridLayout.addWidget(self.pushButton_30, 8, 4, 1, 1)
        self.pushButton_28 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_28.sizePolicy().hasHeightForWidth())
        self.pushButton_28.setSizePolicy(sizePolicy)
        self.pushButton_28.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_28.setStyleSheet("border: none;\n"
"padding: 5px 0;\n"
"color: rgb(80, 138, 198);\n"
"background-color: rgb(162, 208, 250);\n"
"border-radius:3px;")
        self.pushButton_28.setObjectName("pushButton_28")
        self.gridLayout.addWidget(self.pushButton_28, 9, 2, 1, 1)
        self.pushButton_31 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_31.sizePolicy().hasHeightForWidth())
        self.pushButton_31.setSizePolicy(sizePolicy)
        self.pushButton_31.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_31.setStyleSheet("border: none;\n"
"padding: 5px 0;\n"
"color: rgb(80, 138, 198);\n"
"background-color: rgb(162, 208, 250);\n"
"border-radius:3px;")
        self.pushButton_31.setObjectName("pushButton_31")
        self.gridLayout.addWidget(self.pushButton_31, 8, 0, 1, 1)
        self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_23.sizePolicy().hasHeightForWidth())
        self.pushButton_23.setSizePolicy(sizePolicy)
        self.pushButton_23.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_23.setStyleSheet("border: none;\n"
"padding: 5px 0;\n"
"color: rgb(80, 138, 198);\n"
"background-color: rgb(162, 208, 250);\n"
"border-radius:3px;")
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout.addWidget(self.pushButton_23, 7, 4, 1, 1)
        self.pushButton_40 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_40.setMinimumHeight(40)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_40.sizePolicy().hasHeightForWidth())
        self.pushButton_40.setSizePolicy(sizePolicy)
        self.pushButton_40.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_40.setStyleSheet("border: none;\n"
"padding: 5px 0;\n"
"background-color: rgb(80, 138, 198);\n"
"color: rgb(162, 208, 250);\n"
"border-radius:3px;")
        self.pushButton_40.setObjectName("pushButton_40")
        self.gridLayout.addWidget(self.pushButton_40,4, 4, 1, 1)
        self.pushButton_34 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_34.sizePolicy().hasHeightForWidth())
        self.pushButton_34.setSizePolicy(sizePolicy)
        self.pushButton_34.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_34.setStyleSheet("border: none;\n"
"padding: 5px 0;\n"
"color: rgb(80, 138, 198);\n"
"background-color: rgb(162, 208, 250);\n"
"border-radius:3px;")
        self.pushButton_34.setObjectName("pushButton_34")
        self.gridLayout.addWidget(self.pushButton_34, 8, 3, 1, 1)
        self.pushButton_38 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_38.sizePolicy().hasHeightForWidth())
        self.pushButton_38.setSizePolicy(sizePolicy)
        self.pushButton_38.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_38.setStyleSheet("border: none;\n"
"padding: 5px 0;\n"
"color: rgb(80, 138, 198);\n"
"background-color: rgb(162, 208, 250);\n"
"border-radius:3px;")
        self.pushButton_38.setObjectName("pushButton_38")
        self.gridLayout.addWidget(self.pushButton_38, 7, 2, 1, 1)
        self.pushButton_27 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_27.sizePolicy().hasHeightForWidth())
        self.pushButton_27.setSizePolicy(sizePolicy)
        self.pushButton_27.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_27.setStyleSheet("border: none;\n"
"padding: 5px 0;\n"
"color: rgb(80, 138, 198);\n"
"background-color: rgb(162, 208, 250);\n"
"border-radius:3px;")
        self.pushButton_27.setObjectName("pushButton_27")
        self.gridLayout.addWidget(self.pushButton_27, 9, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: rgb(235, 237, 238);\n"
"border: none;\n"
"background-color: rgb(204, 229, 255);\n"
"color: rgb(24, 62, 99);\n"
"border-radius: 3px;")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 10, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet("background-color: rgb(235, 237, 238);\n"
"border: none;\n"
"background-color: rgb(204, 229, 255);\n"
"color: rgb(24, 62, 99);\n"
"border-radius: 3px;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 11, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet("border: none;\n"
"color: rgb(80, 138, 198);\n"
"background-color: rgb(162, 208, 250);\n"
"border-radius:3px;")
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 11, 4, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet("background-color: rgb(235, 237, 238);\n"
"border: none;\n"
"background-color: rgb(204, 229, 255);\n"
"color: rgb(24, 62, 99);\n"
"border-radius: 3px;")
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 12, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("background-color: rgb(235, 237, 238);\n"
"border: none;\n"
"background-color: rgb(204, 229, 255);\n"
"color: rgb(24, 62, 99);\n"
"border-radius: 3px;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 11, 0, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_13.setStyleSheet("background-color: rgb(235, 237, 238);\n"
"border: none;\n"
"background-color: rgb(204, 229, 255);\n"
"color: rgb(24, 62, 99);\n"
"border-radius: 3px;")
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 12, 2, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_14.setStyleSheet("border: none;\n"
"color: rgb(80, 138, 198);\n"
"background-color: rgb(162, 208, 250);\n"
"border-radius:3px;")
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 12, 3, 1, 1)
        self.pushButton_46 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_46.setMinimumHeight(40)
        self.pushButton_46.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_46.setTabletTracking(False)
        self.pushButton_46.setStyleSheet("image: url(backspace.png);\n"
"background-color: rgb(218, 220, 224);\n"
"border:none;\n"
"padding: 5px 0;\n"
"color: rgb(80, 138, 198);\n"
"background-color: rgb(162, 208, 250);\n"
"border-radius:3px;")
        self.pushButton_46.setText("")
        self.pushButton_46.setObjectName("pushButton_46")
        self.gridLayout.addWidget(self.pushButton_46, 2, 4, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_19.sizePolicy().hasHeightForWidth())
        self.pushButton_19.setSizePolicy(sizePolicy)
        self.pushButton_19.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_19.setStyleSheet("border: none;\n"
"color: rgb(80, 138, 198);\n"
"background-color: rgb(162, 208, 250);\n"
"border-radius:3px;")
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout.addWidget(self.pushButton_19, 13, 3, 1, 1)
        self.pushButton_48 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_48.setMinimumHeight(40)
        self.pushButton_48.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_48.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_48.setStyleSheet("image: url(flatten_the_curve_icon_142602.png);\n"
"border: none;\n"
"color:  rgb(162, 208, 250);\n"
"background-color: rgb(80, 138, 198);\n"
"font-size:23px;\n"
"border-radius:3px;")
        self.pushButton_48.setText("")
        self.pushButton_48.setIconSize(QtCore.QSize(12, 12))
        self.pushButton_48.setObjectName("pushButton_48")
        self.gridLayout.addWidget(self.pushButton_48, 4, 3, 1, 1)
        self.pushButton_26 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_26.sizePolicy().hasHeightForWidth())
        self.pushButton_26.setSizePolicy(sizePolicy)
        self.pushButton_26.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_26.setStyleSheet("border: none;\n"
"padding: 5px 0;\n"
"color: rgb(80, 138, 198);\n"
"background-color: rgb(162, 208, 250);\n"
"border-radius:3px;")
        self.pushButton_26.setObjectName("pushButton_26")
        self.gridLayout.addWidget(self.pushButton_26, 9, 0, 1, 1)
        self.pushButton_24 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_24.setMinimumHeight(40)
        self.pushButton_24.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_24.setStyleSheet("border: none;\n"
"padding: 5px 0;\n"
"background-color: rgb(80, 138, 198);\n"
"color: rgb(162, 208, 250);\n"
"border-radius:3px;")
        self.pushButton_24.setObjectName("pushButton_24")
        self.gridLayout.addWidget(self.pushButton_24, 4, 1, 1, 1)
        self.pushButton_39 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_39.setMinimumHeight(40)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_39.sizePolicy().hasHeightForWidth())
        self.pushButton_39.setSizePolicy(sizePolicy)
        self.pushButton_39.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_39.setStyleSheet("border: none;\n"
"padding: 5px 0;\n"
"background-color: rgb(80, 138, 198);\n"
"color: rgb(162, 208, 250);\n"
"border-radius:3px;")
        self.pushButton_39.setObjectName("pushButton_39")
        self.gridLayout.addWidget(self.pushButton_39, 4, 2, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("border: none;\n"
"color: rgb(80, 138, 198);\n"
"background-color: rgb(162, 208, 250);\n"
"border-radius:3px;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 11, 3, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_15.setStyleSheet("border: none;\n"
"color: rgb(80, 138, 198);\n"
"background-color: rgb(162, 208, 250);\n"
"border-radius:3px;")
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_15, 12, 4, 1, 1)
        self.pushButton_29 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_29.sizePolicy().hasHeightForWidth())
        self.pushButton_29.setSizePolicy(sizePolicy)
        self.pushButton_29.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_29.setStyleSheet("border: none;\n"
"padding: 5px 0;\n"
"color: rgb(80, 138, 198);\n"
"background-color: rgb(162, 208, 250);\n"
"border-radius:3px;")
        self.pushButton_29.setObjectName("pushButton_29")
        self.gridLayout.addWidget(self.pushButton_29, 9, 3, 1, 1)
        self.pushButton_36 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_36.sizePolicy().hasHeightForWidth())
        self.pushButton_36.setSizePolicy(sizePolicy)
        self.pushButton_36.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_36.setStyleSheet("border: none;\n"
"padding: 5px 0;\n"
"color: rgb(80, 138, 198);\n"
"background-color: rgb(162, 208, 250);\n"
"border-radius:3px;")
        self.pushButton_36.setObjectName("pushButton_36")
        self.gridLayout.addWidget(self.pushButton_36, 7, 0, 1, 1)
        self.pushButton_37 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_37.sizePolicy().hasHeightForWidth())
        self.pushButton_37.setSizePolicy(sizePolicy)
        self.pushButton_37.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_37.setStyleSheet("border: none;\n"
"padding: 5px 0;\n"
"color: rgb(80, 138, 198);\n"
"background-color: rgb(162, 208, 250);\n"
"border-radius:3px;")
        self.pushButton_37.setObjectName("pushButton_37")
        self.gridLayout.addWidget(self.pushButton_37, 7, 1, 1, 1)
        self.pushButton_32 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_32.sizePolicy().hasHeightForWidth())
        self.pushButton_32.setSizePolicy(sizePolicy)
        self.pushButton_32.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_32.setStyleSheet("border: none;\n"
"padding: 5px 0;\n"
"color: rgb(80, 138, 198);\n"
"background-color: rgb(162, 208, 250);\n"
"border-radius:3px;")
        self.pushButton_32.setObjectName("pushButton_32")
        self.gridLayout.addWidget(self.pushButton_32, 8, 1, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_17.setStyleSheet("border: none;\n"
"color: rgb(80, 138, 198);\n"
"background-color: rgb(162, 208, 250);\n"
"border-radius:3px;")
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout.addWidget(self.pushButton_17, 13, 1, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet("background-color: rgb(235, 237, 238);\n"
"border: none;\n"
"background-color: rgb(204, 229, 255);\n"
"color: rgb(24, 62, 99);\n"
"border-radius: 3px;")
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 12, 0, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_16.setStyleSheet("background-color: rgb(235, 237, 238);\n"
"border: none;\n"
"background-color: rgb(204, 229, 255);\n"
"color: rgb(24, 62, 99);\n"
"border-radius:3px;\n"
"padding: 3px 0;")
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_16, 13, 0, 1, 1)
        self.line_edit = QLineEdit(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        self.line_edit.setSizePolicy(sizePolicy)
        self.line_edit.setReadOnly(True)
        self.line_edit.setStyleSheet("background-color: rgb(204, 229, 255);\n"
                                     "font-size: 25px;"
                                     "border:0;"
                                     "padding: 5px;")
        self.line_edit.setObjectName("line_edit")
        self.line_edit.setFixedHeight(100)
        self.gridLayout.addWidget(self.line_edit, 0, 0, 1, 5)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        self.label_2.setWordWrap(True)
        self.label_2.adjustSize()
        self.label_2.setFixedHeight(100)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(13)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())

        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_2.setStyleSheet("background-color: rgb(204, 229, 255);\n"
                                   "font-size: 25px;"
                                   "padding: 5px 5px 10px 5px;"
                                   )
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setProperty("clicked", "")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 5)
        self.pushButton_33 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_33.sizePolicy().hasHeightForWidth())
        self.pushButton_33.setSizePolicy(sizePolicy)
        self.pushButton_33.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_33.setStyleSheet("border: none;\n"
"\n"
"padding: 5px 0;\n"
"color: rgb(80, 138, 198);\n"
"background-color: rgb(162, 208, 250);\n"
"border-radius:3px;")
        self.pushButton_33.setObjectName("pushButton_33")
        self.gridLayout.addWidget(self.pushButton_33, 8, 2, 1, 1)
        self.pushButton_25 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_25.sizePolicy().hasHeightForWidth())
        self.pushButton_25.setSizePolicy(sizePolicy)
        self.pushButton_25.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_25.setStyleSheet("border: none;\n"
"padding: 5px 0;\n"
"margin-button: 0;\n"
"color: rgb(80, 138, 198);\n"
"background-color: rgb(162, 208, 250);\n"
"border-radius:3px;")
        self.pushButton_25.setObjectName("pushButton_25")
        self.gridLayout.addWidget(self.pushButton_25, 9, 4, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background-color: rgb(235, 237, 238);\n"
"border: none;\n"
"background-color: rgb(204, 229, 255);\n"
"color: rgb(24, 62, 99);\n"
"border-radius: 3px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 10, 1, 1, 1)
        self.pushButton_47 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_47.setMinimumHeight(40)
        self.pushButton_47.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_47.setStyleSheet("border: none;\n"
"margin-right: 3px;\n"
"padding: 5px 0;\n"
"color: rgb(80, 138, 198);\n"
"background-color: rgb(162, 208, 250);\n"
"border-radius:3px;")
        self.pushButton_47.setObjectName("pushButton_47")
        self.gridLayout.addWidget(self.pushButton_47, 2, 3, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("border: none;\n"
"color: rgb(80, 138, 198);\n"
"background-color: rgb(162, 208, 250);\n"
"border-radius:3px;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 10, 4, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("border: none;\n"
"color: rgb(80, 138, 198);\n"
"background-color: rgb(162, 208, 250);\n"
"border-radius:3px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 10, 3, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: rgb(235, 237, 238);\n"
"border: none;\n"
"background-color: rgb(204, 229, 255);\n"
"color: rgb(24, 62, 99);\n"
"border-radius: 3px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 10, 2, 1, 1)
        self.pushButton_41 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_41.setMinimumHeight(40)
        self.pushButton_41.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_41.setStyleSheet("border: none;\n"
"\n"
"padding: 5px 0;\n"
"color: rgb(80, 138, 198);\n"
"background-color: rgb(162, 208, 250);\n"
"border-radius:3px;")
        self.pushButton_41.setObjectName("pushButton_41")
        self.gridLayout.addWidget(self.pushButton_41, 4, 0, 1, 1)
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_21.sizePolicy().hasHeightForWidth())
        self.pushButton_21.setSizePolicy(sizePolicy)
        self.pushButton_21.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_21.setStyleSheet("border: none;\n"
"\n"
"padding: 5px 0;\n"
"color: rgb(80, 138, 198);\n"
"background-color: rgb(162, 208, 250);\n"
"border-radius:3px;")
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout.addWidget(self.pushButton_21, 7, 3, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_22.sizePolicy().hasHeightForWidth())
        self.pushButton_22.setSizePolicy(sizePolicy)
        self.pushButton_22.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_22.setStyleSheet("border: none;\n"
"padding: 5px 0;\n"
"color: rgb(80, 138, 198);\n"
"background-color: rgb(162, 208, 250);\n"
"border-radius:3px;")
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout.addWidget(self.pushButton_22, 6, 4, 1, 1)
        self.pushButton_35 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_35.sizePolicy().hasHeightForWidth())
        self.pushButton_35.setSizePolicy(sizePolicy)
        self.pushButton_35.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_35.setStyleSheet("border: none;\n"
"padding: 5px 0;\n"
"color: rgb(80, 138, 198);\n"
"background-color: rgb(162, 208, 250);\n"
"border-radius:3px;")
        self.pushButton_35.setObjectName("pushButton_35")
        self.gridLayout.addWidget(self.pushButton_35, 6, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        ###
        self.pushButton_NOT = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        self.pushButton_NOT.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        sizePolicy.setHeightForWidth(self.pushButton_NOT.sizePolicy().hasHeightForWidth())
        self.pushButton_NOT.setSizePolicy(sizePolicy)
        self.pushButton_NOT.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_NOT.setStyleSheet("border: none;\n"
                                         "padding: 5px 0;\n"
                                         "color: rgb(80, 138, 198);\n"
                                         "background-color: rgb(162, 208, 250);\n"
                                         "border-radius:3px;")
        self.pushButton_NOT.setObjectName("pushButton_NOT")
        self.gridLayout.addWidget(self.pushButton_NOT, 6, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton_OR = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_OR.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_OR.sizePolicy().hasHeightForWidth())
        self.pushButton_OR.setSizePolicy(sizePolicy)
        self.pushButton_OR.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_OR.setStyleSheet("border: none;\n"
                                         "padding: 5px 0;\n"
                                         "color: rgb(80, 138, 198);\n"
                                         "background-color: rgb(162, 208, 250);\n"
                                         "border-radius:3px;")
        self.pushButton_OR.setObjectName("pushButton_OR")
        self.gridLayout.addWidget(self.pushButton_OR, 6, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton_AND = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_AND.sizePolicy().hasHeightForWidth())
        self.pushButton_AND.setSizePolicy(sizePolicy)
        self.pushButton_AND.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_AND.setStyleSheet("border: none;\n"
                                         "padding: 5px 0;\n"
                                         "color: rgb(80, 138, 198);\n"
                                         "background-color: rgb(162, 208, 250);\n"
                                         "border-radius:3px;")
        self.pushButton_AND.setObjectName("pushButton_AND")
        self.gridLayout.addWidget(self.pushButton_AND, 6, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton_SUP = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_SUP.sizePolicy().hasHeightForWidth())
        self.pushButton_SUP.setSizePolicy(sizePolicy)
        self.pushButton_SUP.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_SUP.setStyleSheet("border: none;\n"
                                         "padding: 5px 0;\n"
                                         "color: rgb(80, 138, 198);\n"
                                         "background-color: rgb(162, 208, 250);\n"
                                         "border-radius:3px;")
        self.pushButton_SUP.setObjectName("pushButton_SUP")
        self.gridLayout.addWidget(self.pushButton_SUP, 5, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton_SUPEG = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_SUPEG.sizePolicy().hasHeightForWidth())
        self.pushButton_SUPEG.setSizePolicy(sizePolicy)
        self.pushButton_SUPEG.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_SUPEG.setStyleSheet("border: none;\n"
                                         "padding: 5px 0;\n"
                                         "color: rgb(80, 138, 198);\n"
                                         "background-color: rgb(162, 208, 250);\n"
                                         "border-radius:3px;")
        self.pushButton_SUPEG.setObjectName("pushButton_SUPEG")
        self.gridLayout.addWidget(self.pushButton_SUPEG, 5, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton_EG = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_EG.sizePolicy().hasHeightForWidth())
        self.pushButton_EG.setSizePolicy(sizePolicy)
        self.pushButton_EG.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_EG.setStyleSheet("border: none;\n"
                                         "padding: 5px 0;\n"
                                         "color: rgb(80, 138, 198);\n"
                                         "background-color: rgb(162, 208, 250);\n"
                                         "border-radius:3px;")
        self.pushButton_EG.setObjectName("pushButton_EG")
        self.gridLayout.addWidget(self.pushButton_EG, 5, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton_INFEG = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_INFEG.sizePolicy().hasHeightForWidth())
        self.pushButton_INFEG.setSizePolicy(sizePolicy)
        self.pushButton_INFEG.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_INFEG.setStyleSheet("border: none;\n"
                                         "padding: 5px 0;\n"
                                         "color: rgb(80, 138, 198);\n"
                                         "background-color: rgb(162, 208, 250);\n"
                                         "border-radius:3px;")
        self.pushButton_INFEG.setObjectName("pushButton_INFEG")
        self.gridLayout.addWidget(self.pushButton_INFEG, 5, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton_INF = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_INF.sizePolicy().hasHeightForWidth())
        self.pushButton_INF.setSizePolicy(sizePolicy)
        self.pushButton_INF.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_INF.setStyleSheet("border: none;\n"
                                         "padding: 5px 0;\n"
                                         "color: rgb(80, 138, 198);\n"
                                         "background-color: rgb(162, 208, 250);\n"
                                         "border-radius:3px;")
        self.pushButton_INF.setObjectName("pushButton_INF")
        self.gridLayout.addWidget(self.pushButton_INF, 5, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        #############################################
        self.pushButton_35.setMinimumHeight(40)
        self.pushButton_21.setMinimumHeight(40)
        self.pushButton_22.setMinimumHeight(40)
        self.pushButton_23.setMinimumHeight(40)
        self.pushButton_25.setMinimumHeight(40)
        self.pushButton_26.setMinimumHeight(40)
        self.pushButton_27.setMinimumHeight(40)
        self.pushButton_28.setMinimumHeight(40)
        self.pushButton_29.setMinimumHeight(40)
        self.pushButton_30.setMinimumHeight(40)
        self.pushButton_36.setMinimumHeight(40)
        self.pushButton_37.setMinimumHeight(40)
        self.pushButton_38.setMinimumHeight(40)
        self.pushButton_31.setMinimumHeight(40)
        self.pushButton_32.setMinimumHeight(40)
        self.pushButton_33.setMinimumHeight(40)
        self.pushButton_34.setMinimumHeight(40)
        self.pushButton_NOT.setMinimumHeight(40)
        self.pushButton_OR.setMinimumHeight(40)
        self.pushButton_AND.setMinimumHeight(40)

        self.pushButton_SUP.setMinimumHeight(40)
        self.pushButton_SUPEG.setMinimumHeight(40)
        self.pushButton_INF.setMinimumHeight(40)
        self.pushButton_INFEG.setMinimumHeight(40)
        self.pushButton_EG.setMinimumHeight(40)



        self.pushButton_16.setMinimumHeight(50)
        self.pushButton_11.setMinimumHeight(50)
        self.pushButton.setMinimumHeight(50)
        self.pushButton_5.setMinimumHeight(50)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        ############################################
        self.pushButton_16.clicked.connect(self.method0)
        self.pushButton_11.clicked.connect(self.method1)
        self.pushButton_12.clicked.connect(self.method2)
        self.pushButton_13.clicked.connect(self.method3)
        self.pushButton_6.clicked.connect(self.method4)
        self.pushButton_7.clicked.connect(self.method5)
        self.pushButton_8.clicked.connect(self.method6)
        self.pushButton.clicked.connect(self.method7)
        self.pushButton_2.clicked.connect(self.method8)
        self.pushButton_3.clicked.connect(self.method9)
        self.pushButton_14.clicked.connect(self.method_somme)
        self.pushButton_15.clicked.connect(self.method_soustraction)
        self.pushButton_9.clicked.connect(self.method_mul)
        self.pushButton_10.clicked.connect(self.method_division)
        self.pushButton_20.clicked.connect(self.method_Egal)
        self.pushButton_47.clicked.connect(self.method_AC)
        self.pushButton_46.clicked.connect(self.method_del)
        self.pushButton_17.clicked.connect(self.method_point)
        self.pushButton_4.clicked.connect(self.method_par1)
        self.pushButton_5.clicked.connect(self.method_par2)
        self.pushButton_25.clicked.connect(self.method_Factoriel)
        self.pushButton_35.clicked.connect(self.method_ln)
        self.pushButton_34.clicked.connect(self.method_Absolue)
        self.pushButton_33.clicked.connect(self.method_Tan)
        self.pushButton_32.clicked.connect(self.method_Cos)
        self.pushButton_31.clicked.connect(self.method_Sin)
        self.pushButton_38.clicked.connect(self.method_Tanh)
        self.pushButton_37.clicked.connect(self.method_Cosh)
        self.pushButton_36.clicked.connect(self.method_Sinh)
        self.pushButton_26.clicked.connect(self.method_pow)
        self.pushButton_27.clicked.connect(self.method_pow2)
        self.pushButton_28.clicked.connect(self.method_pow3)
        self.pushButton_29.clicked.connect(self.method_sqrt)
        self.pushButton_30.clicked.connect(self.method_exp)
        self.pushButton_21.clicked.connect(self.method_tan_1)
        self.pushButton_22.clicked.connect(self.method_cos_1)
        self.pushButton_23.clicked.connect(self.method_sin_1)
        self.pushButton_18.clicked.connect(self.method_pourcentage)
        self.pushButton_19.clicked.connect(self.method_ans)
        self.pushButton_40.clicked.connect(self.resoudre)
        self.pushButton_40.clicked.connect(MainWindow.close)
        self.pushButton_39.clicked.connect(self.matrice)
        self.pushButton_39.clicked.connect(MainWindow.close)
        self.pushButton_41.clicked.connect(self.method_x)
        self.pushButton_48.clicked.connect(self.generate_graph)
        self.pushButton_NOT.clicked.connect(self.method_Not)
        self.pushButton_AND.clicked.connect(self.method_And)
        self.pushButton_OR.clicked.connect(self.method_Or)
        self.pushButton_EG.clicked.connect(self.method_egal2)
        self.pushButton_SUPEG.clicked.connect(self.method_supeg)
        self.pushButton_SUP.clicked.connect(self.method_sup)
        self.pushButton_INFEG.clicked.connect(self.method_infeg)
        self.pushButton_INF.clicked.connect(self.method_inf)
        self.pushButton_24.clicked.connect(self.conversion)
        self.pushButton_24.clicked.connect(MainWindow.close)

    def method_inf(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "<")

    def method_infeg(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "<=")

    def method_sup(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + ">")

    def method_supeg(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + ">=")

    def method_egal2(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "==")

    def method_Or(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + " or ")

    def method_And(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + " and ")

    def method_Not(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + " not ")

    def generate_graph(self):

            # Get the function from the function label
            fct = self.line_edit.text()
            n1 = fct.count("(")
            n2 = fct.count(")")
            if n1 > n2:
                    for i in range((n1 - n2)):
                            fct = fct + ")"
            # Evaluate the function for a range of x values
            x = linspace(-10, 20, 1000)

            if "^" in fct:
                    fct = fct.replace("^", "**")
            if "ln" in fct:
                    fct = fct.replace("ln", "np.log")
            if "√" in fct:
                    fct = fct.replace("√", "np.sqrt")
            if "²" in fct:
                    fct = fct.replace("²", "**2")
            if "π" in fct:
                    fct = fct.replace("π", "pi")
            if "sin" in fct:
                    fct = fct.replace("sin", "np.sin")
            if "cos" in fct:
                    fct = fct.replace("cos", "np.cos")
            if "tan" in fct:
                    fct = fct.replace("tan", "np.tan")
            if "sinh" in fct:
                    x = linspace(-1, 1, 10)
                    fct = fct.replace("sinh", "sinh")
            if "cosh" in fct:
                    fct = fct.replace("cosh", "cosh")
            if "tanh" in fct:
                    x = linspace(-1, 1, 10)
                    fct = fct.replace("tanh", "tanh")
            if "asin" in fct:
                    x = linspace(-1, 1, 10)
                    fct = fct.replace("asin", "asin")
            if "acos" in fct:
                    x = linspace(-1, 1, 10)
                    fct = fct.replace("acos", "acos")
            if "atan" in fct:
                    x = linspace(-1, 1, 10)
                    fct = fct.replace("atan", "atan")
            if "exp" in fct:
                    fct = fct.replace("exp", "np.exp")

            try:
                    fct = eval(fct)
                    plt.plot(x, fct)
                    plt.ylabel("l'axe des ordonnées")
                    plt.xlabel("l'axe des abcisses")
                    plt.grid()
                    plt.show()

            except:
                    self.label_2.setText("Error Syntaxe")


    def method_x(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "x")
    def method0(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "0")

    def method1(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "1")

    def method2(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "2")

    def method3(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "3")

    def method4(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "4")

    def method5(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "5")

    def method6(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "6")

    def method7(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "7")

    def method8(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "8")

    def method9(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "9")

    def method_somme(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "+")

    def method_soustraction(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "-")

    def method_mul(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "*")

    def method_division(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "/")

    def method_par1(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "(")

    def method_par2(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + ")")

    def method_AC(self):
            self.line_edit.setText("")
            self.label_2.setText("")

    def method_del(self):
            text = self.line_edit.text()
            if text[-5:] == "asin(" or text[-5:] == "acos(" or text[-5:] == "atan("  or text[-5:] == " and " or text[-5:] == " not ":
                    self.line_edit.setText(text[:len(text) - 5])
            elif text[-4:] == "sin(" or text[-4:] == "cos(" or text[-4:] == "tan(" or text[-4:] == "exp(" or text[-4:] == "abs(" or text[-4:] == " or ":
                    self.line_edit.setText(text[:len(text)-4])
            elif text[-5:] == "sinh(" or text[-5:] == "cosh(" or text[-5:] == "tanh(":
                    self.line_edit.setText(text[:len(text)-5])
            elif text[-3:] == "ln(" :
                    self.line_edit.setText(text[:len(text)-3])
            elif text[-2:] == "^(" or text[-2:] == "^2" or text[-2:] == "^3" or text[-2:] == "√(" or text[-2:] == "!(" or text[-2:] == "or" or text[-2:] == "==" or text[-2:] == ">=" or text[-2:] == "<=":
                    self.line_edit.setText(text[:len(text)-2])
            else:
                    self.line_edit.setText(text[:len(text) - 1])
            self.label_2.setText("")
    def method_point(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + ".")

    def method_Egal(self):
            text = self.line_edit.text()
            if "!" in text:
                    text = text.replace("!","factorial")
            if "^" in text:
                    text = text.replace("^", "**")
            if "²" in text:
                    text = text.replace("²", "**2")
            if "π" in text:
                    text = text.replace("π", "pi")
            if "ln" in text:
                    text = text.replace("ln", "log")
            if "√" in text:
                    text = text.replace("√", "sqrt")

            n1 = text.count("(")
            n2 = text.count(")")
            if n1>n2:
                    for i in range((n1-n2)):
                        text = text +")"
            try:
                    ans = eval(text)
                    self.label_2.setText(str(ans))
            except:
                    self.label_2.setText("Error Syntaxe")

    def method_Factoriel(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "!(" )

    def method_ln(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "ln(")

    def method_exp(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "exp(")

    def method_Sin(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "sin(")

    def method_Cos(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "cos(")

    def method_Tan(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "tan(")

    def method_cos_1(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "acos(")

    def method_sin_1(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "asin(")

    def method_tan_1(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "atan(")

    def method_Sinh(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "sinh(")

    def method_Cosh(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "cosh(")

    def method_Tanh(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "tanh(")
    def method_pourcentage(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "%")
    def method_Absolue(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "abs(")

    def method_pow(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "^(")

    def method_pow2(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "²")

    def method_pow3(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "π")

    def method_sqrt(self):
            text = self.line_edit.text()
            self.line_edit.setText(text + "√(")
    def method_ans(self):
            text = self.line_edit.text()
            text2 = self.label_2.text()
            self.line_edit.setText(text + text2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle("Calculatrice scientifique")
        icon = QIcon("logo.png")
        MainWindow.setWindowIcon(icon)
        self.pushButton_18.setText(_translate("MainWindow", "%"))
        self.pushButton_20.setText(_translate("MainWindow", "="))
        self.pushButton_8.setText(_translate("MainWindow", "6"))
        self.pushButton_30.setText(_translate("MainWindow", "exp"))
        self.pushButton_28.setText(_translate("MainWindow", "π"))
        self.pushButton_31.setText(_translate("MainWindow", "sin"))
        self.pushButton_23.setText(_translate("MainWindow", "asin"))
        self.pushButton_40.setText(_translate("MainWindow", "Résolution Eqn"))
        self.pushButton_34.setText(_translate("MainWindow", "abs("))
        self.pushButton_38.setText(_translate("MainWindow", "tanh"))
        self.pushButton_27.setText(_translate("MainWindow", "x²"))
        self.pushButton.setText(_translate("MainWindow", "7"))
        self.pushButton_7.setText(_translate("MainWindow", "5"))
        self.pushButton_10.setText(_translate("MainWindow", "÷"))
        self.pushButton_12.setText(_translate("MainWindow", "2"))
        self.pushButton_6.setText(_translate("MainWindow", "4"))
        self.pushButton_13.setText(_translate("MainWindow", "3"))
        self.pushButton_14.setText(_translate("MainWindow", "+"))
        self.pushButton_19.setText(_translate("MainWindow", "ANS"))
        self.pushButton_26.setText(_translate("MainWindow", "^("))
        self.pushButton_24.setText(_translate("MainWindow", "Conversion"))
        self.pushButton_39.setText(_translate("MainWindow", "Matrice"))
        self.pushButton_9.setText(_translate("MainWindow", "×"))
        self.pushButton_15.setText(_translate("MainWindow", "-"))
        self.pushButton_29.setText(_translate("MainWindow", "√x"))
        self.pushButton_36.setText(_translate("MainWindow", "sinh"))
        self.pushButton_37.setText(_translate("MainWindow", "cosh"))
        self.pushButton_32.setText(_translate("MainWindow", "cos"))
        self.pushButton_17.setText(_translate("MainWindow", "."))
        self.pushButton_11.setText(_translate("MainWindow", "1"))
        self.pushButton_16.setText(_translate("MainWindow", "0"))
        self.line_edit.setText(_translate("MainWindow", ""))
        self.label_2.setText(_translate("MainWindow", ""))
        self.pushButton_33.setText(_translate("MainWindow", "tan"))
        self.pushButton_25.setText(_translate("MainWindow", "Factorielle"))
        self.pushButton_2.setText(_translate("MainWindow", "8"))
        self.pushButton_47.setText(_translate("MainWindow", "AC"))
        self.pushButton_5.setText(_translate("MainWindow", ")"))
        self.pushButton_4.setText(_translate("MainWindow", "("))
        self.pushButton_3.setText(_translate("MainWindow", "9"))
        self.pushButton_41.setText(_translate("MainWindow", "X"))
        self.pushButton_21.setText(_translate("MainWindow", "atan"))
        self.pushButton_22.setText(_translate("MainWindow", "acos"))
        self.pushButton_35.setText(_translate("MainWindow", "ln"))
        self.pushButton_NOT.setText(_translate("MainWindow", "NOT"))
        self.pushButton_OR.setText(_translate("MainWindow", "OR"))
        self.pushButton_AND.setText(_translate("MainWindow", "AND"))
        self.pushButton_SUP.setText(_translate("MainWindow", ">"))
        self.pushButton_SUPEG.setText(_translate("MainWindow", ">="))
        self.pushButton_EG.setText(_translate("MainWindow", "=="))
        self.pushButton_INFEG.setText(_translate("MainWindow", "<="))
        self.pushButton_INF.setText(_translate("MainWindow", "<"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
