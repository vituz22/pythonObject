# С помощью классов и объектов создать модель человека
# который должен прожить N дней

#sadgasdg

class Man:
    def __init__(self, name):
        self.name = name
        self.money = 0
        self.food = 20
        self.fullness = 20

    def eat(self):
        if self.food >= 10:
            print(f"{self.name} поел")
            self.fullness += 10
            self.food -= 10
        else:
            print(f"У {self.name} нет еды")

    def play_dota(self):
        print(f"{self.name} весь день играл в доту")
        self.fullness -= 20

vasya = Man(name="Вася")
vasya.eat()