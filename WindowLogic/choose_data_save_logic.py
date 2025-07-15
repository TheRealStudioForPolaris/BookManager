import threading

from PyQt5 import QtCore, QtGui, QtWidgets
import os

from PyQt5.QtCore import Qt, pyqtSignal, QTimer

os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"  # 启用高DPI适配
from PyQt5.QtWidgets import QApplication
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
from PyQt5.QtWidgets import *
import sys


from GUI import choose_data_save
import how_to_choose_logic
show_how_to_choose = pyqtSignal()
def click_success():


    show_how_to_choose.emit()


app = QtWidgets.QApplication(sys.argv)
window = QWidget()
form=choose_data_save.Ui_Form()
form.setupUi(window)
form.pushButton.clicked.connect(click_success)
form.radioButton.setChecked(True)
window.show()
sys.exit(app.exec_())