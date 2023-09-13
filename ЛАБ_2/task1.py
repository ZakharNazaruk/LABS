import math
def Triangle(side):
    perimetr = side * 3
    h = math.sqrt((side**2)-((side/2)**2))
    square = (h*side)/2
    return perimetr, square

while True:
    try:
        side_t = float(input("Введите сторону треугольника: "))
        if side_t<=0:
            print("Стороноа не может быть отрицательной")
        else:
            print(Triangle(side_t))
            exit()
    except ValueError:
        print("Введено неверное значение")

    finally:
        print("Завершение вычисления")
