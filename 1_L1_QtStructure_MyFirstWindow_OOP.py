import sys
from PySide2 import QtWidgets  # Импорт класса, который содержит элементы окна


class MyFirstWindow(QtWidgets.QMainWindow):  # Наследуемся от QMainWindow

    def __init__(self, parent=None):                 # Создаем конструктор класса
        super().__init__(parent)  # Передаем конструктору ссылку на родительский компонент

        centralWidget = QtWidgets.QWidget()
        v_layout = QtWidgets.QVBoxLayout()

        label = QtWidgets.QLabel("Привет Мир")
        button = QtWidgets.QPushButton("Good Bye, World!")
        button.clicked.connect(lambda: self.close())
        # #
        v_layout.addWidget(label)
        v_layout.addWidget(button)
        # #
        # self.setLayout(v_layout)  # Работать не будет, т.к. нужен центральный виджет
        # #
        self.setCentralWidget(centralWidget)
        centralWidget.setLayout(v_layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication()  # Создаем  объект приложения
    # app = QtWidgets.QApplication(sys.argv)  # Если PyQt

    myWindow = MyFirstWindow()  # Создаём объект окна
    myWindow.show()  # Показываем окно

    sys.exit(app.exec_())  # Если exit, то код дальше не исполняется

