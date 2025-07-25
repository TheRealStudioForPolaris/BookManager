import os,sys,shutil


import Core.FileIO.Read.read_user_info
class WriteUserInfo(object):
    """包含了创建用户的逻辑"""
    support_password_char = 'abcdefghijklmnopqrstuvwxyz1234567890_!+=-\\,.@$%^&*/?<>{}[]|`~#()'
    unsupport_username_char=['\n','\t','\r','|'*10]
    def __init__(self,todo:str,active_id:int):
        """初始化方法"""
        self.todo=todo
        self.active_id=active_id

    #@classmethod
    def __create_user(self,username:str,password:str)->str:
        """用于创建用户
        username：字符串，用户名
        password：字符串，密码
        返回字符串"""
        if self.todo!='c':
            return 'EUT'  #ERROR:UNKOWN TDO
        check_username_exist_id=0x000
        self.__true_password=password
        self.username=username
        for i in self.unsupport_username_char:
            if i in self.username:
                return 'UCU'  # UNSUPPORTED CHARACTER IN USERNAME
        self.__program_path = os.path.abspath('../')
        self.__file_save_path = os.path.join(self.__program_path, 'data/File/UserData')
        if not os.path.exists(self.__file_save_path):
            os.mkdir(self.__file_save_path,mode=0o777)
        check_username_exist=Core.FileIO.Read.read_user_info.ReadUserInfo('c', hex(check_username_exist_id))
        check_username_exist_id = hex(check_username_exist_id + 1)
        check_username_exist_return=check_username_exist.usre(username)
        if check_username_exist_return=='EUE':
            return 'EUC' #ERROR:USER WAS CREATED
        if len(self.__true_password)<5:
            return 'PTS'  #PASSWORD IS TOO SHORT
        # if len(self.__true_password)>30:
        #     return 'PTL'  #PASSWORD IS TOO LONG

        for i in self.__true_password:
            if not i in self.support_password_char and not i in self.support_password_char.upper():
                return 'UCP' #UNSUPPORTED CHARACTER IN PASSWORD
        user_created=[None,None]
        self.__username_path=os.path.join(self.__file_save_path,r'.usrname.bookmanager')
        with open(self.__username_path,'a+',errors='ignore') as username_file:
            username_file.seek(0)
            file_old=username_file.read()
            username_file.seek(0,1)
            username_file.write(f'{username}{'|'*10}Normal\n')
            username_file.seek(0)
            file_new=username_file.read()
            self.username_file_list=username_file.readlines()
            if file_new==f'{file_old}{username} Normal\n':
                user_created[0]=True
            else:
                self.__remove_last_username_writing()
                return 'EUW'  # ERROR FROM USERNAME WRITING


        self.__password_path=os.path.join(self.__file_save_path,r'.Password.bookmanager')
        with open(self.__password_path,'a+',errors='ignore') as password_file:
            password_file.seek(0)
            self.__file_old = password_file.read()
            password_file.seek(0, 1)
            password_file.write(f'{self.__true_password}\n')
            password_file.seek(0)
            self.__file_new = password_file.read()
            self.__password_file_list = password_file.readlines()
            if self.__file_new == f'{self.__file_old}{self.__true_password}\n':
                user_created[1] = True
            else:
                self.__remove_last_password_writing()
                return 'EPW'  # ERROR FROM PASSWORD WRITING
            return 'AOK'  # ALL ACTIVES ARE OKAY



        # if user_created[0]==True:
        #     if user_created[1]==True:
        #
        #     else:
        #
        # else:
        #     if user_created[1]==True:
        #
        #     else:
        #         self.__remove_last_username_writing()
        #         self.__remove_last_password_writing()
        #         return 'E2A' #ERROR FROM ALL ACTIVES


    def usrc(self,username:str,password:str)-> str:
        #obj = Root('c',0x000)
        return self.__create_user(username,password)

    def __remove_last_password_writing(self):
        for i in self.__password_file_list:
            if self.__true_password == i:
                with open(self.__password_path, 'w', errors='ignore') as password_file:
                    password_file.write(self.__password_file_list[0, -2])

    def __remove_last_username_writing(self):
        for i in self.username_file_list:
            if self.username == i:
                with open(self.__username_path, 'w', errors='ignore') as username_file:
                    username_file.write(self.username_file_list[0, -2])
