class Character:
    def __init__(self, *, level: int):
        self.level = level  # to add attribute to an instance
        self.heath = self.base_health * level
        self.power = self.base_power * level

    def attack(self, *, target: "Character"):  # with kovichka
        print(f'{self.name} attacks with {self.power} power!')
        target.heath -= self.power

    def __str__(self):
        return f'{self.name}: level {self.level} with {self.heath} health and {self.power} power.'

    def is_alive(self):
        return self.heath > 0


class Ork(Character):  # extending the base class
    base_health = 120
    base_power = 20
    name = "Ork"


class Elf(Character):
    base_health = 60
    base_power = 30
    name = "Elf"


my_ork = Ork(level=3)
my_elf = Elf(level=4)
print(type(my_ork))
print(my_ork.level)
print(my_ork)
print(my_elf)


# FIGHT!
def brutal_fight(*, char_1: Character, char_2: Character) -> None:
    while char_1.is_alive() and char_2.is_alive():
        char_1.attack(target=char_2)
        if char_2.is_alive():
            char_2.attack(target=char_1)

    print(f"Char1: {char_1}, is_alive: {char_1.is_alive()}")
    print(f"Char2: {char_2}, is_alive: {char_2.is_alive()}")


brutal_fight(char_1=my_ork, char_2=my_elf)

