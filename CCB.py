def bank(accountID,name,money=0):
    print("New account opening information：\n-----------------")
    print("account：",accountID)
    print("name: ",name)
    print("balance：",money)
    print()

    def seeMoney():
        print("The latest balance",money)

    def getMoney(number):
        nonlocal money
        if isinstance(number,(int,float)) == True:
            if number >= 0:
             money= money+number
            else:
                print("The deposit amount cannot be negative！")
        else:
            print("number must be int or float!")
    seeMoney()
#
    def putMoney(number):
        nonlocal money
        if isinstance(number,(int,float))  == True:
            if number >= 0 and  number <= money:
                money=money-number
            else:
                  print("The balance is insufficient")
        else:
             print("number must be int or float!")
        seeMoney()
#


    def menu():
        print("account information：\n-----------------")
        print("account：", accountID)
        print("name：", name)
        while True:
            try:
                opNum = int(input("Please enter what you want to do：（1.Save the money 2.Take the money 3Balance query 4.quit）"))
                if opNum == 1:
                    number = int(input("Please enter the deposit amount："))
                    getMoney(number)
                elif opNum == 2:
                    number = int(input("Please enter the withdrawal amount："))
                    putMoney(number)
                elif opNum == 3:
                    seeMoney()
                elif opNum == 4:
                    print("退卡成功！\n")
                    break
                else:
                    print("请输入有效操作！")
            except:
                    print("请输入有效操作！")
    return menu

users = []  # 保存银行的所有储户
users.append(bank(1002, "Daniel", 10000))

# 使用索引调用函数
users[0]()
























