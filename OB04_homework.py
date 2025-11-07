from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."

class MagicStaff(Weapon):
    def attack(self):
        return "Боец атакует магическим посохом."

class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def change_weapon(self, new_weapon: Weapon):
        self.weapon = new_weapon

    def attack(self):
        return self.weapon.attack()

class Monster:
    def __init__(self, name="Монстр"):
        self.name = name
        self.is_alive = True

    def die(self):
        self.is_alive = False
        return f"{self.name} побежден!"

def battle(fighter: Fighter, monster: Monster):
    print(fighter.attack())
    print(monster.die())

if __name__ == "__main__":
    sword = Sword()
    bow = Bow()
    staff = MagicStaff()

    fighter = Fighter(sword)
    monster = Monster()

    print("Боец выбирает меч.")
    battle(fighter, monster)

    print()
    fighter.change_weapon(bow)
    monster2 = Monster()
    print("Боец выбирает лук.")
    battle(fighter, monster2)

    print()
    fighter.change_weapon(staff)
    monster3 = Monster("Дракон")
    print("Боец выбирает магический посох.")
    battle(fighter, monster3)