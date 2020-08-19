import random

ans = random.randint(1, 100)
while True:
    num = input('請猜一個數字： ')
    num = int(num)
    if num == ans:
        print('終於猜對了')
        break
    elif num < ans:
        print('比答案小')
    else:
        print('比答案大')