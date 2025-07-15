from PyQt5 import QtCore, QtGui, QtWidgets
import os

from PyQt5.QtCore import Qt

os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"  # 启用高DPI适配
from PyQt5.QtWidgets import QApplication
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
from PyQt5.QtWidgets import *
import sys
from GUI import choose_mysql


app = QApplication(sys.argv)
window=QWidget()
form=choose_mysql.Ui_Form()
form.setupUi(window)
window.show()
sys.exit(app.exec_())