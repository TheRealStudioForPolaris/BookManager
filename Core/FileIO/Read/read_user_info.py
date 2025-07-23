import os,sys,shutil
admin_user=False
class ReadUserInfo(object):
    def __init__(self,todo:str,active_id:int):
        self.todo=todo
        self.active_id=active_id

    def __check_user_exist(self,
                           check_username:str,
                           user_file_path:str='../data/File/UserData/.usrname.bookmanager')->str|tuple:
        if self.todo!='c':
            return 'EUT'  #ERROR:UNKNOWN TDO
        self.__username_file_path=os.path.abspath(user_file_path)
        username_file=open(self.__username_file_path,'a',errors='ignore')
        username_file.close()
        with open(self.__username_file_path,'r',errors='ignore') as username_file:
            all_usernames=username_file.readlines()
            # global username_list_location
            username_list_location=0
            for i in all_usernames:
                username_permission_list=i.split()
                if f'{check_username}' == username_permission_list[0]:
                    if username_permission_list[1]=='Admin':
                        global admin_user
                        admin_user=True
                    return 'UWC',username_list_location #USER WAS CREATED
                username_list_location += 1
            else:
                return 'UNC' #USER WAS NOT CREATED
    def usre(self,
             check_username:str,
             user_file_path:str='../data/File/UserData/.usrname.bookmanager')->str:
        return self.__check_user_exist(check_username,user_file_path)


    def __read_user_password(self,
                             password:str,
                             password_location:int,
                             password_file_path:str='../data/File/UserData/.Password.bookmanager')->str:
        if self.todo!='p':
            return 'EUT'  #ERROR:UNKNOWN TDO
        self.__password_will_check=f'{password}\n'
        self.__password_file_path=os.path.abspath(password_file_path)
        password_file=open(self.__password_file_path,'a')
        password_file.close()
        with open(self.__password_file_path,'r',errors='ignore') as password_file:
            all_passwords=password_file.readlines()
            # global username_list_location
            if all_passwords[password_location]==self.__password_will_check:
                return 'PWR'  # PASSWORD WAS REAL
            else:
                return 'PNR'   #PASSWORD WAS NOT REAL

    def rusp(self,
             password:str,
             password_location:int,
             password_file_path:str='../data/File/UserData/.Password.bookmanager')->str|tuple:
        # global username_list_location
        # username_list_location=0
        return self.__read_user_password(password,password_location,password_file_path)

