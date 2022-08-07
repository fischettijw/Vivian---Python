def maxValue(a, b, c):
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    return max


m = maxValue(14, 8, 23)
print(m)
