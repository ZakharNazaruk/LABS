try:
    side_t = float(input("Введите сторону треугольника: "))
    print(side_t**side_t)
except ValueError:
    print("Введено неверное значение")
finally:
    print("Завершение программы")