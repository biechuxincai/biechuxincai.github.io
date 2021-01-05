import random

cai = True
while cai:
    print("你有三次机会")
    for i in range(1, 4):
        a = int(input("请输入你猜的年龄"))
        b = 34
        if a > b:
          print("你猜的大于实际年龄")
        elif a < b:
          print("你猜的小于实际年龄")
        else:
          print("恭喜你猜对了！")
         # print("Gameover!")
          cai=False
          break
    else:
        c = input("是否继续游戏？")
        if c != 'Y':
          cai=False
else:
    print("GameOver!")
