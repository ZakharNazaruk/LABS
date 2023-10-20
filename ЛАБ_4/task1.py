class MyList:
    def __init__(self):
        self.data = []

    def add_item(self, item):
        self.data.append(item)

    def show_list(self):
        print(self.data)

    def remove_item(self, item):
        self.data.remove(item)

    def get_length(self):
        return len(self.data)

    def get_item(self):
        return self.data

    def clear_list(self):
        print("Очищаем список")
        self.data = []


my_list = MyList()

my_list.add_item(1)
my_list.add_item(2)
my_list.add_item(3)

print("Список:", my_list.get_item())

print("Длина списка:", my_list.get_length())

my_list.remove_item(2)

print("Обновленный список:", my_list.get_item())

my_list.clear_list()

print("Список после очистки:", my_list.get_item())