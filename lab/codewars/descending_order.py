def descending_order(num):
    result = ""
    lst = list()
    for chur in str(num):
        lst.append(chur)
    lst.sort(reverse=True)
    for chur in lst:
        result += chur
    return int(result)

def descending_order2(num):
    return int("".join(sorted(str(num), reverse=True)))

print(descending_order(145))
print(descending_order2(145))
