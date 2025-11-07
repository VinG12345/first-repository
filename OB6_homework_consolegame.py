import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        other.health -= self.attack_power
        if other.health < 0:
            other.health = 0

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self):
        player_name = input("Введите имя вашего героя: ")
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print(f"Игра началась! {self.player.name} против {self.computer.name}.\n")
        turn = 0  # 0 - игрок, 1 - компьютер
        while self.player.is_alive() and self.computer.is_alive():
            if turn == 0:
                input(f"\nНажмите Enter, чтобы атаковать {self.computer.name}...")
                self.player.attack(self.computer)
                print(f"{self.player.name} атакует {self.computer.name} на {self.player.attack_power} урона!")
                print(f"У {self.computer.name} осталось {self.computer.health} здоровья.")
                turn = 1
            else:
                print(f"\n{self.computer.name} атакует {self.player.name} на {self.computer.attack_power} урона!")
                self.computer.attack(self.player)
                print(f"У {self.player.name} осталось {self.player.health} здоровья.")
                turn = 0

        print("\nИгра окончена!")
        if self.player.is_alive():
            print(f"Победил {self.player.name}!")
        else:
            print(f"Победил {self.computer.name}!")

if __name__ == '__main__':
    game = Game()
    game.start()