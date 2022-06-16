from PySide2 import QtWidgets, QtCore, QtGui
from New_form import Ui_Form

class MirrorWindow(QtWidgets.QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myWindow = MirrorWindow()
    myWindow.show()

    app.exec_()
