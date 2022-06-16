from PySide2 import QtWidgets, QtCore, QtGui
from MyForm import Ui_Form

class MirrorWindow(QtWidgets.QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.initUi()

    def initUi(self):

        self.ui.left_up.clicked.connect(self.on_left_up_button_clicked)
        self.ui.right_up.clicked.connect(self.on_right_up_button_clicked)
        self.ui.left_down.clicked.connect(self.on_left_down_button_clicked)
        self.ui.right_down.clicked.connect(self.on_right_down_button_clicked)
        self.ui.centre.clicked.connect(self.on_centre_button_clicked)






        self.ui.dial.valueChanged.connect(self.value_changed)
        self.ui.dial.sliderMoved.connect(self.slider_position)
        self.ui.dial.sliderPressed.connect(self.slider_pressed)
        self.ui.dial.sliderReleased.connect(self.slider_released)


# ss

    def on_left_up_button_clicked(self):
        self.move(0, 0)

    def on_right_up_button_clicked(self):
        print(QtWidgets.QApplication.screenAt(self.pos()).size().width())
        print(self.width())
        screen_width = QtWidgets.QApplication.screenAt(self.pos()).size().width()
        app_width = self.width()

        x = screen_width - app_width
        self.move(x, 0)

    def on_left_down_button_clicked(self):
        print(QtWidgets.QApplication.screenAt(self.pos()).size().height())
        print(self.height())
        screen_height = QtWidgets.QApplication.screenAt(self.pos()).size().height()
        app_height = self.height()

        y = screen_height - app_height
        self.move(0, y)

    def on_right_down_button_clicked(self):
        screen_height = QtWidgets.QApplication.screenAt(self.pos()).size().height()
        app_height = self.height()
        screen_width = QtWidgets.QApplication.screenAt(self.pos()).size().width()
        app_width = self.width()
        y = screen_height - app_height
        x = screen_width - app_width
        self.move(x, y)

    def on_centre_button_clicked(self):
        screen_height = QtWidgets.QApplication.screenAt(self.pos()).size().height()
        app_height = self.height()
        screen_width = QtWidgets.QApplication.screenAt(self.pos()).size().width()
        app_width = self.width()
        y = screen_height / 2 - app_height / 2
        x = screen_width / 2 - app_width / 2
        self.move(x, y)




    def event(self, event: QtCore.QEvent) -> bool:
        if event.type() == QtCore.QEvent.Resize:
            print(event.size().width())
            print(self.size())
            self.ui.plainTextEdit.appendPlainText(self.size)

        return QtWidgets.QWidget.event(self, event)


    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        print(self.pos().x(), self.pos().y())

    def get_screen_info(self):
        print(QtWidgets.QApplication.screens())
        print(QtWidgets.QApplication.primaryScreen())

        print(self.size)
        print(self.pos())

    def changeEvent(self, event: QtCore.QEvent) -> None:
        print(event.type())
        if event.type() == QtCore.QEvent.Type.WindowStateChange:
            if self.isMinimized():
                print("Окно свернуто")


    def value_changed(self, i):
        print(i)

    def slider_position(self, p):
        print("position", p)

    def slider_pressed(self):
        print("Pressed!")

    def slider_released(self):
        print("Released")

    def get_screen_info(self):
        print(QtWidgets.QApplication.screens())
        print(QtWidgets.QApplication.primaryScreen())

        print(self.size)
        print(self.pos())

        self.ui.plainTextEdit.appendPlainText(self.size)
        # # setplaintext
        # # appendplaintext






if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myWindow = MirrorWindow()
    myWindow.show()

    app.exec_()



# Задания:
# ВЫВОД В ЛОГ

# + Перемещение окна по заданным координатам
#
# Получение параметров экрана + установить для элемента shortCut (горячую клавишу)
#
# Кол-во экранов
# Текущее основное окно
# Разрешение экрана
# На каком экране окно находится
# Размеры окна
# Минимальные размеры окна
# Текущее положение (координаты) окна
# Координаты центра приложения
# Отслеживани bе состояния окна (свернуто/развёрнуто/активно/отображено + время)
#
# ВЫВОД В ТЕРМИНАЛ
# + Информация о координатах при перемещении окна
#
# + Информиция о размерах окна при изменении размера
#
# Значение кнопки когда она была нажата eventFilter
#
# Добавить в dial возможность установки значений кнопками клавиатуры(+ и -), выводить новые значения в лог slots
#
# Законектить между собой QDial, QSlider, QLCDNumber
#
# Для QLCDNumber сделать отображение в различных системах счисления QSettings
#
# Сохранять значение и режима LCDNumber в системные настройки, при перезапуске программы выводить в него соответствующие значения