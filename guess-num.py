import random

ans = random.randint(1, 100)
count = 0
while True:
    count += 1 # count = count + 1
    num = input('請猜一個數字： ')
    num = int(num)
    if num == ans:
        print('終於猜對了')
        print('這是你猜的第', count, '次')
        break
    elif num < ans:
        print('比答案小')
    else:
        print('比答案大')
    print('這是你猜的第', count, '次')