class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    @staticmethod
    def info():
        print("Прямоугольник имеет 4 стороны и все углы перпендикулярны")

    def perimetr(self):
        per = self.length * 2 + self.width * 2
        print(f"Периметр прямоугольника равен {per}")

    def square(self):
        sq = self.length * self.width
        print(f"Площадь прямоугольника равна {sq}")

    @classmethod
    def difference(cls, length, width):
        return cls(length + 10, width + 10)


rect = Rectangle(10, 5)
rect.info()
rect.square()
rect.perimetr()
rect1 = Rectangle.difference(20, 20)
rect1.perimetr()


# width = input("Введите ширину треугольника")
        # while True:
        #     for ch in width:
        #         is_correct = True
        #         if ch.isalpha():
        #             is_correct = False
        #     if is_correct:
        #         break
        #     else:
        #         print("Некорректный ввод")
        # self.width = int(width)
        # length = input("Введите длину треугольника")
        # while True:
        #     for ch in length:
        #         is_correct = True
        #         if ch.isalpha():
        #             is_correct = False
        #     if is_correct:
        #         break
        #     else:
        #         print("Некорректный ввод")
        # self.length = int(length)