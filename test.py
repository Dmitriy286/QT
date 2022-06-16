import sys
from PySide2 import QtWidgets, QtCore, QtGui

class MyWidgets(QtWidgets.QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)

        self.initUi()

    def initUi(self):
        # настройка графического интерфейса
        self.lineEditSource = QtWidgets.QLineEdit()
        self.lineEditSource.setPlaceholderText("Введите исходный текст")

        self.lineEditResult = QtWidgets.QLineEdit()
        self.lineEditResult.setPlaceholderText("Результат")

        self.pushButtonHandle = QtWidgets.QPushButton("Отзеркалить")

        main_layout = QtWidgets.QVBoxLayout()
        lineedit_layout = QtWidgets.QHBoxLayout()

        lineedit_layout.addWidget(self.lineEditSource)
        lineedit_layout.addWidget(self.lineEditResult)

        main_layout.addLayout(lineedit_layout)
        main_layout.addWidget(self.pushButtonHandle)

        self.setLayout(main_layout)



    # настройка слотов/сигнелов
        self.pushButtonHandle.clicked.connect(self.onPushButtonHandleClicked)

    def onPushButtonHandleClicked(self):
        source = self.lineEditSource.text()
        self.lineEditResult.setText(source[::-1])


    def event(self, event: QtCore.QEvent) -> bool:
        if event.type() == QtCore.QEvent.Resize:
            print(event.size().width())

        return QtWidgets.QWidget.event(self, event)

    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        print(self.pos().x(), self.pos().y())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    myWindow = MyWidgets()
    myWindow.show()

    app.exec_()
