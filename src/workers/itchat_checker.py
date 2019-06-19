from PyQt5.QtCore import QThread
from src.pass_message.settings import Settings
import time
import itchat
from src.pass_message.program_status import ProgramStatus
import random


class itchat_checker(QThread):
    def check_process(self):
        while True:
            if ProgramStatus.gf_username != "":
                before_send = ProgramStatus.test_message_reply
                print("send", itchat.send_msg(Settings.bf_sentence, ProgramStatus.gf_username))
                self.programSignal.send_test_message_signal.emit()
                time.sleep(0.5)
                after_send = ProgramStatus.test_message_reply
                if not after_send == before_send + 1:
                    ProgramStatus.is_black = False
                    self.programSignal.removed_already.emit()

            time.sleep(Settings.check_internal)
            if not ProgramStatus.is_black:
                return

    def inform_process(self):
        if Settings.is_inform_brothers:
            for bro_name in ProgramStatus.brother_username:
                itchat.send_msg(Settings.send_to_brother_message, bro_name)
                time.sleep(0.5)
        if Settings.is_sent_to_file_receiver:
            itchat.send_msg('你女朋友把你从黑名单里拔出来了！你快去哄她！', toUserName='filehelper')
            time.sleep(0.5)
            itchat.send_msg('你快去哄她！', toUserName='filehelper')
            time.sleep(0.5)

    def reply_from_list(self):
        first = 0
        last = len(Settings.auto_reply_content) - 1
        if Settings.auto_reply_way_choose == 0:
            while True:
                yield Settings.auto_reply_content[random.randint(first, last)]
        elif Settings.auto_reply_way_choose == 1:
            for each_reply in Settings.auto_reply_content:
                yield each_reply
        elif Settings.auto_reply_way_choose == 2:
            index = first
            while True:
                index = first if index == last else index + 1
                yield Settings.auto_reply_content[index]

    def reply_process(self):
        if Settings.is_auto_reply:
            reply_generator = self.reply_from_list()
            while True:
                if ProgramStatus.receive_flag:
                    try:
                        reply_msg = next(reply_generator)
                    except StopIteration:
                        self.programSignal.exit_signal.emit()
                        return
                    print("间隔：", len(reply_msg) * 0.5)
                    time.sleep(len(reply_msg) * 0.5)
                    itchat.send_msg(reply_msg, ProgramStatus.gf_username)
                    self.programSignal.send_auto_reply.emit(reply_msg)
                    ProgramStatus.receive_flag = False
        else:
            self.programSignal.exit_signal.emit()

    def run(self):
        global is_black
        self.check_process()
        self.inform_process()
        self.reply_process()

    def __init__(self, programSignal):
        super().__init__()
        self.programSignal = programSignal
