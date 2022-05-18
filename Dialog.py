from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def __init__(self, errorNumber = 0):
        self.di_text = None
        self.errorNumber = errorNumber

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(385, 155)
        Dialog.setAutoFillBackground(False)
        self.di_text = QtWidgets.QLabel(Dialog)
        self.di_text.setGeometry(QtCore.QRect(30, 20, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.di_text.setFont(font)
        self.di_text.setTextFormat(QtCore.Qt.PlainText)
        self.di_text.setObjectName("eq_label")
        self.DiBtn = QtWidgets.QPushButton(Dialog)
        self.DiBtn.setGeometry(QtCore.QRect(110, 90, 161, 33))
        self.DiBtn.setStyleSheet("background-color: #dc425e;\n"
"color: black;\n"
"border-radius: 15px;\n"
"padding: 45px;\\n\n"
"font: 9pt \\\"Montserrat\\\";")
        self.DiBtn.setObjectName("DiBtn")
        self.DiBtn.clicked.connect(Dialog.close)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Error Message"))
        if self.errorNumber == 0:
            self.di_text.setText(_translate("Dialog", "  Your Entered a Wrong Equation, Try Again..."))
        elif self.errorNumber == 1:
            self.di_text.setText(_translate("Dialog", "           Empty Fields, Please Fill it"))
        elif self.errorNumber == 2:
            self.di_text.setText(_translate("Dialog", "       X Min Should be smaller than X Max"))

        self.DiBtn.setText(_translate("Dialog", "OK"))
