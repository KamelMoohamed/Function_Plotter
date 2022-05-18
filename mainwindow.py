from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
from PyQt5 import QtCore, QtGui, QtWidgets
from Dialog import Ui_Dialog

import numpy as np
from calculation.evaluation import evaluation
from Eval_Calculation import Eval


class Ui_MatplotlibWindow(object):
    def setupUi(self, MatplotlibWindow):
        MatplotlibWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        MatplotlibWindow.setObjectName("MatplotlibWindow")
        MatplotlibWindow.setEnabled(True)
        MatplotlibWindow.resize(966, 692)
        MatplotlibWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MatplotlibWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.backgorund = QtWidgets.QLabel(self.centralwidget)
        self.backgorund.setEnabled(True)
        self.backgorund.setGeometry(QtCore.QRect(0, 0, 961, 691))
        font = QtGui.QFont()
        self.backgorund.setFont(font)
        self.backgorund.setAutoFillBackground(False)
        self.backgorund.setText("")
        self.backgorund.setPixmap(QtGui.QPixmap(":/stockes/resources/whiteBackground.png"))
        self.backgorund.setObjectName("backgorund")
        self.closeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.closeBtn.setGeometry(QtCore.QRect(910, 20, 20, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeBtn.sizePolicy().hasHeightForWidth())
        self.closeBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("IROicons")
        font.setPointSize(21)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.closeBtn.setFont(font)
        self.closeBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeBtn.setToolTip("")
        self.closeBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.closeBtn.setStyleSheet("border-radius:10px;\n"
                                    "color: #710101;\n"
                                    "text-align: left;\n"
                                    "font: 21pt \"IROicons\";")
        self.closeBtn.setCheckable(False)
        self.closeBtn.setDefault(False)
        self.closeBtn.setFlat(False)
        self.closeBtn.setObjectName("closeBtn")
        self.miniBtn = QtWidgets.QPushButton(self.centralwidget)
        self.miniBtn.setGeometry(QtCore.QRect(880, 20, 20, 21))
        font = QtGui.QFont()
        font.setFamily("IROicons")
        font.setPointSize(21)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.miniBtn.setFont(font)
        self.miniBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.miniBtn.setStyleSheet("border-radius:10px;\n"
                                   "color: #000;\n"
                                   "text-align: left;\n"
                                   "font: 21pt \"IROicons\";")
        self.miniBtn.setObjectName("miniBtn")
        self.eq_input = QtWidgets.QLineEdit(self.centralwidget)
        self.eq_input.setGeometry(QtCore.QRect(110, 18, 191, 33))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.eq_input.setFont(font)
        self.eq_input.setStyleSheet("background-color: #f9f9f9;\n"
                                    "color: black;\n"
                                    "border-radius: 15px;\n"
                                    "padding: 45px;\n"
                                    "font: 9pt \"Montserrat\";\n"
                                    "")
        self.eq_input.setText("")
        self.eq_input.setObjectName("eq_input")
        self.eq_icon = QtWidgets.QLabel(self.centralwidget)
        self.eq_icon.setGeometry(QtCore.QRect(120, 18, 22, 31))
        font = QtGui.QFont()
        font.setFamily("IROicons")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.eq_icon.setFont(font)
        self.eq_icon.setStyleSheet("font: 20pt \"IROicons\";")
        self.eq_icon.setObjectName("eq_icon")
        self.redVal = QtWidgets.QLabel(self.centralwidget)
        self.redVal.setGeometry(QtCore.QRect(280, 670, 51, 16))
        font = QtGui.QFont()
        self.redVal.setFont(font)
        self.redVal.setObjectName("redVal")
        self.greenVal = QtWidgets.QLabel(self.centralwidget)
        self.greenVal.setGeometry(QtCore.QRect(440, 670, 51, 16))
        font = QtGui.QFont()
        self.greenVal.setFont(font)
        self.greenVal.setObjectName("greenVal")
        self.blueVal = QtWidgets.QLabel(self.centralwidget)
        self.blueVal.setGeometry(QtCore.QRect(610, 670, 51, 16))
        font = QtGui.QFont()
        self.blueVal.setFont(font)
        self.blueVal.setObjectName("blueVal")
        self.lineWVal = QtWidgets.QLabel(self.centralwidget)
        self.lineWVal.setGeometry(QtCore.QRect(1060, 829, 111, 16))
        font = QtGui.QFont()
        self.lineWVal.setFont(font)
        self.lineWVal.setObjectName("lineWVal")
        self.menu = QtWidgets.QGroupBox(self.centralwidget)
        self.menu.setGeometry(QtCore.QRect(50, -115, 121, 111))
        self.menu.setStyleSheet("background-color:  #fff;\n"
                                "border-radius: 15px;")
        self.menu.setTitle("")
        self.menu.setObjectName("menu")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.menu)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 121, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.menuNew = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.menuNew.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "color: rgb(0, 0, 0);\n"
                                   "font: 9pt \"Montserrat\";")
        self.menuNew.setObjectName("menuNew")
        self.verticalLayout.addWidget(self.menuNew)
        self.menuOpen = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.menuOpen.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "color: rgb(0, 0, 0);\n"
                                    "font: 9pt \"Montserrat\";")
        self.menuOpen.setObjectName("menuOpen")
        self.verticalLayout.addWidget(self.menuOpen)
        self.menuSave = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.menuSave.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "color: rgb(0, 0, 0);\n"
                                    "font: 9pt \"Montserrat\";")
        self.menuSave.setObjectName("menuSave")
        self.verticalLayout.addWidget(self.menuSave)
        self.eq_label = QtWidgets.QLabel(self.centralwidget)
        self.eq_label.setGeometry(QtCore.QRect(10, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.eq_label.setFont(font)
        self.eq_label.setTextFormat(QtCore.Qt.PlainText)
        self.eq_label.setObjectName("eq_label")
        self.min_input = QtWidgets.QLineEdit(self.centralwidget)
        self.min_input.setGeometry(QtCore.QRect(410, 20, 161, 33))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.min_input.setFont(font)
        self.min_input.setStyleSheet("background-color: #f9f9f9;\n"
                                     "color: black;\n"
                                     "border-radius: 15px;\n"
                                     "padding: 45px;\n"
                                     "font: 9pt \"Montserrat\";\n"
                                     "")
        self.min_input.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.min_input.setText("")
        self.min_input.setObjectName("min_input")
        self.min_label = QtWidgets.QLabel(self.centralwidget)
        self.min_label.setGeometry(QtCore.QRect(320, 22, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.min_label.setFont(font)
        self.min_label.setTextFormat(QtCore.Qt.PlainText)
        self.min_label.setObjectName("min_label")
        self.max_label = QtWidgets.QLabel(self.centralwidget)
        self.max_label.setGeometry(QtCore.QRect(600, 25, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.max_label.setFont(font)
        self.max_label.setTextFormat(QtCore.Qt.PlainText)
        self.max_label.setObjectName("max_label")
        self.max_input = QtWidgets.QLineEdit(self.centralwidget)
        self.max_input.setGeometry(QtCore.QRect(690, 21, 161, 33))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.max_input.setFont(font)
        self.max_input.setStyleSheet("background-color: #f9f9f9;\n"
                                     "color: black;\n"
                                     "border-radius: 15px;\n"
                                     "padding: 45px;\n"
                                     "font: 9pt \"Montserrat\";\n"
                                     "")
        self.max_input.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.max_input.setText("")
        self.max_input.setObjectName("max_input")
        self.graph_widget = MpWidget(self.centralwidget)
        self.graph_widget.setGeometry(QtCore.QRect(18, 110, 931, 551))
        self.graph_widget.setStyleSheet("background-color: #f4f5f5;\n"
                                        "border-radius: 20px;\n"
                                        "border-top-right-radius: 0px;\n"
                                        "border-bottom-right-radius: 0px;")
        self.graph_widget.setObjectName("graph_widget")
        self.plotBtn = QtWidgets.QPushButton(self.centralwidget)
        self.plotBtn.setGeometry(QtCore.QRect(875, 60, 61, 33))
        self.plotBtn.setStyleSheet("background-color: #dc425e;\n"
                                   "color: black;\n"
                                   "border-radius: 15px;\n"
                                   "padding: 45px;\\n\n"
                                   "font: 9pt \\\"Montserrat\\\";")
        self.plotBtn.clicked.connect(self.plot)
        self.plotBtn.setObjectName("plotBtn")
        self.message_1 = QtWidgets.QLabel(self.centralwidget)
        self.message_1.setGeometry(QtCore.QRect(10, 70, 841, 21))

        self.message_2 = QtWidgets.QLabel(self.centralwidget)
        self.message_2.setGeometry(QtCore.QRect(10, 95, 841, 21))


        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.message_1.setFont(font)
        self.message_1.setTextFormat(QtCore.Qt.PlainText)
        self.message_1.setObjectName("message_1")

        self.message_2.setFont(font)
        self.message_2.setTextFormat(QtCore.Qt.PlainText)
        self.message_2.setObjectName("message_2")


        MatplotlibWindow.setCentralWidget(self.centralwidget)
        MatplotlibWindow.addToolBar(NavigationToolbar(self.graph_widget.canvas, MatplotlibWindow))

        self.retranslateUi(MatplotlibWindow)
        self.closeBtn.clicked.connect(MatplotlibWindow.close)
        self.miniBtn.clicked.connect(MatplotlibWindow.showMinimized)

        QtCore.QMetaObject.connectSlotsByName(MatplotlibWindow)


    def retranslateUi(self, MatplotlibWindow):
        _translate = QtCore.QCoreApplication.translate
        MatplotlibWindow.setWindowTitle(_translate("MatplotlibWindow", "MainWindow"))
        self.closeBtn.setText(_translate("MatplotlibWindow", "x"))
        self.miniBtn.setText(_translate("MatplotlibWindow", "y"))
        self.eq_input.setToolTip(
            _translate("MatplotlibWindow", "<html><head/><body><p>Search for Item</p></body></html>"))
        self.eq_icon.setText(_translate("MatplotlibWindow", "c"))
        self.redVal.setText(_translate("MatplotlibWindow", "R: 0 "))
        self.greenVal.setText(_translate("MatplotlibWindow", "G: 0  "))
        self.blueVal.setText(_translate("MatplotlibWindow", "B:0"))
        self.lineWVal.setText(_translate("MatplotlibWindow", "Line Weight: 0"))
        self.menuNew.setToolTip(
            _translate("MatplotlibWindow", "<html><head/><body><p>Make a New Draw</p></body></html>"))
        self.menuNew.setText(_translate("MatplotlibWindow", "New"))
        self.menuOpen.setToolTip(_translate("MatplotlibWindow", "<html><head/><body><p>Open a Draw</p></body></html>"))
        self.menuOpen.setText(_translate("MatplotlibWindow", "Open"))
        self.menuSave.setToolTip(_translate("MatplotlibWindow", "<html><head/><body><p>Save a Draw</p></body></html>"))
        self.menuSave.setText(_translate("MatplotlibWindow", "Save"))
        self.eq_label.setText(_translate("MatplotlibWindow", "Eqution:"))
        self.min_input.setToolTip(
            _translate("MatplotlibWindow", "<html><head/><body><p>Search for Item</p></body></html>"))
        self.min_label.setText(_translate("MatplotlibWindow", "Min X Value:"))
        self.max_label.setText(_translate("MatplotlibWindow", "Max X Value:"))
        self.max_input.setToolTip(
            _translate("MatplotlibWindow", "<html><head/><body><p>Search for Item</p></body></html>"))
        self.plotBtn.setText(_translate("MatplotlibWindow", "Plot"))
        self.message_1.setText(_translate("MatplotlibWindow",
                                          " - Please enter f(x) in terms of [+, -, *, /, ^, (, ) ] operators. Also "
                                          "min, max x values to draw the function."))
        self.message_2.setText(_translate("MatplotlibWindow",
                                          " - Also you can use the above toolbar to set graph title, labels, colors, "
                                          "limits and others."))


    def plot(self):
        if self.eq_input.text() != "" and self.min_input.text() != "" and self.max_input.text() != "":
            self.min_text = float(self.min_input.text())
            self.max_text = float(self.max_input.text())
            if self.min_text >= self.max_text:
                self.openDialog(2)
            try:
                self.eq_text = self.eq_input.text()
                self.update_graph()
            except:
                self.openDialog(0)
        else:
            self.openDialog(1)


    def update_graph(self, interpreter=True):
        if interpreter:
            e = evaluation()
        else:
            e = Eval()

        step = 0.1
        x = np.arange(float(self.min_text), float(self.max_text), step)
        y = [e.calculate(self.eq_text, i) for i in x]

        self.graph_widget.canvas.axes.clear()

        self.graph_widget.canvas.axes.plot(x, y)
        self.graph_widget.canvas.draw()

    def openDialog(self, errorNumber):
        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_Dialog(errorNumber)
        dialog.ui.setupUi(dialog)
        dialog.setGeometry(QtCore.QRect(300, 300, 385, 155))
        dialog.exec_()
        dialog.show()

from mpwidget import MpWidget
import resources_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MatplotlibWindow = QtWidgets.QMainWindow()
    ui = Ui_MatplotlibWindow()
    ui.setupUi(MatplotlibWindow)
    MatplotlibWindow.show()
    sys.exit(app.exec_())
