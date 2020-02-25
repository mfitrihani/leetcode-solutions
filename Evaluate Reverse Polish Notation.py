def evalRPN(tokens):
    index = 0
    while len(tokens) != 1:
        if tokens[index] == "+":
            value = int(tokens[index - 2]) + int(tokens[index - 1])
        elif tokens[index] == "-":
            value = int(tokens[index - 2]) - int(tokens[index - 1])
        elif tokens[index] == "*":
            value = int(tokens[index - 2]) * int(tokens[index - 1])
        elif tokens[index] == "/":
            value = int(tokens[index - 2]) / int(tokens[index - 1])
        else:
            index += 1
            continue
        tokens[index] = value
        tokens.pop(index - 2)
        tokens.pop(index - 2)
        index -= 2
    return int(tokens[0])


if __name__ == '__main__':
    print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
