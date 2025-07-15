from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import os
os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"  # 启用高DPI适配
from PyQt5.QtWidgets import QApplication
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
import sys
from GUI import how_to_choose
import choose_data_save_logic

#CDSL = choose_data_save_logic.click_success()
app = QApplication(sys.argv)
window = QWidget()
form = how_to_choose.Ui_Form()
form.setupUi(window)
#CDSL.show_how_to_choose.connect(window.show())
window.show()
sys.exit(app.exec_())