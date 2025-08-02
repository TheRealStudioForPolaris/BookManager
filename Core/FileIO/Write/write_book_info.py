import os,sys,shutil
import datetime,re
class WriteBookInfo(object):
    def __init__(self,todo:str,active_id:int):
        self.todo=todo
        self.active_id=active_id

    def __create_book(self,
                    name:str,
                    price:int|float,
                    writer:str,
                    press:str,
                    publish_time:datetime.date,
                    isbn:int,
                    intro:str)->str|tuple:
        if self.todo!='c':
            return 'EUT'  #ERROR:UNKNOWN TDO
        self.name=name
        self.price=price
        self.writer=writer
        self.press=press
        self.publish_time=publish_time
        self.isbn=isbn
        self.intro=intro

        self.__book_file_path=os.path.abspath('../data/File/BooksData')
        book_created=[None]*8
        if not os.path.exists(self.__book_file_path):
            os.mkdir(self.__book_file_path,0o777)
        filename_tuple=('name','price','writer','press','publish_time','isbn','intro')
        files_tuple=(self.name,self.price,self.writer,self.press,self.publish_time,self.isbn,self.intro)
        book_created_num=0
        for i in filename_tuple:
            for a in files_tuple:
                if i=='isbn':
                    import Core.FileIO.Read.read_book_info
                    check_book_exist=Core.FileIO.Read.read_book_info.ReadBookInfo('c',self.active_id)
                    if 'BWC' == check_book_exist.cbke(isbn=a):
                        return 'BWC'
                final_str=re.sub(r'\n',r'/n',str(a))
                self.__file_path=os.path.join(self.__book_file_path,f'.{i}.bookmanager')
                with open(self.__file_path,'a+',errors='ignore') as file:
                    file.seek(0)
                    file_old=file.read()
                    file.seek(0,1)
                    file.write(f'{final_str}\n')
                    file.seek(0)
                    file_new=file.read()
                    if file_new==f'{file_old}{final_str}\n':
                        book_created[book_created_num]=True
                        book_created_num+=1
                    else:
                        self.__rollback(i)
                        return 'EFW',i  #ERROR FROM FILE WRITING
        return 'AOK'  #ALL ACTIVES ARE OKAY
    def bokc(self,
            name:str,
            price:int|float,
            writer:str,
            press:str,
            publish_time:datetime.date,
            isbn:int,
            intro:str)->str|tuple:
        return self.__create_book(name,price,writer,press,publish_time,isbn,intro)

    def __rollback(self, error_from:str):
        with open(os.path.join(self.__book_file_path,f'.{error_from}.bookmanager'),'w+',errors='ignore') as roolback_file:
            roolback_file.seek(0,1)
            self.__roolback_file_list=roolback_file.readlines()
            self.__final_file_list=self.__roolback_file_list[0,-1]
            roolback_file.seek(0)
            roolback_file.write(self.__final_file_list)