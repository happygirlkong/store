'''
在注释里增加：
1、猜的数字是系统产生，不是自己定义
            使用random随机数技术来获取随机数
 范围：0~150
    猜10次！
    如果输入大了：温馨提示：大了
    如果输入小了：温馨提示：小了
    正好猜中，恭喜您，猜中，本次猜的数字为xxxx。
操作完成之后才增加：
    起始：5000金币，每猜错一次，减去500金币，一直扣完为止。15次没猜中，系统锁定。猜中加3000。
'''
import random

ran = random.randint(0,150)
print(ran)
money = 5000
print("您的初始金币为：5000" ,end=",")
print("猜对加3000，猜错减500，您共有15次机会")
i = 1
while i <= 15 :


    sum = int(input("请输入您猜的第 %d 数字：" %i))
    if ran == sum :
        money += 3000
        print("恭喜您猜中，本次的数字为 %d" %ran)

    elif ran < sum :
        money -= 500
        print("您输入的数字太大了")

    else :
        money -= 500
        print("您输入的数字太小了")


    print("目前剩余金币数量：%d"%money)

    i += 1


number = 30
for i in range(3):
    guess_number = int(input("guess_number:"))
    if guess_number > 30:
        print("bigger")
    elif guess_number <30:
        print("smaller")
    else:
        print("you are right!")
        break
else:
    print("you have tired 3 times,game exit")

