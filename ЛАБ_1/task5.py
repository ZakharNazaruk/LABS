toys = {
    "Мяч": ["Описание мяча", 10.0, 50],
    "Кукла": ["Описание куклы", 15.0, 30],
    "Конструктор": ["Описание конструктора", 20.0, 40],
    "Машинка": ["Описание машинки", 12.0, 60],
    "Пазл": ["Описание пазла", 18.0, 20],
    "Кубики": ["Описание кубиков", 8.0, 70]
}

while True:
    print("\nМеню:")
    print("1. Просмотр описания")
    print("2. Просмотр цены")
    print("3. Просмотр количества")
    print("4. Вся информация")
    print("5. Покупка")
    print("6. До свидания")

    choice = input("Введите номер пункта меню: ")

    if choice == "1":
        toy_name = input("Введите название игрушки: ")
        if toy_name in toys:
            print("Описание:", toys[toy_name][0])
        else:
            print("Такой игрушки нет в магазине.")

    elif choice == "2":
        toy_name = input("Введите название игрушки: ")
        if toy_name in toys:
            print("Цена:", toys[toy_name][1])
        else:
            print("Такой игрушки нет в магазине.")

    elif choice == "3":
        toy_name = input("Введите название игрушки: ")
        if toy_name in toys:
            print("Количество:", toys[toy_name][2])
        else:
            print("Такой игрушки нет в магазине.")

    elif choice == "4":
        for toy, info in toys.items():
            print(f"{toy}: {info[0]}, Цена: {info[1]}, Количество: {info[2]}")
    elif choice == "5":
        flag = 0

        purchase_list = []
        while True:
            toy_name = input("Введите название игрушки (n - завершить покупки): ")
            if toy_name == "n":
                break

            if toy_name in toys:
                quantity = int(input("Введите количество: "))
                if quantity <= 0:
                    print("Вы ввели отрцательное число или не взяли игрушек")
                    flag = 1
                    break
                else:
                    if quantity <= toys[toy_name][2]:
                      purchase_list.append((toy_name, quantity))
                      toys[toy_name][2] -= quantity
                    else:
                      print("Недостаточно товара на складе.")
            else:
                print("Такой игрушки нет в магазине.")
        if 0 == flag:
            total_price = sum(toys[toy][1] * quantity for toy, quantity in purchase_list)
            print("Вы купили:")
            for toy, quantity in purchase_list:
                print(f"{toy}: {quantity} шт")
            print("Итого:", total_price, "руб")

    elif choice == "6":
        print("До свидания!")
        break

    else:
        print("Некорректный ввод. Пожалуйста, выберите пункт из меню.")