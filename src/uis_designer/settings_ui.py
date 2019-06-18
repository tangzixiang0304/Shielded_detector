# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(829, 671)
        Form.setStyleSheet("background-color: rgb(255, 221, 215);\n"
"font: 75 11pt \"Adobe 黑体 Std R\";")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 40, 131, 581))
        self.frame.setStyleSheet("QWidget{\n"
"    border:2px solid rgba(205,92,92,255);\n"
"    border-radius:10px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.toolBox = QtWidgets.QToolBox(self.frame)
        self.toolBox.setGeometry(QtCore.QRect(20, 110, 91, 311))
        self.toolBox.setAcceptDrops(False)
        self.toolBox.setStyleSheet("font: 75 11pt \"Adobe 黑体 Std R\";\n"
"border:none\n"
"\n"
"")
        self.toolBox.setObjectName("toolBox")
        self.index_1 = QtWidgets.QWidget()
        self.index_1.setGeometry(QtCore.QRect(0, 0, 91, 179))
        self.index_1.setObjectName("index_1")
        self.toolBox.addItem(self.index_1, "")
        self.index_2 = QtWidgets.QWidget()
        self.index_2.setGeometry(QtCore.QRect(0, 0, 91, 179))
        self.index_2.setObjectName("index_2")
        self.toolBox.addItem(self.index_2, "")
        self.index_3 = QtWidgets.QWidget()
        self.index_3.setGeometry(QtCore.QRect(0, 0, 91, 179))
        self.index_3.setObjectName("index_3")
        self.toolBox.addItem(self.index_3, "")
        self.index_4 = QtWidgets.QWidget()
        self.index_4.setGeometry(QtCore.QRect(0, 0, 91, 179))
        self.index_4.setObjectName("index_4")
        self.toolBox.addItem(self.index_4, "")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(160, 40, 641, 581))
        self.widget.setStyleSheet("QWidget[objectName=widget]\n"
"{\n"
"    \n"
"    border:2px solid rgba(205,92,92,255);\n"
"    border-radius:10px;\n"
"    \n"
"}\n"
"\n"
"*{\n"
"background-color: rgba(255, 0, 0,30);    \n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QtCore.QRect(40, 30, 551, 521))
        self.stackedWidget.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgba(255, 0, 0, 50);    \n"
"    border:2px solid rgba(255,255,255,255);\n"
"}\n"
"\n"
"QComboBox{\n"
"    background-color: rgba(255, 0, 0, 50);    \n"
"    border:2px solid rgba(255,255,255,255);\n"
"    alternate-background-color: rgb(255, 170, 255);\n"
"    selection-background-color: rgb(255, 170, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color:rgba(255,0,0,30)\n"
"}\n"
"\n"
"*{\n"
"background-color: rgba(255, 0, 0, 0);    \n"
"}\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page0 = QtWidgets.QWidget()
        self.page0.setObjectName("page0")
        self.bf_name_gui = QtWidgets.QLineEdit(self.page0)
        self.bf_name_gui.setGeometry(QtCore.QRect(60, 110, 161, 31))
        self.bf_name_gui.setStyleSheet("")
        self.bf_name_gui.setObjectName("bf_name_gui")
        self.bf_sentence_gui = QtWidgets.QLineEdit(self.page0)
        self.bf_sentence_gui.setGeometry(QtCore.QRect(60, 230, 371, 31))
        self.bf_sentence_gui.setStyleSheet("")
        self.bf_sentence_gui.setObjectName("bf_sentence_gui")
        self.label = QtWidgets.QLabel(self.page0)
        self.label.setGeometry(QtCore.QRect(60, 70, 151, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page0)
        self.label_2.setGeometry(QtCore.QRect(60, 190, 371, 31))
        self.label_2.setObjectName("label_2")
        self.next_0_btn = QtWidgets.QPushButton(self.page0)
        self.next_0_btn.setGeometry(QtCore.QRect(410, 450, 111, 41))
        self.next_0_btn.setObjectName("next_0_btn")
        self.label_6 = QtWidgets.QLabel(self.page0)
        self.label_6.setGeometry(QtCore.QRect(60, 310, 71, 16))
        self.label_6.setObjectName("label_6")
        self.check_internal_gui = QtWidgets.QComboBox(self.page0)
        self.check_internal_gui.setGeometry(QtCore.QRect(60, 340, 341, 31))
        self.check_internal_gui.setStyleSheet("")
        self.check_internal_gui.setObjectName("check_internal_gui")
        self.check_internal_gui.addItem("")
        self.check_internal_gui.addItem("")
        self.check_internal_gui.addItem("")
        self.check_internal_gui.addItem("")
        self.check_internal_gui.addItem("")
        self.check_internal_gui.addItem("")
        self.check_internal_gui.addItem("")
        self.check_internal_gui.addItem("")
        self.stackedWidget.addWidget(self.page0)
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.next_1_btn = QtWidgets.QPushButton(self.page1)
        self.next_1_btn.setGeometry(QtCore.QRect(410, 450, 111, 41))
        self.next_1_btn.setObjectName("next_1_btn")
        self.is_jump_out_gui = QtWidgets.QCheckBox(self.page1)
        self.is_jump_out_gui.setGeometry(QtCore.QRect(50, 70, 181, 21))
        self.is_jump_out_gui.setChecked(True)
        self.is_jump_out_gui.setObjectName("is_jump_out_gui")
        self.is_sent_to_file_receiver_gui = QtWidgets.QCheckBox(self.page1)
        self.is_sent_to_file_receiver_gui.setGeometry(QtCore.QRect(50, 140, 201, 16))
        self.is_sent_to_file_receiver_gui.setObjectName("is_sent_to_file_receiver_gui")
        self.is_inform_brothers_gui = QtWidgets.QCheckBox(self.page1)
        self.is_inform_brothers_gui.setGeometry(QtCore.QRect(50, 210, 301, 16))
        self.is_inform_brothers_gui.setObjectName("is_inform_brothers_gui")
        self.add_brother_widget = QtWidgets.QWidget(self.page1)
        self.add_brother_widget.setEnabled(True)
        self.add_brother_widget.setGeometry(QtCore.QRect(50, 240, 381, 261))
        self.add_brother_widget.setObjectName("add_brother_widget")
        self.add_brother_btn = QtWidgets.QPushButton(self.add_brother_widget)
        self.add_brother_btn.setGeometry(QtCore.QRect(260, 10, 51, 31))
        self.add_brother_btn.setObjectName("add_brother_btn")
        self.brother_name = QtWidgets.QLineEdit(self.add_brother_widget)
        self.brother_name.setGeometry(QtCore.QRect(100, 10, 141, 31))
        self.brother_name.setObjectName("brother_name")
        self.label_3 = QtWidgets.QLabel(self.add_brother_widget)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 81, 31))
        self.label_3.setObjectName("label_3")
        self.brother_list_gui = QtWidgets.QListWidget(self.add_brother_widget)
        self.brother_list_gui.setGeometry(QtCore.QRect(20, 60, 311, 101))
        self.brother_list_gui.setStyleSheet("background-color: rgba(255, 0, 0,30);\n"
"border:2px solid rgb(255,255,255);")
        self.brother_list_gui.setObjectName("brother_list_gui")
        self.delete_brother_btn = QtWidgets.QPushButton(self.add_brother_widget)
        self.delete_brother_btn.setGeometry(QtCore.QRect(280, 170, 51, 31))
        self.delete_brother_btn.setObjectName("delete_brother_btn")
        self.label_7 = QtWidgets.QLabel(self.add_brother_widget)
        self.label_7.setGeometry(QtCore.QRect(20, 200, 91, 16))
        self.label_7.setObjectName("label_7")
        self.send_to_brother_message = QtWidgets.QLineEdit(self.add_brother_widget)
        self.send_to_brother_message.setGeometry(QtCore.QRect(20, 220, 301, 31))
        self.send_to_brother_message.setObjectName("send_to_brother_message")
        self.stackedWidget.addWidget(self.page1)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.quickWidget = QtQuickWidgets.QQuickWidget(self.page2)
        self.quickWidget.setGeometry(QtCore.QRect(-230, 640, 300, 200))
        self.quickWidget.setResizeMode(QtQuickWidgets.QQuickWidget.SizeRootObjectToView)
        self.quickWidget.setObjectName("quickWidget")
        self.is_auto_reply_gui = QtWidgets.QCheckBox(self.page2)
        self.is_auto_reply_gui.setGeometry(QtCore.QRect(10, 40, 241, 16))
        self.is_auto_reply_gui.setObjectName("is_auto_reply_gui")
        self.widget_2 = QtWidgets.QWidget(self.page2)
        self.widget_2.setEnabled(True)
        self.widget_2.setGeometry(QtCore.QRect(0, 80, 541, 371))
        self.widget_2.setObjectName("widget_2")
        self.auto_reply_text_gui = QtWidgets.QPlainTextEdit(self.widget_2)
        self.auto_reply_text_gui.setGeometry(QtCore.QRect(10, 40, 521, 321))
        self.auto_reply_text_gui.setObjectName("auto_reply_text_gui")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 171, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(210, 10, 61, 16))
        self.label_5.setObjectName("label_5")
        self.auto_reply_way_gui = QtWidgets.QComboBox(self.widget_2)
        self.auto_reply_way_gui.setGeometry(QtCore.QRect(280, 0, 251, 31))
        self.auto_reply_way_gui.setObjectName("auto_reply_way_gui")
        self.auto_reply_way_gui.addItem("")
        self.auto_reply_way_gui.addItem("")
        self.auto_reply_way_gui.addItem("")
        self.next_2_btn = QtWidgets.QPushButton(self.page2)
        self.next_2_btn.setGeometry(QtCore.QRect(410, 450, 111, 41))
        self.next_2_btn.setObjectName("next_2_btn")
        self.stackedWidget.addWidget(self.page2)
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.is_close_after_inform_gui = QtWidgets.QCheckBox(self.page3)
        self.is_close_after_inform_gui.setGeometry(QtCore.QRect(70, 60, 381, 31))
        self.is_close_after_inform_gui.setChecked(True)
        self.is_close_after_inform_gui.setObjectName("is_close_after_inform_gui")
        self.auto_reply_close = QtWidgets.QCheckBox(self.page3)
        self.auto_reply_close.setEnabled(False)
        self.auto_reply_close.setGeometry(QtCore.QRect(70, 150, 421, 31))
        self.auto_reply_close.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.auto_reply_close.setObjectName("auto_reply_close")
        self.is_stop_by_filereceiver_gui = QtWidgets.QCheckBox(self.page3)
        self.is_stop_by_filereceiver_gui.setGeometry(QtCore.QRect(70, 240, 381, 31))
        self.is_stop_by_filereceiver_gui.setObjectName("is_stop_by_filereceiver_gui")
        self.run_btn = QtWidgets.QPushButton(self.page3)
        self.run_btn.setGeometry(QtCore.QRect(410, 450, 111, 41))
        self.run_btn.setObjectName("run_btn")
        self.stackedWidget.addWidget(self.page3)

        self.retranslateUi(Form)
        self.toolBox.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.is_inform_brothers_gui.toggled['bool'].connect(self.add_brother_widget.setVisible)
        self.toolBox.currentChanged['int'].connect(self.stackedWidget.setCurrentIndex)
        self.is_auto_reply_gui.clicked['bool'].connect(self.auto_reply_close.setChecked)
        self.is_auto_reply_gui.clicked['bool'].connect(self.widget_2.setVisible)
        self.stackedWidget.currentChanged['int'].connect(self.toolBox.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.index_1), _translate("Form", "检测设置"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.index_2), _translate("Form", "通知设置"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.index_3), _translate("Form", "自动回复"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.index_4), _translate("Form", "关闭条件"))
        self.bf_name_gui.setText(_translate("Form", "宝宝"))
        self.bf_sentence_gui.setText(_translate("Form", "宝宝我爱你"))
        self.label.setText(_translate("Form", "TA在你微信里的备注名"))
        self.label_2.setText(_translate("Form", "你想发什么话来检测呢(会是对方看到的第一句话）"))
        self.next_0_btn.setText(_translate("Form", "下一步"))
        self.label_6.setText(_translate("Form", "检测间隔"))
        self.check_internal_gui.setItemText(0, _translate("Form", "5秒"))
        self.check_internal_gui.setItemText(1, _translate("Form", "10秒"))
        self.check_internal_gui.setItemText(2, _translate("Form", "30秒"))
        self.check_internal_gui.setItemText(3, _translate("Form", "1分钟"))
        self.check_internal_gui.setItemText(4, _translate("Form", "2分钟"))
        self.check_internal_gui.setItemText(5, _translate("Form", "5分钟"))
        self.check_internal_gui.setItemText(6, _translate("Form", "10分钟"))
        self.check_internal_gui.setItemText(7, _translate("Form", "20分钟"))
        self.next_1_btn.setText(_translate("Form", "下一步"))
        self.is_jump_out_gui.setText(_translate("Form", "程序弹窗"))
        self.is_sent_to_file_receiver_gui.setText(_translate("Form", "给文件传输助手发消息"))
        self.is_inform_brothers_gui.setText(_translate("Form", "通知微信里其他兄弟，让他们叫我"))
        self.add_brother_btn.setText(_translate("Form", "添加"))
        self.label_3.setText(_translate("Form", "微信备注名"))
        self.delete_brother_btn.setText(_translate("Form", "删除"))
        self.label_7.setText(_translate("Form", "给他们发什么"))
        self.is_auto_reply_gui.setText(_translate("Form", "在你回来之前自动回复TA"))
        self.label_4.setText(_translate("Form", "回复内容(每一行为一条）"))
        self.label_5.setText(_translate("Form", "回复方式"))
        self.auto_reply_way_gui.setItemText(0, _translate("Form", "随机回复"))
        self.auto_reply_way_gui.setItemText(1, _translate("Form", "顺序回复(结束后停止）"))
        self.auto_reply_way_gui.setItemText(2, _translate("Form", "顺序回复(结束后从头开始循环）"))
        self.next_2_btn.setText(_translate("Form", "下一步"))
        self.is_close_after_inform_gui.setText(_translate("Form", "通知结束后自动关闭"))
        self.auto_reply_close.setText(_translate("Form", "检测到你回来后自动关闭（取决于是否设置自动回复）"))
        self.is_stop_by_filereceiver_gui.setText(_translate("Form", "给文件传输助手发送“停止”后关闭"))
        self.run_btn.setText(_translate("Form", "运行"))

from PyQt5 import QtQuickWidgets
