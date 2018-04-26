class Person:
    def __init__(self, initialAge):

        # se age < 0
        # print Age is not valid, setting age to 0.
        # e seta nova age = 0
        if initialAge < 0:
            print('Age is not valid, setting age to 0.')
            self._age = 0
        # se > 0 age = initialAge
        else:
            self._age = initialAge

    def amIOld(self):
        # classificacao
        if self._age < 13:
            print('You are young.')
        elif 12 < self._age < 18:
            print('You are a teenager.')
        elif self._age >= 18:
            print('You are old.')

    def yearPasses(self):
        # idade + 1
        self._age = self._age + 1

t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")