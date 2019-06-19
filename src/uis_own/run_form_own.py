from src.uis_designer.run_ui import *
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5 import QtGui
from PyQt5 import QtCore
import time



class Run_form_own(QWidget, Ui_Form):
    def change_to_checking(self):
        self.toolBox.setCurrentIndex(1)

    def change_to_replying(self):
        self.toolBox.setCurrentIndex(2)

    def add_send_message(self):
        self.send_message_time += 1
        self.send_time.setText(str(self.send_message_time))

    @QtCore.pyqtSlot(str)
    def send_auto_reply(self, msg):
        str_add = time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime(time.time()))
        self.listWidget.addItem(str_add + "   :  " + msg)



    def drow_qr(self):
        scene = QGraphicsScene()
        png = QtGui.QPixmap('QR.png')
        scene.addPixmap(png)
        self.QR_plain.setScene(scene)

    def connect(self):
        self.programSignal.login_success_signal.connect(self.change_to_checking)
        self.programSignal.removed_already.connect(self.change_to_replying)
        self.programSignal.send_auto_reply.connect(self.send_auto_reply)
        self.programSignal.send_test_message_signal.connect(self.add_send_message)
        self.programSignal.getting_QR.connect(self.drow_qr)

    def setupUi(self):
        super().setupUi(self)
        self.send_message_time = 0
        self.connect()

    def __init__(self, programSignal):
        super().__init__()
        self.programSignal = programSignal
