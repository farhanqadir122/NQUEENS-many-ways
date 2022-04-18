# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(730, 519)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(180, 0, 331, 71))
        self.outputLabel.setTextFormat(QtCore.Qt.RichText)
        self.outputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.runAStarButton = QtWidgets.QPushButton(self.centralwidget)
        self.runAStarButton.setGeometry(QtCore.QRect(110, 370, 121, 41))
        self.runAStarButton.setStyleSheet("")
        self.runAStarButton.setObjectName("runAStarButton")
        self.mutprobDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.mutprobDoubleSpinBox.setGeometry(QtCore.QRect(530, 230, 51, 22))
        self.mutprobDoubleSpinBox.setMaximum(1.0)
        self.mutprobDoubleSpinBox.setProperty("value", 0.8)
        self.mutprobDoubleSpinBox.setObjectName("mutprobDoubleSpinBox")
        self.mutProbLabel = QtWidgets.QLabel(self.centralwidget)
        self.mutProbLabel.setGeometry(QtCore.QRect(410, 230, 111, 21))
        self.mutProbLabel.setObjectName("mutProbLabel")
        self.nQueenSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.nQueenSpinBox.setGeometry(QtCore.QRect(371, 80, 51, 22))
        self.nQueenSpinBox.setMinimum(4)
        self.nQueenSpinBox.setMaximum(100)
        self.nQueenSpinBox.setObjectName("nQueenSpinBox")
        self.nQueensLabel = QtWidgets.QLabel(self.centralwidget)
        self.nQueensLabel.setGeometry(QtCore.QRect(250, 80, 101, 21))
        self.nQueensLabel.setObjectName("nQueensLabel")
        self.initpopSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.initpopSpinBox.setGeometry(QtCore.QRect(531, 170, 51, 22))
        self.initpopSpinBox.setMinimum(5)
        self.initpopSpinBox.setMaximum(150)
        self.initpopSpinBox.setObjectName("initpopSpinBox")
        self.initpopLabel = QtWidgets.QLabel(self.centralwidget)
        self.initpopLabel.setGeometry(QtCore.QRect(410, 170, 101, 21))
        self.initpopLabel.setObjectName("initpopLabel")
        self.maxgenLabel = QtWidgets.QLabel(self.centralwidget)
        self.maxgenLabel.setGeometry(QtCore.QRect(410, 200, 111, 21))
        self.maxgenLabel.setObjectName("maxgenLabel")
        self.maxgenSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.maxgenSpinBox.setGeometry(QtCore.QRect(530, 200, 51, 22))
        self.maxgenSpinBox.setMinimum(100)
        self.maxgenSpinBox.setMaximum(1000000)
        self.maxgenSpinBox.setObjectName("maxgenSpinBox")
        self.runGaButton = QtWidgets.QPushButton(self.centralwidget)
        self.runGaButton.setGeometry(QtCore.QRect(470, 370, 151, 41))
        self.runGaButton.setObjectName("runGaButton")
        self.stopbutton = QtWidgets.QPushButton(self.centralwidget)
        self.stopbutton.setGeometry(QtCore.QRect(300, 430, 121, 31))
        self.stopbutton.setObjectName("stopbutton")
        self.hLine3 = QtWidgets.QFrame(self.centralwidget)
        self.hLine3.setGeometry(QtCore.QRect(0, 460, 731, 21))
        self.hLine3.setFrameShape(QtWidgets.QFrame.HLine)
        self.hLine3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hLine3.setObjectName("hLine3")
        self.crossoverTypeLabel = QtWidgets.QLabel(self.centralwidget)
        self.crossoverTypeLabel.setGeometry(QtCore.QRect(410, 260, 101, 21))
        self.crossoverTypeLabel.setObjectName("crossoverTypeLabel")
        self.crossoverRateLabel = QtWidgets.QLabel(self.centralwidget)
        self.crossoverRateLabel.setGeometry(QtCore.QRect(410, 290, 101, 21))
        self.crossoverRateLabel.setObjectName("crossoverRateLabel")
        self.crossoverRateDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.crossoverRateDoubleSpinBox.setGeometry(QtCore.QRect(530, 290, 51, 22))
        self.crossoverRateDoubleSpinBox.setMinimum(0.2)
        self.crossoverRateDoubleSpinBox.setMaximum(1.0)
        self.crossoverRateDoubleSpinBox.setProperty("value", 0.8)
        self.crossoverRateDoubleSpinBox.setObjectName("crossoverRateDoubleSpinBox")
        self.elitismLabel = QtWidgets.QLabel(self.centralwidget)
        self.elitismLabel.setGeometry(QtCore.QRect(410, 320, 101, 21))
        self.elitismLabel.setObjectName("elitismLabel")
        self.elitismComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.elitismComboBox.setGeometry(QtCore.QRect(530, 320, 161, 22))
        self.elitismComboBox.setObjectName("elitismComboBox")
        self.spradioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.spradioButton.setGeometry(QtCore.QRect(530, 260, 83, 18))
        self.spradioButton.setObjectName("spradioButton")
        self.mpradioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.mpradioButton.setGeometry(QtCore.QRect(620, 260, 83, 18))
        self.mpradioButton.setObjectName("mpradioButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 100, 731, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(350, 110, 20, 311))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(-3, 410, 731, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.astarrunninglabel = QtWidgets.QLabel(self.centralwidget)
        self.astarrunninglabel.setGeometry(QtCore.QRect(10, 120, 341, 221))
        self.astarrunninglabel.setTextFormat(QtCore.Qt.RichText)
        self.astarrunninglabel.setAlignment(QtCore.Qt.AlignCenter)
        self.astarrunninglabel.setObjectName("astarrunninglabel")
        self.garunninglabel = QtWidgets.QLabel(self.centralwidget)
        self.garunninglabel.setGeometry(QtCore.QRect(370, 120, 321, 41))
        self.garunninglabel.setTextFormat(QtCore.Qt.RichText)
        self.garunninglabel.setAlignment(QtCore.Qt.AlignCenter)
        self.garunninglabel.setObjectName("garunninglabel")
        self.showfinalstate = QtWidgets.QPushButton(self.centralwidget)
        self.showfinalstate.setGeometry(QtCore.QRect(470, 430, 121, 31))
        self.showfinalstate.setStyleSheet("")
        self.showfinalstate.setObjectName("showfinalstate")
        self.tracebutton = QtWidgets.QPushButton(self.centralwidget)
        self.tracebutton.setGeometry(QtCore.QRect(110, 430, 121, 31))
        self.tracebutton.setObjectName("tracebutton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 730, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.outputLabel.setText(_translate("MainWindow", "Total Steps and Time Information"))
        self.runAStarButton.setText(_translate("MainWindow", "Run A* Algorithm"))
        self.mutProbLabel.setText(_translate("MainWindow", "Mutation probability:"))
        self.nQueensLabel.setText(_translate("MainWindow", "No. of Queens"))
        self.initpopLabel.setText(_translate("MainWindow", "Population Size:"))
        self.maxgenLabel.setText(_translate("MainWindow", "Max generation:"))
        self.runGaButton.setText(_translate("MainWindow", "Run Genetic Algorithm"))
        self.stopbutton.setText(_translate("MainWindow", "Stop"))
        self.crossoverTypeLabel.setText(_translate("MainWindow", "Crossover type"))
        self.crossoverRateLabel.setText(_translate("MainWindow", "Crossover rate"))
        self.elitismLabel.setText(_translate("MainWindow", "Other Options:"))
        self.spradioButton.setText(_translate("MainWindow", "SP"))
        self.mpradioButton.setText(_translate("MainWindow", "MP"))
        self.astarrunninglabel.setText(_translate("MainWindow", "Algorithm running..."))
        self.garunninglabel.setText(_translate("MainWindow", "Algorithm running..."))
        self.showfinalstate.setText(_translate("MainWindow", "Show Final State"))
        self.tracebutton.setText(_translate("MainWindow", "Trace Path"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
