# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MyForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(694, 478)
        self.horizontalLayout_5 = QHBoxLayout(Form)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_up = QPushButton(Form)
        self.left_up.setObjectName(u"left_up")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_up.sizePolicy().hasHeightForWidth())
        self.left_up.setSizePolicy(sizePolicy)
        self.left_up.setMinimumSize(QSize(0, 40))

        self.horizontalLayout.addWidget(self.left_up)

        self.right_up = QPushButton(Form)
        self.right_up.setObjectName(u"right_up")
        self.right_up.setMinimumSize(QSize(0, 40))

        self.horizontalLayout.addWidget(self.right_up)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.centre = QPushButton(Form)
        self.centre.setObjectName(u"centre")
        self.centre.setMinimumSize(QSize(0, 40))

        self.verticalLayout_3.addWidget(self.centre)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.left_down = QPushButton(Form)
        self.left_down.setObjectName(u"left_down")
        self.left_down.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_2.addWidget(self.left_down)

        self.right_down = QPushButton(Form)
        self.right_down.setObjectName(u"right_down")
        self.right_down.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_2.addWidget(self.right_down)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.get_window_data = QPushButton(Form)
        self.get_window_data.setObjectName(u"get_window_data")

        self.verticalLayout_3.addWidget(self.get_window_data)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.dial = QDial(Form)
        self.dial.setObjectName(u"dial")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dial.sizePolicy().hasHeightForWidth())
        self.dial.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.dial)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEditable(False)

        self.verticalLayout.addWidget(self.comboBox)

        self.lcdNumber = QLCDNumber(Form)
        self.lcdNumber.setObjectName(u"lcdNumber")

        self.verticalLayout.addWidget(self.lcdNumber)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.slider = QSlider(Form)
        self.slider.setObjectName(u"slider")
        self.slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.slider)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.plainTextEdit = QPlainTextEdit(Form)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.plainTextEdit)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.left_up.setText(QCoreApplication.translate("Form", u"\u041b\u0435\u0432\u043e/\u0412\u0435\u0440\u0445", None))
        self.right_up.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0430\u0432\u043e/\u0412\u0435\u0440\u0445", None))
        self.centre.setText(QCoreApplication.translate("Form", u"\u0426\u0435\u043d\u0442\u0440", None))
        self.left_down.setText(QCoreApplication.translate("Form", u"\u041b\u0435\u0432\u043e/\u041d\u0438\u0437", None))
        self.right_down.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0430\u0432\u043e/\u041d\u0438\u0437", None))
        self.get_window_data.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u043e\u043a\u043d\u0430", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"HEX", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"DEC", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"OCT", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"BIN", None))

    # retranslateUi

