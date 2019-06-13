# 1부터 100까지의 랜덤 숫자 생성
import random

min,max = 1, 100

print(min,'-',max)
while True:
    answer = random.randrange(max)+min
    i = 1
    while True:
        num = int(input(str(i)+' >> '))
        if answer == num:
            print('맞았습니다.')
            break
        elif answer > num:
            print('더 높게')
        else:
            print('더 낮게')
        i+=1
    if 'n' == input('다시 하시겠습니까(y/n) >> '):
        break