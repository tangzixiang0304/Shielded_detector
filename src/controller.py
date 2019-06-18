import sys
from src.workers.detector_controller import detector_controller
from PyQt5.QtWidgets import *
from src.pass_message.signals import ProgramSignals

app = QApplication(sys.argv)
p = ProgramSignals()
demo = detector_controller(p)
sys.exit(app.exec_())
