def hammingDistance(x, y):
    x = "{0:b}".format(x)
    y = "{0:b}".format(y)
    if len(x) > len(y):
        y = "0"*(len(x) - len(y)) + y
    if len(y) > len(x):
        x = "0"*(len(y) - len(x)) + x
    distance = 0
    for i in range(0, len(x)):
        if x[i] != y[i]:
            distance += 1
    return distance


if __name__ == '__main__':
    print(hammingDistance(12, 3))
