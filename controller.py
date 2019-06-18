import sys
from PyQt5.QtCore import *
from workers.detector_controller import detector_controller
from PyQt5.QtWidgets import *
from pass_message.signals import ProgramSignals
from pass_message.program_status import ProgramStatus
from pass_message.settings import Settings
import itchat
from itchat.content import *





app = QApplication(sys.argv)
p = ProgramSignals()
demo = detector_controller(p)
sys.exit(app.exec_())
