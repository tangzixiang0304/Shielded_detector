from PyQt5.QtCore import *


class ProgramSignals(QObject):
    settings_done = pyqtSignal()  # settings信息填写完毕

    login_success_signal = pyqtSignal()  # 登录成功
    send_test_message_signal = pyqtSignal()  # 发送了信息
    removed_already = pyqtSignal()  # 已经从黑名单中移除了你
    send_auto_reply = pyqtSignal()  # 发送了自动回复
    you_are_back = pyqtSignal()  # 你回来了

    err_no_girlfriend = pyqtSignal()  # 错误：填写的名称不存在
