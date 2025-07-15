import os,sys,shutil
import Core.FileIO.Read.read_user_info
class Root(object):
    def __init__(self,todo:str,active_id:int):
        self.todo=todo
        self.active_id=active_id

    def __user_login(self,login_username:str,login_user_password:str)->str:
        if self.todo!='l':
            return 'EUT'  #ERROR:UNKNOWN TDO
        check_have_user_id=0x000
        login_successfully=[None,None]
        check_have_user=Core.FileIO.Read.read_user_info.ReadUserInfo('c', hex(check_have_user_id))
        check_have_user_id=hex(check_have_user_id+1)
        check_have_user_return=check_have_user.usre(login_username)
        if check_have_user_return[0]=='UWC':
            username_location=check_have_user_return[1]
            login_successfully[0]=True
        if check_have_user_return=='UNC':
            return 'UNC'  #USER WAS NOT CREATED
        check_user_password_id=0x000
        check_user_password=Core.FileIO.Read.read_user_info.ReadUserInfo('p', hex(check_user_password_id))
        check_user_password_return=check_user_password.rusp(login_user_password,username_location)
        if check_user_password_return=='PWR':
            login_successfully[1]=True
        if check_user_password_return=='PNR':
            return 'PNR'  #PASSWORD WAS NOT REAL
        return 'LUS'  # LOGIN USER SUCCESSFULLY
    def usrl(self,login_username:str,login_user_password:str)->str:
        return self.__user_login(login_username,login_user_password)