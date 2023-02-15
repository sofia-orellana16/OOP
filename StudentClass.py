from datetime import date
today = date.today()
year = today.year

class Student:
    
    def __init__(self, s, n, d, c):
        self.__studentid = s
        self.__name = n
        self.__dob = d
        self.__classification = c
        self.__age = 0
        self.__register = ''

    def age(self):
        dob = self.__dob.split('/')
        dob_year = int(dob[2])
        self.__age = year - dob_year
        

    def calc_register(self):
        if self.__classification == 'F':
            self.__register = 'Your registration date is from 4/10 thru 4/12'
        elif self.__classification == 'S':
            self.__register = 'Your registration date is from 4/7 thru 4/9'
        elif self.__classification == 'Jr':
            self.__register = 'Your registration date is from 4/4 thru 4/6'
        elif self.classification == 'SR':
            self.__register = 'Your registration date is from 4/1 thry 4/3'
        else:
            self.__register = 'Not found'

    def get_age(self):
        return self.__age
    
    def get_register(self):
        return self.__register
        