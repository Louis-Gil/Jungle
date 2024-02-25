def put_star(num):
    if num == 1:
        return ["*"]
    star = put_star(num//3)
    L = []
    for i in star:
        L.append(i * 3)
    for i in star:
        L.append(i + ' '*(num//3) + i)
    for i in star:
        L.append(i * 3)
    return L

test1 = put_star(9)
print('\n'.join(test1))
