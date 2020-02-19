def backspaceCompare(S, T):
    S = list(S)
    index = 0
    while index < len(S):
        if S[index] == "#" and (index - 1) >= 0:
            index -= 1
            S.pop(index)
            S.pop(index)
        elif S[index] == "#":
            S.pop(index)
        else:
            index += 1
    T = list(T)
    index = 0
    while index < len(T):
        if T[index] == "#" and (index - 1) >= 0:
            index -= 1
            T.pop(index)
            T.pop(index)
        elif T[index] == "#":
            T.pop(index)
        else:
            index += 1
    return S == T


if __name__ == '__main__':
    print(backspaceCompare("a##c", "#a#c"))