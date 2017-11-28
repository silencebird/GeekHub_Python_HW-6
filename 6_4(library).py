import json

class Books:
    def __init__(self, id, author, title, subject, date_of_publication, ISBN):
        self.id = id
        self.author = author
        self.title = title
        self.subject = subject
        self.date_of_publication = date_of_publication
        self.ISBN = ISBN


class Staff:
    def __init__(self, first_name, last_name, position, responsibility, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.responsibility = responsibility
        self.phone_number = phone_number

    def newStaff(self,first_name, last_name, position, responsibility, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.responsibility = responsibility
        self.phone_number = phone_number



class Library:
    def __init__(self, timing, staff={},  catalog={}):
        self.staff = staff
        self.timing = timing
        self.catalog = catalog

    def getNewStaff(self, newstaff):
        self.staff.update({'%s  %s' % (newstaff.first_name, newstaff.last_name) : newstaff.__dict__})

    def getNewBook(self, newbook):
        self.catalog.update({'%s:%s' %(newbook.author,newbook.title) : newbook.__dict__})



library = Library("8:00 - 18:00")

library.getNewStaff(Staff('Vasya', 'Pupkin', 'director', 'all library', '000XXX000XX'))
library.getNewStaff(Staff('Petya', 'Pupkin', 'de-director', 'all library', 'X00XXX0X0XX'))
library.getNewStaff(Staff('Vasya', 'Ivanov', 'librarian', 'all library', 'X00XXX0X0XX'))
library.getNewStaff(Staff('Vasya', 'Petrov', 'librarian', 'all library', 'X00XXX0X0XX'))
library.getNewStaff(Staff('Vasya', 'Sidorov', 'librarian', 'all library', 'X00XXX0X0XX'))
library.getNewStaff(Staff('Abram', 'Friman', 'accountant', 'all library', 'X00XXX0X0XX'))
library.getNewStaff(Staff('Petya', 'Ivanov', 'cleaner', 'right side of library', 'X00XXX0X0XX'))
library.getNewStaff(Staff('Petya', 'Sidorov', 'cleaner', 'left side of library', 'X00XXX0X0XX'))
library.getNewBook(Books(1,
                         "Arif Abdul Majid",
                         "Political structure in a changing Pakistani",
                         "politology",
                         1985,
                         "969-8612-02-5"))
library.getNewBook(Books(2,
                         "Paul Kalanithi",
                         "When Breath Becomes Air",
                         "neurosurgeon ",
                         2016,
                         "969-8612-02-5"))
library.getNewBook(Books(3,
                         "Yuval Noah Harari",
                         "Sapiens: A Brief History of Humankind",
                         "history",
                         2015,
                         "969-8612-02-5"))
library.getNewBook(Books(4,
                         "Jon Krakauer",
                         "Into Thin Air: A Personal Account of the Mt. Everest Disaster",
                         "Biographies & Memoirs",
                         1999,
                         "969-8612-02-5"))
library.getNewBook(Books(5,
                         "Richard P. Feynman",
                         "Surely You're Joking, Mr. Feynman!",
                         "Biographies & Memoirs",
                         1997,
                         "969-8612-02-5"))
library.getNewBook(Books(6,
                         "Epictetus",
                         "Manual for Living",
                         "Religion & Spirituality",
                         1994,
                         "969-8612-02-5"))
library.getNewBook(Books(7,
                         "Robert Cialdini",
                         "Influence: The Psychology of Persuasion",
                         "The Psychology of Persuasion",
                         1997,
                         "969-8612-02-5"))
library.getNewBook(Books(8,
                         "Marcus Aurelius",
                         "Meditations",
                         "Biographies & Memoirs",
                         1995,
                         "969-8612-02-5"))
library.getNewBook(Books(9,
                         "Stephen Hawking",
                         "A Brief History of Time",
                         "Science & Math",
                         1998,
                         "969-8612-02-5"))
library.getNewBook(Books(10,
                         "Steven Pressfield",
                         "The War of Art: Break Through Your Blocks and Win Your Inner Creative Battles",
                         "Health, Fitness & Dieting",
                         2012,
                         "969-8612-02-5"))

print(json.dumps(library.__dict__, sort_keys=True,  indent=4, separators=(',', ': ')))