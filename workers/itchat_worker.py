from PyQt5.QtCore import QThread
import sys
import time
from pass_message.settings import *
from pass_message.program_status import ProgramStatus
import itchat
from itchat.content import *


class itchat_worker(QThread):

    def output_info(self, msg):
        print('[INFO] %s' % msg)

    def open_QR(self):
        for get_count in range(10):
            self.output_info('Getting uuid')
            uuid = itchat.get_QRuuid()
            while uuid is None:
                uuid = itchat.get_QRuuid()
                time.sleep(1)
            self.output_info('Getting QR Code')
            if itchat.get_QR(uuid):
                break
            elif get_count >= 9:
                self.output_info('Failed to get QR Code, please restart the program')
                sys.exit()
        self.output_info('Please scan the QR Code')
        return uuid

    def login_process(self):
        uuid = self.open_QR()
        waitForConfirm = False
        while 1:
            status = itchat.check_login(uuid)
            if status == '200':
                break
            elif status == '201':
                if waitForConfirm:
                    self.output_info('Please press confirm')
                    waitForConfirm = True
            elif status == '408':
                self.output_info('Reloading QR Code')
                uuid = self.open_QR()
                waitForConfirm = False
        userInfo = itchat.web_init()
        itchat.show_mobile_login()
        itchat.start_receiving()
        itchat.get_friends(True)
        print('Login successfully as %s' % userInfo['User']['NickName'])
        name = itchat.search_friends(name=Settings.bf_name)[0]['UserName']
        ProgramStatus.my_own_username = userInfo['User']['UserName']
        if name:
            ProgramStatus.gf_username = name
        else:
            self.programSignal.err_no_girlfriend.emit()
            return
        self.programSignal.login_success_signal.emit()

    def run(self):
        self.login_process()
        itchat.run()

    def __init__(self, programSignal):
        super().__init__()
        self.programSignal = programSignal
        # itchat.programSignal = programSignal

    # Start auto-replying

    @itchat.msg_register([TEXT, NOTE])
    def simple_reply(self, msg):
        print(msg)
        msg_name = msg['User']['RemarkName'] if msg['User']['RemarkName'] != '' else msg['User']['NickName']
        if ProgramStatus.is_black:
            if msg_name == Settings.bf_name:
                ProgramStatus.test_message_reply += 1
                ProgramStatus.is_black = msg['Type'] == 'Note' and msg['Text'] == '消息已发出，但被对方拒收了。'
                if not ProgramStatus.is_black:
                    self.programSignal.removed_already.emit()
                    pass
        if not ProgramStatus.is_black:
            # 她主动给你发消息了！
            if msg['FromUserName'] == ProgramStatus.gf_username:
                ProgramStatus.receive_flag = True
            # 她把你拉出黑名单后，你回来了
            if msg['FromUserName'] == ProgramStatus.my_own_username and msg['ToUserName'] == ProgramStatus.gf_username:
                self.programSignal.you_are_back.emit()
                ProgramStatus.is_you_back = True
