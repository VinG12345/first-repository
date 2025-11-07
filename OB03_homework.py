import json

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __str__(self):
        return f"{self.species} по имени {self.name}"

    def to_dict(self):
        return {"name": self.name, "species": self.species}

    @staticmethod
    def from_dict(data):
        return Animal(data["name"], data["species"])

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def list_animals(self):
        if not self.animals:
            print("Зоопарк пуст.")
        for animal in self.animals:
            print(animal)

    def save_to_file(self, filename):
        data = [animal.to_dict() for animal in self.animals]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Зоопарк сохранён в файл {filename}.")

    def load_from_file(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.animals = [Animal.from_dict(item) for item in data]
            print(f"Зоопарк загружен из файла {filename}.")
        except FileNotFoundError:
            print("Файл не найден. Начинаем с пустого зоопарка.")

# Пример интерфейса
def main():
    zoo = Zoo()
    filename = "zoo.json"
    zoo.load_from_file(filename)
    while True:
        print("\n1. Добавить животное\n2. Показать всех животных\n3. Сохранить\n4. Выйти")
        choice = input("Выберите действие: ")
        if choice == "1":
            name = input("Имя животного: ")
            species = input("Вид животного: ")
            zoo.add_animal(Animal(name, species))
        elif choice == "2":
            zoo.list_animals()
        elif choice == "3":
            zoo.save_to_file(filename)
        elif choice == "4":
            zoo.save_to_file(filename)
            print("Выход. Зоопарк сохранён.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()