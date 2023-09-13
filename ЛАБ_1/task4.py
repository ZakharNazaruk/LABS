my_dict = {'a': 12, 'b': 13, 'c': 56, 'd': 400, 'e': 58, 'f': 20}

sorted_items = sorted(my_dict.items(), key=lambda x: x[1])

top_three = sorted_items[:3]

result = [item[0] for item in top_three]

print(result)