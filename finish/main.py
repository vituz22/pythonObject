import random
#dssdbs

class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = random.randint(10, 100)

    def __str__(self):
        return f'Я - {self.name}\nСытость: {self.fullness}'

    def eat(self):
        if self.house.food >= 10:
            print(f'{self.name} поел')
            self.fullness += 10
            self.house.food -= 10
        else:
            print(f'У {self.name} нет еды')

    def work(self):
        print(f'{self.name} сходил на работу')
        self.house.money += 50
        self.fullness -= 10

    def play_dota(self):
        print(f'{self.name} играл в доту целый день')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            print(f'{self.name} сходил в магазин за едой')
            self.house.money -= 50
            self.house.food += 50
        else:
            print(f'У {self.name} нет денег. Деньги кончились')

    def zaseletsay(self, house):
        self.house = house
        self.fullness -= 10
        print(f"{self.name} заехал в дом ")


    def act(self):
        if self.fullness <= 0:
            print(f"{self.name} умер...")
            return
        dice = random.randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play_dota()
class House:
    def __init__(self):
        self.food = random.randint(10, 100)
        self.money = random.randint(0, 0)
    def __str__(self):
        return f'Еды - {self.food}\n Денег: {self.money}'


my_home = House()

vasya = Man(name='Вася')
petya = Man(name='Петя')

vasya.zaseletsay(house=my_home)
petya.zaseletsay(house=my_home)

vasya.play_dota()
for day in range(1, 366):
    print(f'=============== день {day} ================')
    vasya.act()
    petya.act()
    print("-----------конец дня ---------------")
    print(petya)
    print(vasya)
    print(my_home)


