import my_functions as func

x = 5
y = 6
c_temp = 15
f_temp = 59
list_of_numbers = [-45, 56, 4, -8, -67]

print("The sum of", x, "and", y, "=", func.add(x, y))

print("The multiplication of", x, "and", y, "=", func.mult(x, y))

print(c_temp, "Celsius is =", func.celsius_to_fahrenheit(c_temp), "Fahrenheit")

print(f_temp, "Fahrenheit =", func.fahrenheit_to_celsius(f_temp), "Celsius")

print("The maximum number in list", list_of_numbers, "=", func.maximum(list_of_numbers))
