from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QWidget, QDialog

import sys


import GUI.login
import GUI.login_register


class LoginWindow(QWidget):


    def __init__(self):

        super().__init__()
        self.ui = GUI.login.Ui_Form()
        self.ui.setupUi(self)
        self.reg_win=None
        self.ui.pushButton.setDefault(True)
        self.ui.username.setFocus()
        self.ui.pushButton_2.clicked.connect(self.open_reg_win)
        self.ui.pushButton.clicked.connect(self.login_button_click)
        #self.win.show()

    def login_button_click(self):
        username = self.ui.username.text()
        password = self.ui.password.text()
        if not username:
            QtWidgets.QMessageBox.critical(win, '登录失败', '用户名不能为空', QtWidgets.QMessageBox.Close)
            return
        import Core.Users.user_service
        import Core.FileIO.Read.read_user_info
        login_user_id=0x000
        login_user=Core.Users.user_actives.UserService('l', hex(login_user_id))
        login_user_id=hex(login_user_id+1)
        login_user_return=login_user.usrl(username,password)
        if login_user_return=='UNC':
            QtWidgets.QMessageBox.critical(None, '登录失败', '用户不存在，请先点击“注册”以创建用户！', QtWidgets.QMessageBox.Close)
        if login_user_return=='PNR':
            QtWidgets.QMessageBox.critical(None, '登录失败', '密码不正确，请重新输入密码！', QtWidgets.QMessageBox.Close)
        if login_user_return=='LUS':
            win.close()
            QtWidgets.QMessageBox.information(None, '登录成功',
                                              f'成功登录了{"管理员" if Core.FileIO.Read.read_user_info.admin_user else "普通"}用户“{username}”',
                                              QtWidgets.QMessageBox.Ok)

    def open_reg_win(self):
        #import login_logic
        #if self.reg_win==None:
        self.reg_win = RegisterWindow(parent=self)

        #reg_win=GUI.login_register.Ui_Form()
        #reg_win.setupUi(win)
        #win.show()
        #app.exec_()
        self.reg_win.show()

    def close_reg_win(self):
        self.reg_win.close()



class RegisterWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.reg_ui=GUI.login_register.Ui_Form()
        self.reg_ui.setupUi(self)
        #self.btn_close.clicked.connect(self.close)
        self.reg_ui.pushButton.setDefault(True)
        self.reg_ui.username.setFocus()
        self.reg_ui.pushButton.clicked.connect(self.register_button_click)

    def register_button_click(self):
        # reg_win=RegisterWindow
        create_user_id: int=0x000
        reg_username=self.reg_ui.username.text()
        reg_password=self.reg_ui.password.text()
        reg_re_password=self.reg_ui.re_password.text()
        #while True:
        #print(reg_username,reg_password,reg_re_password)
        if not reg_username:
            QtWidgets.QMessageBox.critical(None, '注册失败', '用户名不能为空', QtWidgets.QMessageBox.Close)
            return
        if reg_password!=reg_re_password:
            QtWidgets.QMessageBox.critical(None, '注册失败', '密码与重复密码不相同', QtWidgets.QMessageBox.Close)
            return
        import Core.Users.user_service
        create_user= Core.Users.user_actives.UserService('r', hex(create_user_id))
        create_user_return=create_user.usrr(reg_username,reg_password)
        #print(create_user_return)

        if create_user_return=='PTS':
            QtWidgets.QMessageBox.critical(None, '注册失败', '密码太短', QtWidgets.QMessageBox.Close)
        if create_user_return=='UCU':
            QtWidgets.QMessageBox.critical(None, '注册失败', '用户名中存在不被支持的字符', QtWidgets.QMessageBox.Close)
        if create_user_return=='UCP':
            QtWidgets.QMessageBox.critical(None, '注册失败', f'密码中存在不被支持的字符，被支持的字符有：{Core.FileIO.Write.write_user_info.WriteUserInfo.support_password_char}\n（字母大小写都可以）', QtWidgets.QMessageBox.Close)
        if create_user_return == 'EUE':
            QtWidgets.QMessageBox.critical(None, '注册失败', '用户已经存在', QtWidgets.QMessageBox.Close)
        if create_user_return=='AOK':
            win.close_reg_win()
            QtWidgets.QMessageBox.information(None,'注册成功',f'成功注册了用户“{reg_username}”',QtWidgets.QMessageBox.Ok)
        create_user_id=hex((create_user_id+1))
app=QtWidgets.QApplication(sys.argv)
win=LoginWindow()
#ui=GUI.login.Ui_Form()
#ui=GUI.login.Ui_Form()
#ui.setupUi(win)
win.show()

sys.exit(app.exec_())