def maxValue(a, b, c):
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    return max


def minValue(a, b, c):
    min = a
    if b < min:
        min = b
    if c < min:
        min = c
    return min


mx = maxValue(14, 8, 23)
print(mx)

mi = minValue(4, 1, 67)
print(mi)
