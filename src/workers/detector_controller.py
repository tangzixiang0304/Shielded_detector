from src.uis_own.ui_form_own import UI_form_own
from src.uis_own.run_form_own import Run_form_own
from src.workers.itchat_checker import itchat_checker
from src.workers.itchat_worker import itchat_worker
from PyQt5.QtCore import QThread
from PyQt5 import QtCore


class detector_controller(QThread):
    @QtCore.pyqtSlot()
    def setting_form_done(self):
        self.setting_ui.close()
        self.run_ui.setupUi()
        self.run_ui.show()
        self.worker.start()

    def connect(self):
        self.programSignal.settings_done.connect(self.setting_form_done)
        self.programSignal.login_success_signal.connect(self.on_login_success)

    def on_login_success(self):
        self.checker.start()

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
