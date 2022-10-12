# coding: utf-8
# Ahian


class Book:
    def __init__(self,__code,__title):
        self.__code = __code
        self.__title = __title
        self.__status = True

    def get_book_title(self):
        return self.__title

    def get_book_code(self):
        return self.__code

    def is_available(self):
        return self.__status

    def borrow_book(self):
        self.__status = False

    def return_book(self):
        self.__status = True

    def __str__(self):
        if self.__status == True:
            return "{}, {} (Available)".format(self.__title,self.__code)
        else:
            return "{}, {} (On Loan)".format(self.__title,self.__code)

class Member:


    def __init__(self,__member_id,__name):
        self.__member_id = __member_id
        self.__name = __name
        self.__on_loan_books_list = []

    def get_name(self):
        return self.__name

    def get_member_id(self):
        return self.__member_id

    def get_on_loan_books(self):
        return self.__on_loan_books_list

    def borrow_book(self, book):
        self.__on_loan_books_list.append(book.get_book_title())

    def return_book(self, book):
        self.__on_loan_books_list.remove(book.get_book_title())

    def __str__(self):
        result1 = "{}\nOn loan book(s):\n".format(self.__name)
        result2 = ""
        if len(self.__on_loan_books_list) == 0:
            return result1 + '-'
        else:
            for i in self.__on_loan_books_list:
                result2 = result2 + i+"\n"
            result2 = result2[:-1]
            result = result1 + result2
            return result

class Record:
    def __init__(self,__book,__member,__issue_date):
        self.__book = __book
        self.__member = __member
        self.__issue_date = __issue_date
        self.__book.borrow_book()
        self.__member.borrow_book(self.__book)
        self.__is_on_loan = self.__book.is_available()

    def get_member_id(self):
        return self.__member.get_member_id()

    def get_book_code(self):
        return self.__book.get_book_code()

    def get_issue_date(self):
        return self.__issue_date

    def is_on_loan(self):
        if self.__book.is_available() == True:
            return False
        else:
            return True

    def return_book(self):
        self.__book.return_book()
        self.__member.return_book(self.__book)

    def __str__(self):
        if self.__book.is_available() == True:
            status = 'Available'
        else:
            status = 'On Loan'
        return '{}, {}, {} ({}), issued date={}'.format(self.__member.get_name(),self.__book.get_book_title(),self.__book.get_book_code(),status,self.__issue_date)


