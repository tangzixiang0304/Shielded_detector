from src.uis_own.ui_form_own import UI_form_own
from src.uis_own.run_form_own import Run_form_own
from src.workers.itchat_checker import itchat_checker
from src.workers.itchat_worker import itchat_worker
from src.pass_message.program_status import ProgramStatus
from PyQt5.QtCore import QThread
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMessageBox


class detector_controller(QThread):
    @QtCore.pyqtSlot()
    def setting_form_done(self):
        self.setting_ui.hide()
        self.run_ui.setupUi()
        self.run_ui.show()
        self.worker.start()

    def connect(self):
        self.programSignal.settings_done.connect(self.setting_form_done)
        self.programSignal.login_success_signal.connect(self.on_login_success)
        self.programSignal.err_no_name.connect(self.no_name_error)

    def on_login_success(self):
        self.checker.start()

    def open_message_box(self, str):
        msgBox = QMessageBox()
        msgBox.setText(str)
        msgBox.exec()

    def no_name_error(self):
        self.setting_ui.show()
        self.setting_ui.stackedWidget.setCurrentIndex(0)
        self.run_ui.hide()
        self.worker = itchat_worker(self.programSignal)
        self.checker = itchat_checker(self.programSignal)
        str = "我发现你输入的备注名有问题"
        for name in ProgramStatus.not_exist_name:
            str += "  ,“"
            str += name
            str += "”"
        str += " ,这微信备注真的在你的列表里吗？？？修改一下吧"
        print(str)
        self.open_message_box(str)

    def __init__(self, programSignal):
        super().__init__()
        self.programSignal = programSignal
        self.setting_ui = UI_form_own(programSignal)
        self.run_ui = Run_form_own(programSignal)
        self.worker = itchat_worker(programSignal)
        self.checker = itchat_checker(programSignal)
        self.setting_ui.setupUi()
        self.connect()
        self.setting_ui.show()
