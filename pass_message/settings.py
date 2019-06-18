class Settings:
    bf_name = "宝宝"
    bf_sentence = "宝宝我爱你"
    check_internal = 5
    is_jump_out = True
    is_sent_to_file_receiver = False
    is_inform_brothers = False
    brothers_list = []
    send_to_brother_message = ""
    is_auto_reply = False
    # auto_reply_way = ["random", "order_once", "order_forever"]
    auto_reply_way_choose = 0
    auto_reply_content = []
    is_close_after_inform = True
    is_stop_by_filereceiver = False

    @classmethod
    def message(cls):
        sb = "名字：" + Settings.bf_name + "\n"
        sb += "句子：" + Settings.bf_sentence + "\n"
        sb += "时间间隔：" + str(cls.check_internal) + "\n"
        sb += "是否弹窗：" + str(cls.is_jump_out) + "\n"
        sb += "通知给文件传输助手：" + str(cls.is_sent_to_file_receiver) + "\n"
        sb += "通知兄弟：" + str(cls.is_sent_to_file_receiver) + "\n"
        sb += "兄弟列表：" + str(cls.brothers_list) + "\n"
        sb += "是否自动回复：" + str(cls.is_auto_reply) + "\n"
        sb += "回复内容：" + str(cls.auto_reply_content) + "\n"
        sb += "通知结束后关闭：" + str(cls.is_close_after_inform) + "\n"
        sb += "传输助手关闭：" + str(cls.is_stop_by_filereceiver) + "\n"
        return sb
