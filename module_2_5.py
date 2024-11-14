def get_matrix(n, m, value):
    if n <= 0 or m <= 0:
        return []

    ret = []
    for i in range(n):
        ret.append([])
        for j in range(m):
            ret[i].append(value)

    return ret

print(get_matrix(4, 2, 13))
