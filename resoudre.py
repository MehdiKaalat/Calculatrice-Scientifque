from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor, QIcon
from PyQt5.QtWidgets import QVBoxLayout, QLineEdit, QMainWindow, QPushButton
from numpy import *
from sympy import *


class ResoudreWindow(object):
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
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_2.setStyleSheet("background-color: rgb(204, 229, 255);\n"
                                   "padding: 10px;")
        self.label_2.setText("")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setProperty("clicked", "")
        self.label_2.setObjectName("label_2")
        self.label_2.setFixedHeight(200)
        self.label_2.setAlignment(Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.adjustSize()
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 5)
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.layout = QVBoxLayout()
        self.widget.setLayout(self.layout)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 16, 220, 20))
        self.label.setObjectName("label")
        self.spinBox = QtWidgets.QSpinBox(self.widget)
        self.spinBox.setGeometry(QtCore.QRect(290, 1, 62, 42))
        self.spinBox.setMaximum(5)
        self.spinBox.setObjectName("spinBox")
        self.pushButton_24 = QtWidgets.QPushButton(self.widget)
        self.pushButton_24.setGeometry(QtCore.QRect(370, 2, 100, 37))
        self.pushButton_24.setCursor((QCursor(QtCore.Qt.PointingHandCursor)))
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_24.setStyleSheet("""
                                                QPushButton {
                                                    border: none;
                                                    padding: 5px 0;
                                                    color: rgb(80, 138, 198);
                                                    background-color: rgb(162, 208, 250);
                                                    border-radius:3px;}
                                                QPushButton:hover {
                                                    background-color:  rgb(80, 138, 198);
                                                    color:  rgb(162, 208, 250);}
                                                    """)
        self.pushButton_20 = QtWidgets.QPushButton(self.widget)
        self.pushButton_20.setGeometry(QtCore.QRect(480, 2, 100, 37))
        self.pushButton_20.setObjectName("pushButton_24")
        self.pushButton_20.setCursor((QCursor(QtCore.Qt.PointingHandCursor)))
        self.pushButton_20.setStyleSheet("""
                                        QPushButton {
                                            border: none;
                                            padding: 5px 0;
                                            color: rgb(80, 138, 198);
                                            background-color: rgb(162, 208, 250);
                                            border-radius:3px;}
                                        QPushButton:hover {
                                            background-color:  rgb(80, 138, 198);
                                            color:  rgb(162, 208, 250);}
                                            """)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 5)
        self.verticalLayout.addLayout(self.gridLayout)
        self.layout.update()
        MainWindow.setCentralWidget(self.centralwidget)
        # Create the button and set its parent to the QTabWidget
        self.button = QtWidgets.QPushButton(self.widget)
        self.button.setObjectName("buttton")
        self.button.setCursor(Qt.PointingHandCursor)
        self.button.setGeometry(QtCore.QRect(470, 610, 81, 16))
        self.button.setStyleSheet("""
                                                        QPushButton {
                                                            border: none;
                                                            color: rgb(80, 138, 198);
                                                            background-color: rgb(162, 208, 250);
                                                            border-radius:3px;}
                                                        QPushButton:hover {
                                                            background-color:  rgb(80, 138, 198);
                                                            color:  rgb(162, 208, 250);}
                                                            """)
        # Set the button's fixed size
        self.button.setFixedHeight(50)
        self.button.setFixedWidth(100)
        self.button.clicked.connect(self.calculatrice)
        self.button.clicked.connect(MainWindow.close)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_24.clicked.connect(self.createLineEdits)
        self.pushButton_20.clicked.connect(self.method_Egal)

    def method_Egal(self):
            self.label_2.setText("")
            try:
                    equations = []
                    for lineedit in self.lineedits:
                            equation = lineedit.text()
                            equations.append(equation)
                    eqs = Tuple(*equations)
                    syms = eqs.free_symbols
                    solution = solve(eqs, syms)

                    if solution == []:
                            self.label_2.setText("L'équation est indeterminée ou impossible ")
                    else:
                            self.label_2.setText(str(solution))
            except:
                    self.label_2.setText("Error Syntaxe")
    def createLineEdits(self):
            self.layout.setContentsMargins(0,50,0,0)
            if self.pushButton_24.text() == "Valider":
                    # Create N QLineEdit widgets, where N is the value of the QSpinBox
                    self.lineedits = []
                    for i in range(self.spinBox.value()):
                            lineedit = QLineEdit()
                            lineedit.setFixedHeight(40)
                            lineedit.setStyleSheet("border: 1px solid black;\n"
                                                   "color: rgb(80, 138, 198);\n"
                                                   "padding-left: 10px;\n"
                                                   "background-color: rgb(162, 208, 250);\n"
                                                   "border-radius:3px;")
                            self.layout.addWidget(lineedit)
                            self.lineedits.append(lineedit)
                    # Change the text of the validate_button to "Delete All"
                    self.pushButton_24.setText("Supprimer")
            # If the validate_button text is "Delete All", delete all QLineEdit widgets
            else:
                    for lineedit in self.lineedits:
                            lineedit.setParent(None)
                    self.lineedits = []
                    self.label_2.setText("")
                    # Change the text of the validate_button to "Validate"
                    self.pushButton_24.setText("Valider")
    def method_expo(self):
            text = self.label.text()
            self.label.setText(text + "exp(")
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle("Résolution des équations")
        icon = QIcon("logo.png")
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)
        self.pushButton_20.setText(_translate("MainWindow", "Résoudre"))
        self.label.setText(_translate("MainWindow", "Ecrire le nombre d \'equations : "))
        self.pushButton_24.setText(_translate("MainWindow", "Valider"))
        self.button.setText(_translate("MainWindow", "Retour"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ResoudreWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
