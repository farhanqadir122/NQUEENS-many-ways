from PyQt5 import QtWidgets as qtw, QtCore, QtGui
from MainWindowUI import Ui_MainWindow
import sys, PyQt5
import AstarAlgorithm
import GeneticAlgorithm
from test import draw_board

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


outputAstar = []
outputGenetic = []
displayAstar = False
displayGenetic = False


class MyLogic(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.elitismComboBox.addItem('Elitism')
        self.ui.elitismComboBox.addItem('No Elitism')

        self.ui.runAStarButton.clicked.connect(self.run_astar_algorithm)
        self.ui.runGaButton.clicked.connect(self.run_geneticalgorithm)
        self.ui.showfinalstate.clicked.connect(self.show_final_state)

    def run_astar_algorithm(self):

        N = self.ui.nQueenSpinBox.value()
        global outputAstar
        outputAstar = AstarAlgorithm.runAlgo.run_algo(N)
        global displayAstar
        displayAstar = True
        self.ui.garunninglabel.setText("Check console, too long")
        self.ui.outputLabel.setText("Check console, too long")
        self.ui.astarrunninglabel.setText("Check console, too long")

    def run_geneticalgorithm(self):

        N = self.ui.nQueenSpinBox.value()
        popsize = self.ui.initpopSpinBox.value()
        maxGen = self.ui.maxgenSpinBox.value()
        mutationProb = self.ui.mutprobDoubleSpinBox.value()

        if self.ui.spradioButton.isChecked():
            ctype = 'S'
        elif self.ui.mpradioButton.isChecked():
            ctype = 'M'
        else:
            ctype = 'S'

        crossoverRate = self.ui.crossoverRateDoubleSpinBox.value()
        elitism = self.ui.elitismComboBox.currentText()
        if elitism == 'Elitism':
            elitism = 'Y'
        else:
            elitism = 'N'

        global outputGenetic
        outputGenetic = GeneticAlgorithm.runAlgo.run_algo(N, popsize, maxGen, mutationProb, ctype,
                                                          crossoverRate, elitism)
        global displayGenetic
        displayGenetic = True
        self.ui.garunninglabel.setText("Check console, too long")
        self.ui.outputLabel.setText("Check console, too long")
        self.ui.astarrunninglabel.setText("Check console, too long")

    def show_final_state(self):
        global outputAstar
        global displayGenetic
        global outputGenetic
        global displayAstar

        if displayGenetic:
            draw_board(outputGenetic)
        elif displayAstar:
            draw_board(outputAstar)
        else:
            self.ui.outputLabel.setText("Please run an algorithm first")


if __name__ == '__main__':
    app = qtw.QApplication([])
    win = MyLogic()
    win.show()
    sys.exit(app.exec_())
