class Animal:
    def __init__(self, breed):
        self.breed = breed

    def way_of_movement(self):
        print("Животное передвигается")

class Fish(Animal):
    def __init__(self):
        while True:
            name = input("Введите название рыбы: ")
            if not any(char.isdigit() for char in name):
                break
            else:
                print("Некорректный ввод. Повторите.")

        super().__init__(name)
        while True:
            price = input(f"Введите цену на {name}: ")
            if price.isdigit() and int(price) > 0:
                break
            else:
                print("Некорректный ввод. Повторите.")

        self.price = int(price)

    def way_of_movement(self):
        super().way_of_movement()
        print("С помощью плавников в воде")

class Bird(Animal):
    def __init__(self):
        while True:
            name = input("Введите название птицы: ")
            if not any(char.isdigit() for char in name):
                break
            else:
                print("Некорректный ввод. Повторите.")

        super().__init__(name)
        while True:
            price = input(f"Введите цену на {name}: ")
            if price.isdigit() and int(price) >0:
                break
            else:
                print("Некорректный ввод. Повторите.")

        self.price = int(price)

    def way_of_movement(self):
        super().way_of_movement()
        print("С помощью крыльев по воздуху")

class ZooShop:
    def __init__(self):
        self.animals = []
        self.price = []

    def add_animal(self, animal, price):
        self.animals.append(animal)
        self.price.append(price)

    def show_max_price(self):
        if self.price:
            max_price_index = self.price.index(max(self.price))
            print(f"Самая дорогая порода: {self.animals[max_price_index].breed} с ценой {self.price[max_price_index]}")
        else:
            print("В магазине нет животных.")

    def show_animal_movement(self, breed):
        found = False
        for animal in self.animals:
            if animal.breed == breed:
                print(f"{breed} передвигается:")
                animal.way_of_movement()
                found = True
                break

        if not found:
            print(f"Нет животного с породой {breed} в магазине.")

    def show_price(self):
        name = input("Введите название животного, у которого вы хотите узнать цену: ")
        is_found = False
        i = 0
        for i in range(len(self.animals)):
            if self.animals[i].breed == name:
                is_found = True
                break
        if is_found:
            print(f"Цена на {name} = {self.price[i]}")
        else:
            print("Такого животного в магазине не существует")
    def show_info(self):

        for i in range(len(self.animals)):
            print(f"Животное: {self.animals[i].breed} Цена: {self.price[i]}")
    def write_to_file(self):
        with open("zoo.txt", 'w',encoding="utf-8") as my_f:
            for i in range(len(self.animals)):
                my_f.write(f"Животное: {self.animals[i].breed} Цена: {self.price[i]}\n")
my_zoo = ZooShop()

while True:
    print("Что вы хотите выполнить:")
    print("1. Добавить в магазин рыбу")
    print("2. Добавить в магазин птицу")
    print("3. Узнать цену животного")
    print("4. Узнать породу самого дорогого животного")
    print("5. Узнать способ передвижения животного")
    print("6. Просмотреть всех животных")
    print("0. Закончить программу")
    choice = input()

    if choice.isdigit() and 0 <= int(choice) <= 6:
        if int(choice) == 1:
            my_fish = Fish()
            my_zoo.add_animal(my_fish, my_fish.price)
        elif int(choice) == 2:
            my_bird = Bird()
            my_zoo.add_animal(my_bird, my_bird.price)
        elif int(choice) == 3:
            if len(my_zoo.animals) == 0:
                print("Еще нет животных в магазине")
            else:
                my_zoo.show_price()
        elif int(choice) == 4:
            if len(my_zoo.animals) == 0:
                print("Еще нет животных в магазине")
            else:
                my_zoo.show_max_price()
        elif int(choice) == 5:
            if len(my_zoo.animals) == 0:
                print("Еще нет животных в магазине")
            else:
                breed = input("Введите название: ")
                my_zoo.show_animal_movement(breed)
        elif int(choice) == 6:
            if len(my_zoo.animals) == 0:
                print("Еще нет животных в магазине")
            else:

                my_zoo.show_info()
        elif int(choice) == 0:
            break
    else:
        print("Некорректный ввод")
my_zoo.write_to_file()