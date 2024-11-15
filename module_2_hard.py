def find_dividers(x):
    l = []
    for j in range(2, x):
        if x % j == 0:
            l.append(j)
    return l

def ret_value(x): #ищем все пары чисел для x
    ret_ = ""
    if x < 3:
        return ret_

    if x % 2 == 0:
        r = x // 2
    else:
        r = x // 2 + 1

    for i in range(1, r):
        ret_ += str(i) + str(x - i)
    return ret_

while True:
    a = input("Введите число от 3 до 20, или 'q' для завершения: ")
    if a == "q":
        break

    a = int(a)
    list_ = find_dividers(a)
    list_.append(a)
    print(list_)
    s = ""
    for i in list_ :
        s += ret_value(i)
    print(s)
