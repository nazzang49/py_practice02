def sum(*num):
    total = 0
    for n in num:
        total+=n
    return total

print(sum(1,2,3,4))