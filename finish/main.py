import random


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.food = 10
        self.money = 0

    def __str__(self):
        return f'Я - {self.name}\nСытость: {self.fullness}\nЕды: {self.food}\nДенег: {self.money}'

    def eat(self):
        if self.food >= 10:
            print(f'{self.name} поел')
            self.fullness += 10
            self.food -= 10
        else:
            print(f'У {self.name} нет еды')

    def work(self):
        print(f'{self.name} сходил на работу')
        self.money += 50
        self.fullness -= 10

    def play_dota(self):
        print(f'{self.name} играл в доту целый день')
        self.fullness -= 10

    def shopping(self):
        if self.money >= 50:
            print(f'{self.name} сходил в магазин за едой')
            self.money -= 50
            self.food += 50
        else:
            print(f'У {self.name} нет денег. Деньги кончились')

    def act(self):
        if self.fullness <= 0:
            print(f"{self.name} умер...")
            return
        dice = random.randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.food < 10:
            self.shopping()
        elif self.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play_dota()


man = Man(name='Вася')
for day in range(1, 21):
    print(f'=============== день {day} ================')
    man.act()
    print(man)