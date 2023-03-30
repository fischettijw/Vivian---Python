'''
The following are examples of Python user created functions
'''


def add(a, b):
    '''
    provide two number ("a" and "b") to be added and
    this function will return the sum
    '''
    sum = a + b
    return sum


def mult(a, b):
    '''
    provide two number ("a" and "b") to be multiplied and
    this function will return the product
    '''
    product = a * b
    return product


def maximum(numbers):
    '''
    provide a LIST variable ("numbers") that contains
    at least 10 numeric value and this function will
    return the maximum value in the list
    '''
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


def celsius_to_fahrenheit(celsius):
    '''
    provide a temperature in degrees CELSIUS ("celsius")
    and this fuction will return it's equivalent
    in degrees fahrenhelt
    '''
    fahren = (celsius * 9 / 5) + 32
    return fahren


def fahrenheit_to_celsius(fahrenheit):
    '''
    provide a temperature in degrees FAHRENHEIT ("fahrenheit")
    and this fuction will return it's equivalent
    in degrees celsius
    '''
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius
