import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore


number1 = None
number2 = None
has_clicked_operator = False
operator = ""


class Window(QWidget):
    def __init__(self, number1, number2, has_clicked_operator, operator):
        super().__init__()
        self.number1 = number1
        self.number2 = number2
        self.has_clicked_operator = has_clicked_operator
        self.operator = operator
        self.num = 0
        self.setGeometry(100, 100, 300, 600)
        self.setStyleSheet("background-color: #173F5F;"
                           "font-size: 20px;"
                           "color: #FFFFFF;")
        self.setWindowTitle('4 Function Calculator')
        self.UI()

    def UI(self):
        # Buttons / Labels
        self.numLabel = QLabel("0", self)
        self.numLabel.setGeometry(0, 0, 300, 100)
        self.numLabel.setStyleSheet("color: #FFFFFF;"
                                    "padding-right: 28px;")
        self.numLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        plusButton = QPushButton("+", self)
        plusButton.setGeometry(0, 100, 75, 100)
        plusButton.setStyleSheet("background-color: #ED553B")
        minusButton = QPushButton("-", self)
        minusButton.setGeometry(75, 100, 75, 100)
        minusButton.setStyleSheet("background-color: #ED553B")
        divideButton = QPushButton("÷", self)
        divideButton.setGeometry(150, 100, 75, 100)
        divideButton.setStyleSheet("background-color: #ED553B")
        multiplyButton = QPushButton("×", self)
        multiplyButton.setGeometry(225, 100, 75, 100)
        multiplyButton.setStyleSheet("background-color: #ED553B")
        button1 = QPushButton("1", self)
        button1.setGeometry(0, 200, 100, 100)
        button1.setStyleSheet("background-color: #20639B")
        button2 = QPushButton("2", self)
        button2.setGeometry(100, 200, 100, 100)
        button2.setStyleSheet("background-color: #20639B")
        button3 = QPushButton("3", self)
        button3.setGeometry(200, 200, 100, 100)
        button3.setStyleSheet("background-color: #20639B")
        button4 = QPushButton("4", self)
        button4.setGeometry(0, 300, 100, 100)
        button4.setStyleSheet("background-color: #20639B")
        button5 = QPushButton("5", self)
        button5.setGeometry(100, 300, 100, 100)
        button5.setStyleSheet("background-color: #20639B")
        button6 = QPushButton("6", self)
        button6.setGeometry(200, 300, 100, 100)
        button6.setStyleSheet("background-color: #20639B")
        button7 = QPushButton("7", self)
        button7.setGeometry(0, 400, 100, 100)
        button7.setStyleSheet("background-color: #20639B")
        button8 = QPushButton("8", self)
        button8.setGeometry(100, 400, 100, 100)
        button8.setStyleSheet("background-color: #20639B")
        button9 = QPushButton("9", self)
        button9.setGeometry(200, 400, 100, 100)
        button9.setStyleSheet("background-color: #20639B")
        button0 = QPushButton("0", self)
        button0.setGeometry(100, 500, 100, 100)
        button0.setStyleSheet("background-color: #20639B")
        clearButton = QPushButton("C", self)
        clearButton.setGeometry(0, 500, 100, 100)
        clearButton.setStyleSheet("background-color: #173F5F")
        equalsButton = QPushButton("=", self)
        equalsButton.setGeometry(200, 500, 100, 100)
        equalsButton.setStyleSheet("background-color: #173F5F")
        # Functions
        clearButton.clicked.connect(self.clearFunc)
        plusButton.clicked.connect(self.addFunc)
        minusButton.clicked.connect(self.minusFunc)
        divideButton.clicked.connect(self.divideFunc)
        multiplyButton.clicked.connect(self.multiplyFunc)
        equalsButton.clicked.connect(self.getNum)
        button1.clicked.connect(lambda: self.numFunc(1))
        button2.clicked.connect(lambda: self.numFunc(2))
        button3.clicked.connect(lambda: self.numFunc(3))
        button4.clicked.connect(lambda: self.numFunc(4))
        button5.clicked.connect(lambda: self.numFunc(5))
        button6.clicked.connect(lambda: self.numFunc(6))
        button7.clicked.connect(lambda: self.numFunc(7))
        button8.clicked.connect(lambda: self.numFunc(8))
        button9.clicked.connect(lambda: self.numFunc(9))
        button0.clicked.connect(lambda: self.numFunc(0))
        self.show()

    def clearFunc(self):
        self.number1 = None
        self.number2 = None
        self.has_clicked_operator = False
        self.numLabel.setText("0")

    def addFunc(self):
        self.has_clicked_operator = True
        self.operator = "add"
        self.numLabel.setText("")


    def divideFunc(self):
        self.has_clicked_operator = True
        self.operator = "divide"
        self.numLabel.setText("")

    def multiplyFunc(self):
        self.has_clicked_operator = True
        self.operator = "multiply"
        self.numLabel.setText("")

    def minusFunc(self):
        self.has_clicked_operator = True
        self.operator = "minus"
        self.numLabel.setText("")

    def getNum(self):
        if self.operator == "add":
            result = self.number1 + self.number2
        elif self.operator == "minus":
            result = self.number1 - self.number2
        elif self.operator == "divide":
            result = self.number1 / self.number2
            result = str(result)
            if result[-2:] == ".0":
                result = result[:-2]
                result = int(result)
        else:
            result = self.number1 * self.number2
        self.numLabel.setText(str(result))
        self.number1 = result
        self.number2 = None
        self.operator = ""
        self.has_clicked_operator = False

    def numFunc(self, num):
        if not self.has_clicked_operator:
            if self.number1 == None:
                val = str(num)
            else:
                val = str(self.number1) + str(num)
            self.numLabel.setText(val)
            self.number1 = int(val)
        else:
            if self.number2 == None:
                val = str(num)
            else:
                val = str(self.number2) + str(num)
            self.numLabel.setText(val)
            self.number2 = int(val)


def main():
    App = QApplication(sys.argv)
    window = Window(number1, number2, has_clicked_operator, operator)
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
