import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QIcon

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Example"
        self.left = 40
        self.top = 40
        self.width = 200
        self.height = 200
        self.statusMessage = 'Belajar PyQt5 '
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width, self.height)
        self.statusBar().showMessage(self.statusMessage)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
