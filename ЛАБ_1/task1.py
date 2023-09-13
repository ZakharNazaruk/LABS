num = input("Введите натуральное число: ")
sum = 0
for digit in num:
    if digit.isdigit():
      if int(digit) % 2 == 0:
        sum = sum + int(digit)
    else:
      break
print("Сумма четных цифр введенного числа", sum)