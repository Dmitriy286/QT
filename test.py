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

        self.button1 = QtWidgets.QPushButton("1")

        main_layout = QtWidgets.QVBoxLayout()
        lineedit_layout = QtWidgets.QHBoxLayout()

        lineedit_layout.addWidget(self.lineEditSource)
        lineedit_layout.addWidget(self.lineEditResult)

        main_layout.addLayout(lineedit_layout)
        main_layout.addWidget(self.pushButtonHandle)
        main_layout.addWidget(self.button1)

        self.setLayout(main_layout)



    # настройка слотов/сигнелов
        self.pushButtonHandle.clicked.connect(self.onPushButtonHandleClicked)

        self.button1.installEventFilter(self)

    def onPushButtonHandleClicked(self):
        source = self.lineEditSource.text()
        self.lineEditResult.setText(source[::-1])


    def event(self, event: QtCore.QEvent) -> bool:
        if event.type() == QtCore.QEvent.Resize:
            print(event.size().width())

        return QtWidgets.QWidget.event(self, event)

        # if event.type() == QtCore.QEvent.Close:
        #     event.ignore()



    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        print(self.pos().x(), self.pos().y())


    def eventFilter(self, watched:QtCore.QObject, event:QtCore.QEvent) -> bool:
        if watched == self.button1 and event.type() ==QtCore.QEvent.MouseButtonPress:
            print("mouse pressed")
            self.hello(watched)

        return super(MyWidgets, self).eventFilter(watched, event)

    def hello(self, watched):
        print(self.sender())
        print(self.lineEditResult.setText(f"Hello, {watched.text()}"))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    myWindow = MyWidgets()
    myWindow.show()

    app.exec_()
