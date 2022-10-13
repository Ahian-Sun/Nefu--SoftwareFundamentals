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
        if book.get_book_title() not in self.__on_loan_books_list:
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

class MyLibrary:
    def __init__(self,file_name):
        self.__books_list = []
        self.__on_loan_records_list = []
        self.all_records = []
        self.data = []
        self.on_loan = []
        self.book_name = []
        self.book_id = []
        try:
            with open(file_name) as f:
                f = f.read()
                book_list = f.split('\n')
                for i in book_list:
                    a = i.split(',')
                    for j in a:
                        if j[0] == 'Q':
                            self.book_id.append(j)
                        else:
                            self.book_name.append(j)
            print("{} books loaded.".format(len(self.book_name)))
        except:
            print("ERROR: The file '{}' does not exist.".format(file_name))

    def show_all_books(self):
        for i,j in zip(self.book_name,self.book_id):
            print("{}, {} (Available)".format(i,j))

    def find_book(self, code):
        if code in self.book_id and code not in self.on_loan:
            return Book(code,self.book_name[self.book_id.index(code)])
        else:
            return None

    def borrow_book(self, book, member, issue_date):
        if book != None:
            print("{} is borrowed by {}.".format(book.get_book_title(),member.get_name()))
            self.on_loan.append(book.get_book_code())
            member.borrow_book(book)
            book.borrow_book()
            self.__books_list.append(book)
            self.data.append([book,member,issue_date])
            self.__on_loan_records_list.append(Record(book,member,issue_date))
            self.all_records.append(Record(book,member,issue_date))
        else:
            print("ERROR: could not issue the book.")

    def show_available_books(self):
        for i in self.book_id:
            if i not in self.on_loan:
                print("{}, {} (Available)".format(self.book_name[self.book_id.index(i)],i))

    def find_record(self, code):
        if code in self.on_loan:
            for i in self.data:
                if i[0].get_book_code() == code:
                    return Record(i[0],i[1],i[2])
        else:
            return None

    def return_book(self, record):
        if record != None:
            if record.get_book_code() in self.on_loan:
                record.return_book()
                self.on_loan.remove(record.get_book_code())
                for i in self.__on_loan_records_list:
                    if i.get_member_id() == record.get_member_id():
                        if i.get_book_code() == record.get_book_code():
                            if i.get_issue_date() == record.get_issue_date():
                                self.__on_loan_records_list.remove(i)
                print("{} is returned successfully.".format(record.get_book_code()))
        else:
            print("ERROR: could not return the book.")

    def show_on_loan_records(self):
        for i in self.__on_loan_records_list:
            if i != None:
                print(i)

    def show_all_records(self):
        for i in self.all_records:
            if i != None:
                print(i)

