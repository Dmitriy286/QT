from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import QDateTime, QSettings

from MyForm import Ui_Form
import datetime
import time

class MirrorWindow(QtWidgets.QWidget):
    CONFIG = "config.ini"

    def __init__(self, parent = None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.initUi()

        self.load_settings()

    def initUi(self):

        self.ui.left_up.clicked.connect(self.on_left_up_button_clicked)
        self.ui.right_up.clicked.connect(self.on_right_up_button_clicked)
        self.ui.left_down.clicked.connect(self.on_left_down_button_clicked)
        self.ui.right_down.clicked.connect(self.on_right_down_button_clicked)
        self.ui.centre.clicked.connect(self.on_centre_button_clicked)

        self.ui.get_window_data.clicked.connect(self.on_get_window_data_button_clicked)
        self.ui.get_window_data.setShortcut('Ctrl+q')

        # self.ui.dial.sliderMoved.connect(self.slider_position)
        # self.ui.dial.sliderPressed.connect(self.slider_pressed)
        # self.ui.dial.sliderReleased.connect(self.slider_released)
        self.ui.dial.valueChanged.connect(self.value_dial_changed)
        self.ui.slider.valueChanged.connect(self.value_slider_changed)
        # self.ui.slider.valueChanged.connect(self.ui.dial.setValue(self.ui.slider.value()))

        self.ui.get_window_data.installEventFilter(self)
        self.ui.dial.installEventFilter(self)
        self.ui.centre.installEventFilter(self)


        self.ui.comboBox.currentTextChanged.connect(self.setMode)

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

    def on_get_window_data_button_clicked(self):
        self.get_screen_info()


    def event(self, event: QtCore.QEvent) -> bool:
        if event.type() == QtCore.QEvent.Resize:
            print(event.size().width())
            print(self.size())
            str_size = str(self.size())
            self.ui.plainTextEdit.appendPlainText(str_size)

        return QtWidgets.QWidget.event(self, event)

    def changeEvent(self, event: QtCore.QEvent) -> None:
        dt = QDateTime()
        print(event.type())
        if event.type() == QtCore.QEvent.Type.WindowStateChange:
            if self.isMaximized():
                self.ui.plainTextEdit.appendPlainText("Окно развернуто")
                print("Окно развернуто")
            elif self.isMinimized():
                print("Окно свернуто")
                print(datetime.time.strftime("%H:%M:%S"))
                print(dt)
                self.ui.plainTextEdit.appendPlainText("Окно свернуто")
                self.ui.plainTextEdit.appendPlainText(datetime.time.strftime("%H:%M:%S"))
            elif self.isActiveWindow():
                self.ui.plainTextEdit.appendPlainText("Окно активно")
                print("Окно активно")


    def showEvent(self, e):
        dt = QDateTime()
        print("Окно отображено")
        print(datetime.time())
        print(dt.currentDateTime())
        self.ui.plainTextEdit.appendPlainText("Окно отображено")
        self.ui.plainTextEdit.appendPlainText(str(dt.currentDateTime()))

    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        print(self.pos().x(), self.pos().y())

    def get_screen_info(self):
        print("Список объектов всех экранов:")
        print(QtWidgets.QApplication.screens())
        self.ui.plainTextEdit.appendPlainText(str(QtWidgets.QApplication.screens()))
        print("Кол-во экранов:")
        print(len(QtWidgets.QApplication.screens()))
        self.ui.plainTextEdit.appendPlainText(str(len(QtWidgets.QApplication.screens())))
        print("Объект основного окна:")
        print(QtWidgets.QApplication.primaryScreen())
        self.ui.plainTextEdit.appendPlainText(str(QtWidgets.QApplication.primaryScreen()))

        print(QtWidgets.QApplication.allWindows())
        self.ui.plainTextEdit.appendPlainText(str(QtWidgets.QApplication.allWindows()))
        print(QtWidgets.QApplication.activeWindow())
        self.ui.plainTextEdit.appendPlainText(str(QtWidgets.QApplication.activeWindow()))

        print("Размеры окна:")
        print(self.size())
        self.ui.plainTextEdit.appendPlainText(str(self.size()))
        print("Координаты окна:")
        print(self.pos())
        self.ui.plainTextEdit.appendPlainText(str(self.pos()))


        print("Координаты центра приложения:")
        print(self.pos().x() + self.size().width()/2)
        print(self.pos().y() + self.size().height()/2)
        self.ui.plainTextEdit.appendPlainText(str(self.pos().x() + self.size().width()/2))
        self.ui.plainTextEdit.appendPlainText(str(self.pos().y() + self.size().height()/2))

        # # setplaintext
        # # appendplaintext

        print(f"Минимальные размеры окна: {self.minimumWidth()}, {self.minimumHeight()}, \n"
              f"максимальные размеры окна: {self.maximumWidth()}, {self.maximumHeight()}")

        self.desktop = app.desktop()
        print("Разрешение экрана:")
        print(self.desktop.screenGeometry().height())
        print(self.desktop.screenGeometry().width())


    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent):
        if watched == self.ui.centre and event.type() == QtCore.QEvent.KeyPress:
            print(f"key {event.text()} pressed")

        if watched == self.ui.dial and event.type() == QtCore.QEvent.KeyPress:
            print(f"key {event.text()} pressed")

            print(event.type())
            if event.key() == QtCore.Qt.Key_T:
                self.dial_value_change(1)
                print(event.text())
            elif event.key() == QtCore.Qt.Key_Y:
                self.dial_value_change(-1)
                print(event.text())

        return super(MirrorWindow, self).eventFilter(watched, event)

    def value_dial_changed(self):
        self.ui.lcdNumber.display(self.ui.dial.value())

        self.ui.slider.setValue(self.ui.dial.value())

    def value_slider_changed(self):
        self.ui.lcdNumber.display(self.ui.slider.value())

        self.ui.dial.setValue(self.ui.slider.value())

    def dial_value_change(self, i):
        base_value = self.ui.dial.value()
        new_value = base_value + i
        self.ui.dial.setValue(new_value)

    def slider_position(self, p):
        print("position", p)

    def slider_pressed(self):
        print("Pressed!")

    def slider_released(self):
        print("Released")

    def setMode(self):
        if self.ui.comboBox.currentText() == "HEX":
            self.ui.lcdNumber.setHexMode()
            print("HEX")
        elif self.ui.comboBox.currentText() == "BIN":
            self.ui.lcdNumber.setBinMode()
            print("BIN")
        elif self.ui.comboBox.currentText() == "OCT":
            self.ui.lcdNumber.setOctMode()
            print("OCT")
        elif self.ui.comboBox.currentText() == "DEC":
            self.ui.lcdNumber.setDecMode()
            print("DEC")

    def save_settings(self):
        settings = QSettings(self.CONFIG, QSettings.IniFormat)
        settings.setValue("lcdNumber_value", self.ui.lcdNumber.value())
        settings.setValue("combobox_select", self.ui.comboBox.currentText())
        settings.setValue("dial_select", self.ui.dial.value())
        print(type(self.ui.dial.value()))
        print(self.ui.dial.value())
        print(type(settings.value("dial_select", "")))
        print(settings.value("dial_select", ""))
        print(type(settings.value("dial_select")))
        print(settings.value("dial_select"))

    def load_settings(self):
        settings = QSettings(self.CONFIG, QSettings.IniFormat)
        self.ui.comboBox.setCurrentText(settings.value("combobox_select", ""))
        self.ui.lcdNumber.display(settings.value("lcdNumber_value", ""))
        print(type(settings.value("dial_select", "")))
        value = int(settings.value("dial_select", ""))
        print(value)
        self.ui.dial.setValue(value)


    def closeEvent(self, event):
        self.save_settings()
        super().closeEvent(event)



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myWindow = MirrorWindow()
    myWindow.show()

    app.exec_()

# Задания:
# ВЫВОД В ЛОГ

# На каком экране окно находится
#
# ВЫВОД В ТЕРМИНАЛ
#
# Значение кнопки когда она была нажата eventFilter