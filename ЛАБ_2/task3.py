while True:
    try:
        m = int(input("Введите кол-во строк: "))
        n = int(input("Введите кол-во столбцов: "))
        if n <0 or m <0:
            print("Размер матрицы не может быть отрицательным")
        else:
            matrix = list()
            j=0
            for i in range(m):
                j = 0
                line = []
                for j in range(n):

                    el=int(input(f"Введите элемент {i},{j}: "))

                    line.append(el)
                    j+=1


                matrix.append(line)
                i+=1
            print(matrix)
            while True:
                i = int(input("Введите столбец №1: "))
                j = int(input("Введите столбец №2: "))
                ind = 0
                if i<m or j<n or i<=0 or j<=0:
                    print("Ошибка")
                else:
                    for ind in range(m):
                        m = matrix[ind][i]
                        matrix[ind][i]=matrix[ind][j]
                        matrix[ind][j] = m
                    print (matrix)
    except ValueError:
        print("Введено неверное значение")
    finally:
        print("Завершение программы")

