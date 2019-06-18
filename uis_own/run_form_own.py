from uis_designer.run_ui import *
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5 import QtGui


class Run_form_own(QWidget, Ui_Form):
    def change_to_checking(self):
        self.toolBox.setCurrentIndex(1)

    def change_to_replying(self):
        self.toolBox.setCurrentIndex(2)

    def add_send_message(self):
        self.send_message_time += 1
        self.send_time.setText(str(self.send_message_time))

    def drow_qr(self):
        scene = QGraphicsScene()
        png = QtGui.QPixmap('QR.png')
        scene.addPixmap(png)
        self.QR_plain.setScene(scene)

    def connect(self):
        self.programSignal.login_success_signal.connect(self.change_to_checking)
        self.programSignal.removed_already.connect(self.change_to_replying)
        self.programSignal.send_auto_reply.connect(self.add_send_message)
        self.programSignal.send_test_message_signal.connect(self.add_send_message)

    def setupUi(self):
        super().setupUi(self)
        self.send_message_time = 0
        self.connect()

    def __init__(self, programSignal):
        super().__init__()
        self.programSignal = programSignal
