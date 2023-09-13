
my_list = [12, 511, 'Python', 311, 122, 'love']

for index, item in enumerate(my_list):
    if isinstance(item, int):
        if item % 2 == 0:
            digit_sum = sum(int(digit) for digit in str(item))
            my_list[index] = digit_sum
        else:
            my_list[index] = 1

print(my_list)