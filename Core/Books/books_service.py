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
