import random

import PyQt5
import sys
import drawBoard
from PyQt5 import QtWidgets as qtw, QtCore

import UI
from backtracking import nQueens

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class MyLogic(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = UI.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.filtering_comboBox.addItem('None')
        self.ui.filtering_comboBox.addItem('FC')
        self.ui.filtering_comboBox.addItem('AC3')

        self.ui.stop_pushButton.clicked.connect(self.stopAlgo)
        self.ui.show_solution_board_pushButton.clicked.connect(self.runAlgo)

    def runAlgo(self):
        N = self.ui.nqueens_spinBox.value()
        nQueensObject = nQueens(n=N)
        filtering = self.ui.filtering_comboBox.currentText()
        if self.ui.lcv_checkBox.isChecked():
            LCV = True
        else:
            LCV = False
        if self.ui.mrv_checkBox.isChecked():
            MRV = True
        else:
            MRV = False
        if self.ui.mcv_checkBox.isChecked():
            MCV = True
        else:
            MCV = False

        if filtering == "AC3":
            if not LCV:
                filtering = "AC3MRV"
            else:
                filtering = "AC3MRVLCV"

        nQueens.getSolution(nQueensObject, filtering, MRV, LCV, MCV)
        output = f'Steps = {nQueensObject.count} | Time = {nQueensObject.timeTaken}'
        self.ui.output_label.setText(output)

    def stopAlgo(self):
        self.ui.output_label.setText("Solution not reached. Please run again.")
        N = self.ui.nqueens_spinBox.value()
        emptyBoardList = []
        for i in range(N):
            emptyBoardList.append(random.randint(0, N - 1))
        print(emptyBoardList)
        drawBoard.draw_board(emptyBoardList)


if __name__ == '__main__':
    app = qtw.QApplication([])
    win = MyLogic()
    win.show()
    sys.exit(app.exec_())
