# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'run_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(681, 663)
        Form.setStyleSheet("background-color: rgb(255, 221, 215);\n"
"font: 75 11pt \"Adobe 黑体 Std R\";")
        self.toolBox = QtWidgets.QToolBox(Form)
        self.toolBox.setGeometry(QtCore.QRect(70, 20, 531, 601))
        self.toolBox.setStyleSheet("font: 75 11pt \"Adobe 黑体 Std R\";\n"
"border:none")
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 531, 502))
        self.page.setAccessibleDescription("")
        self.page.setObjectName("page")
        self.QR_plain = QtWidgets.QGraphicsView(self.page)
        self.QR_plain.setGeometry(QtCore.QRect(0, 0, 521, 491))
        self.QR_plain.setObjectName("QR_plain")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 531, 502))
        self.page_2.setObjectName("page_2")
        self.widget = QtWidgets.QWidget(self.page_2)
        self.widget.setGeometry(QtCore.QRect(50, 70, 431, 161))
        self.widget.setStyleSheet("font: 75 24pt \"Adobe 黑体 Std R\";")
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(60, 20, 161, 61))
        self.label_2.setObjectName("label_2")
        self.send_time = QtWidgets.QLabel(self.widget)
        self.send_time.setGeometry(QtCore.QRect(220, 20, 101, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send_time.sizePolicy().hasHeightForWidth())
        self.send_time.setSizePolicy(sizePolicy)
        self.send_time.setAlignment(QtCore.Qt.AlignCenter)
        self.send_time.setObjectName("send_time")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(320, 20, 31, 61))
        self.label_4.setObjectName("label_4")
        self.widget_2 = QtWidgets.QWidget(self.page_2)
        self.widget_2.setGeometry(QtCore.QRect(90, 260, 351, 121))
        self.widget_2.setObjectName("widget_2")
        self.label_8 = QtWidgets.QLabel(self.widget_2)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 371, 31))
        self.label_8.setObjectName("label_8")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(40, 70, 191, 41))
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(self.widget_2)
        self.label_9.setGeometry(QtCore.QRect(40, 40, 161, 31))
        self.label_9.setObjectName("label_9")
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 531, 502))
        self.page_3.setObjectName("page_3")
        self.label_10 = QtWidgets.QLabel(self.page_3)
        self.label_10.setGeometry(QtCore.QRect(70, 20, 451, 21))
        self.label_10.setObjectName("label_10")
        self.listWidget = QtWidgets.QListWidget(self.page_3)
        self.listWidget.setGeometry(QtCore.QRect(10, 50, 511, 391))
        self.listWidget.setObjectName("listWidget")
        self.toolBox.addItem(self.page_3, "")

        self.retranslateUi(Form)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Form", "扫描二维码"))
        self.label_2.setText(_translate("Form", "已经测试了"))
        self.send_time.setText(_translate("Form", "0"))
        self.label_4.setText(_translate("Form", "次"))
        self.label_8.setText(_translate("Form", "温馨提示:"))
        self.label_3.setText(_translate("Form", "小舔怡情，大添伤身"))
        self.label_9.setText(_translate("Form", "舔狗不得house"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Form", "她还没把你移除黑名单"))
        self.label_10.setText(_translate("Form", "自动回复中，你快回来，我一个人应付不来"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("Form", "她把你移出来啦！"))

