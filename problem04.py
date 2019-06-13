for i in range(1,100):
    i = str(i)
    print(i,'',end='')
    for j in i:
        j = int(j)
        if j%3==0 and j!=0:
            print('짝',end='')
    print()