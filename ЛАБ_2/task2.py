def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False  # Found a divisor other than 1 and num itself

    return True


def func(var):
    if isinstance(var, list):
        count = 0
        count = 0
        sum_after_second_negative = 0
        found_second_negative = False

        for el in var:
            if count == 2:
                found_second_negative = True
            if el < 0:
                count += 1

            if found_second_negative:
                sum_after_second_negative += el
        odd_numbers = [el for el in var if el % 2 == 0]

        print("Сумма после второго отрицательного элемента:", sum_after_second_negative)
        print("Все четные элементы:", odd_numbers)
    if isinstance(var, set):
        print(f"Максимальный элемент{max(var)}\nМинимальный элемент{min(var)}")
    if isinstance(var, int):
        i = 0
        my_list = list()
        for i in range(var):

            if is_prime(i):
                my_list.append(i)

        print(my_list)
    if isinstance(var, str):
        list_n = list()
        for char in var:
            if char.isdigit():
                list_n.append(char)
        print(list_n)


while True:
    print("\nМеню:")
    print("1. Ввести список")
    print("2. Ввести множество")
    print("3. Ввести число")
    print("4. Ввести строку")
    print("5. До свидания")
    try:
        choice = input("Введите номер пункта меню: ")
        if choice == "1":
            while True:
                n = int(input("Введите размер списка: "))
                if n <= 0:
                    print("Размер не может быть отрицательным")
                else:
                    print("Введите элементы списка: ")
                    my_list = list()
                    for i in range(n):
                        el = int(input())
                        my_list.append(el)
                    func(my_list)
                    break



        elif choice == "2":
            while True:
                n = int(input("Введите размер множества: "))
                if n < 0:
                    print("Размер не может быть отрицательным")
                else:
                    print("Введите элементы множества: ")
                    my_set = set()
                    for i in range(n):

                        while True:
                            num = int(input())
                            if num in my_set:
                                print("Такое число существует в множестве. Повторите ввод")
                            else:
                                break
                        my_set.add(num)

                    func(my_set)
                    break


        elif choice == "3":
            n = int(input("Введите число: "))
            if n < 0:
                print("Число не может быть отрицательным")
            else:
                func(n)

        elif choice == "4":
            n = str(input("Введите строку: "))
            func(n)
        elif choice == "5":
            print("До свидания!")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите пункт из меню.")
    except ValueError:
        print("Введено неверное значение")
    finally:
        print("Завершение вычисления")

# a = ('wffwf1w31f321wefw')
# func(a)
# a = 58
# func(a)
# my_list = [1, 2, 3, 4, -2, 3, -1, 2, 1, 2, -3, 3, 8]
# func(my_list)
