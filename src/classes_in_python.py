import datetime


class Person:
    def __init__(self, name, age=None, sex=None):
        self.name = name
        self.age = age
        self.sex = sex
    
    def getSurname(self):
        return self.name.split()[-1]

    def getBirthyear(self):
        if self.age is None:
            print("[INFO] please update {self.name}'s age")
            pass
        else:
            now = datetime.datetime.now()
            
            return now.year - self.age
    
    def setMood(self, happy=False):
        if happy:
            self.mood = 'happy'
            print(f'{self.name.split()[0]}: I have no regrets over past mistakes')
        else:
            self.mood = 'angry'
            print(f'{self.name.split()[0]}: #@*&%')
    
    def __repr__(self):
        return f'Person: {self.name}, {self.age}, {self.sex}'


class Researcher(Person):
    def __init__(self, pay=10, areas=['research'], **kwargs):
        super(Researcher, self).__init__(**kwargs)
        self.pay = pay
        self.areas = areas


def main():
    kln = Researcher(
            name='Kristoffer L. Nielbo',
            age=45,
            sex='male',
            areas=['culture analytics', 'humanities computing']
            )
    
    print(kln.getBirthyear())
    kln.setMood(happy=True)


if __name__ == '__main__':
    main()