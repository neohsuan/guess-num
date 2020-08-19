import random
start = input('請決定隨機數字開始值： ')
end = input("請決定隨機數字結束值： ")
start = int(start)
end = int(end)

ans = random.randint(start, end)
count = 0
while True:
    count += 1 # count = count + 1
    num = input('請猜一個數字： ')
    num = int(num)
    if num == ans:
        print('終於猜對了!!!')
        print('這是你猜的第', count, '次')
        break
    elif num < ans:
        print('比答案小')
    else:
        print('比答案大')
    print('這是你猜的第', count, '次')