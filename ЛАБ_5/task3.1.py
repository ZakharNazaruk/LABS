import numpy as np
import matplotlib.pyplot as plt

x = 3.567
a_values = (-5,12,2.5)
arg_values = []
func_values = []
for a in a_values:

    func_value = np.sin(x/3)+1.2*a
    arg_values.append(x)
    func_values.append(func_value)

arg_values = np.array(arg_values)
func_values = np.array(func_values)
max_value = func_values.max()
min_value = func_values.min()
mean_value = func_values.mean()
num_elements = func_values.size

print("max: ", max_value)
print("min: ", min_value)
print("mean: ", mean_value)
print("quantity: ", num_elements)

plt.plot(a_values, func_values, 'o-', label='f(x)')
plt.axhline(mean_value, color='r', linestyle='--', label='mean')

plt.xlabel('a')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.title('изменение ф-ции ')
plt.show()