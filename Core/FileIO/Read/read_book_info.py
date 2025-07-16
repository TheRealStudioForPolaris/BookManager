import os,sys,shutil
import re
class ReadBookInfo(object):
    def __init__(self,todo:str,active_id:int):
        self.todo=todo
        self.active_id=active_id

    def __check_book_exist(self,name:str|None=None,isbn:str|None=None)->str:
        if self.active_id!='c':
            return 'EUT'  #ERROR:UNKNOWN TDO
        self.name=name
        self.isbn=isbn
        if not (self.name and self.isbn):
            return 'EUG'   #ERROR:UNKNOWN GOAL
        book_exist=[None,None]
        self.__book_file_path=os.path.abspath('../data/File/BooksData')
        if self.name:
            with open(os.path.join(self.__book_file_path,'.name.bookmanager'),'r',errors='ignore') as name_file:
                self.__name_list=name_file.readlines()
                for i in self.__name_list:
                    if f'{self.name}\n'==i:
                        book_exist[0]=True
                    else:
                        book_exist[0]=False

        if self.isbn:
            with open(os.path.join(self.__book_file_path, '.isbn.bookmanager'), 'r', errors='ignore') as isbn_file:
                self.__isbn_list=isbn_file.readlines()
                for i in self.__isbn_list:
                    if f'{self.isbn}\n'==i:
                        book_exist[1]=True
                    else:
                        book_exist[1]=False


        if book_exist[1]:
            return 'BWC'  #BOOK WAS CREATED
        else:
            if book_exist[0]:
                return 'BMC'    #BOOK MAY BE CREATED
            return 'BNC'  #BOOK WAS NOT CREATED
    def cbke(self,name:str|None=None,isbn:str|None=None)->str:
        return self.__check_book_exist(name,isbn)


    def __get_book_info(self,name:str|None=None,isbn:str|None=None)->str|tuple:
        if self.todo!='g':
            return 'EUT'  #ERROR:UNKNOWN TDO
        self.name=name
        self.isbn=isbn
        if not (self.name and self.isbn):
            return 'EUG'   #ERROR:UNKNOWN GOAL
        filename_tuple = ('name', 'price', 'writer', 'press', 'publish_time', 'isbn', 'intro')
        self.__book_location=0
        return_list=[]
        if self.name:
            for i in self.__name_list:
                if f'{self.name}\n'==i:
                    break
                self.__book_location+=1
            for i in filename_tuple:
                with open(os.path.join(self.__book_file_path,i),'r',errors='ignore') as file:
                    file_list=file.readlines()
                    return_list.append(re.sub('/n','\n',str(file_list[self.__book_location])))

        elif self.isbn:
            for i in self.__isbn_list:
                if f'{self.isbn}\n'==i:
                    break
                self.__book_location+=1
            for i in filename_tuple:
                with open(os.path.join(self.__book_file_path,i),'r',errors='ignore') as file:
                    file_list=file.readlines()
                    return_list.append(re.sub('/n','\n',str(file_list[self.__book_location])))

        if len(return_list) != len(file_list):
            return 'NOK'  #NOT OKAY
        return 'AOK',return_list  #ALL ACTIVES ARE OKAY
    def gboi(self,name:str|None=None,isbn:str|None=None)->str|tuple:
        return self.__get_book_info(name,isbn)