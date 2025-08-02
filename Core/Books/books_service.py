import os,sys,shutil
import datetime
import Core.FileIO.Write.write_book_info
import Core.FileIO.Read.read_book_info
class BooksService(object):
    def __init__(self,todo:tuple,active_id:int):
        self.todo=todo
        self.active_id=active_id

    def __new_book(self,
                   name: str,
                   price: int | float,
                   writer: str,
                   press: str,
                   publish_time: datetime.date,
                   isbn: int,
                   intro: str,
                   icons_path:str|None=None
                   )->str|tuple:
        if self.todo[0]!='n':
            return 'EUT'  #ERROR:UNKNOWN TDO
        self.name = name
        self.price = price
        self.writer = writer
        self.press = press
        self.publish_time = publish_time
        self.isbn = isbn
        self.intro = intro
        self.icons_path=icons_path
        import Core.FileIO.Write.write_book_info
        if self.todo[1]=='f':
            book_creator=Core.FileIO.Write.write_book_info.WriteBookInfo('c',self.active_id)
            book_creator_return=book_creator.bokc(self.name,self.price,self.writer,self.press,self.publish_time,self.isbn,self.intro)
            if book_creator_return=='BWC':
                return 'BWC' #BOOK WAS CREATED
            if book_creator_return[0]=='EFW':
                return 'EFW',book_creator_return[1]  # ERROR FROM FILE WRITING
            return 'AOK'
        elif self.todo[1]=='s':
            return 'EUT'  #ERROR UNSUPPORTED TDO
        else:
            return 'EUT'  # ERROR UNSUPPORTED TDO
    def nbok(self,
                   name: str,
                   price: int | float,
                   writer: str,
                   press: str,
                   publish_time: datetime.date,
                   isbn: int,
                   intro: str,
                   icons_path:str|None=None
                   )->str|tuple:
        return self.__new_book(name,price,writer,press,publish_time,isbn,intro,icons_path)

    def __search_book_info(self,name:str|None=None,isbn:str|None=None)->str|tuple:
        if self.todo[0]!='s':
            return 'EUT'  #ERROR UNKNOWN TDO
        self.name=name
        self.isbn=isbn
        if not (self.name and self.isbn):
            return 'EUG'   #ERROR:UNKNOWN GOAL
        import Core.FileIO.Read.read_book_info
        if self.todo[1]=='f':
            check_book_exist=Core.FileIO.Read.read_book_info.ReadBookInfo('c',self.active_id)
            get_book_info=Core.FileIO.Read.read_book_info.ReadBookInfo('g',self.active_id)
            if self.name:
                check_book_exist_return = check_book_exist.cbke(self.name)
                if check_book_exist_return=='BNC':
                    return 'BNC'  #BOOK WAS NOT CREATED
                get_book_info_return=get_book_info.gboi(self.name)
                if get_book_info_return=='NOK':
                    return 'NOK'   #NOT OKAY
            elif self.isbn:
                check_book_exist_return=check_book_exist.cbke(isbn=self.isbn)
                if check_book_exist_return=='BNC':
                    return 'BNC'  #BOOK WAS NOT CREATED
                get_book_info_return=get_book_info.gboi(isbn=self.isbn)
                if get_book_info_return=='NOK':
                    return 'NOK'   #NOT OKAY
            return 'AOK',get_book_info_return[1]
        elif self.todo[1] == 's':
            return 'EUT'  # ERROR UNSUPPORTED TDO
        else:
            return 'EUT'  # ERROR UNSUPPORTED TDO
    def sboi(self,name:str|None=None,isbn:str|None=None)->str|tuple:
        return self.__search_book_info(name,isbn)