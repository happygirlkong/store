import random
# import pymysql
from DBUtils import update
from DBUtils import select

# 银行名称
bank_name = "中国工商银行昌平支行"

def welcome():
    print("---------------------------------------")
    print("-     中国农业银行账户管理系统V1.0      -")
    print("---------------------------------------")
    print("-  1.开户                             -")
    print("-  2.存钱                             -")
    print("-  3.取钱                             -")
    print("-  4.转账                             -")
    print("-  5.查询                             -")
    print("-  6.Bye!                             -")
    print("--------------------------------------")
# 银行的开户逻辑
def bank_addUser(account,leixing,username,password,country,province,street,door,money):
    # 判断是否已满
    sql = "select count(*) from bank"
    param = []
    data = select(sql,param,mode="one")
    if data[0] > 100:
        return 3

    sql1 = "select * from bank where username  = %s"
    param1 = [username]
    data1 = select(sql1,param1,mode= "all")

    # 判断是否开过户
    if len(data1) > 0:
        return 2

    # 正常开户
    sql2 = "insert into bank values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param2 = [account,leixing,username,password,country,province,street,door,money,bank_name]
    update(sql2,param2)
    return 1

# 开户的输入数据
def  addUser():
    leixing = input("请输入账户类型（一类 or 二类）：")
    username = input("请输入姓名：")
    password = input("请输入密码：")
    country = input("请输入国籍：")
    province = input("请输入省份：")
    street = input("请输入街道：")
    door = input("请输入您家门牌号：")
    money = int(input("请输入初始化您的银行卡余额："))
    account = random.randint(10000000,99999999)
    status = bank_addUser(account,leixing,username,password,country,province,street,door,money)

    if status == 3:
        print("对不起，该银行用户已满，请携带证件到其他银行办理！")
    elif status == 2:
        print("您之前已经开过户！禁止重复开户！")
    elif status  == 1:
        print("嘻嘻，开户成功！以下卡户的个人信息：")
        info = '''
            ------------个人信息查询结果-------------
            用户名：%s
            账号：%s
            密码：%s
            地址：
                国籍：%s
                省份：%s
                街道：%s
                门牌号：%s
            余额：%s
            开户行名称：%s
            ---------------------------------------
        '''
        print(info % (username,account,password,country,province,street,door,money,bank_name))
# 定义取钱逻辑
def out(zhanghao,mima,quchu):

    sql="select account from bank where account =%s"
    a = int(zhanghao)
    data= select(sql,a,mode="all")
    if len(data) == 0:
        return 1

    sql2="select password from bank where account=%s;"
    data2=select(sql2,a,mode="all")
    if mima != data2[0][0]:
        return 2

    sql3="select money from bank where account= %s;"
    data3=select(sql3,a,mode="all")
    if data3[0][0]<quchu:
        return 4

    sql4="select leixing from bank where account =%s;"
    data4=select(sql4,a,mode="all")
    if data4[0][0] =="一类" and quchu<=50000:
        sql5="update bank set money =money -%s where account;"
        data5=select(sql5,a,mode="all")
        return 3
    elif data4[0][0]== "二类" and quchu <= 20000:
        sql6 = "update bank set money =money -%s where account;"
        data6=select(sql6,a,mode="all")
        return 3
    else:
        print("转账金额过大")

#输入取钱信息
def cash():
    zhanghao = str(input("请输入账号"))
    mima = input("请输入密码")
    quchu = int(input("请输入取出的金额"))
    c=out(zhanghao,mima,quchu)
    if c == 1:
        print("账号不存在")
    elif c == 2:
        print("密码不正确")
    elif c == 4:
        print("账户余额不足")
    elif c == 3:
        print("取钱成功，共取出%s元"%(quchu))

# 定义存钱的逻辑
def out(zhanghao,mima,cunru):

    sql="select account from bank where account = %s"
    a = int(zhanghao)
    data = select(sql,a,mode = "all")
    if len(data) == 0:
        return 1

    sql2="select password from bank where account = %s;"
    data2=select(sql2,a,mode="all")
    if mima != data2[0][0]:
        return 2

    sql3="select money from bank where account= %s;"
    data3=select(sql3,a,mode="all")
    if data3[0][0] < cunru:
        return 4

    else:
        sql5="update bank set money =money +%s where account;"
        data5=select(sql5,a,mode="all")
        return 3


#输入存钱信息
def cunqian():
    zhanghao = int(input("请输入账号"))
    mima = input("请输入密码")
    cnuru = int(input("请输入存入的金额"))
    c = out(zhanghao,mima,cnuru)
    if c == 1:
        print("账号不存在")
    elif c == 2:
        print("密码不正确")
    elif c == 4:
        print("账户余额不足")
    elif c == 3:
        print("存钱成功，共取出%s元"%(cnuru))


# 定义转账的逻辑
def zhuanzhang():
    zhuanchu = input('请输入转出账号：')
    zhuanru = input("请输入转入账号：")
    password = input("请输入密码：")
    jine = int(input("请输入转账金额："))
    sql = "select account from bank where account = %s;"
    a = int(zhuanchu)
    bata = select(sql,a,mode = "all") #转出账号
    sql2 = "select password from bank where account = %s;"
    bata2 = select(sql2,a,mode = "all") #转出密码
    sql3 = "select money from bank where account=%s;"
    bata3 = select(sql3,a,mode="all") #转出金额
    sql4 = "select account from bank where account=%s;"
    b =int(zhuanru)
    bata4 = select(sql4,b,mode="all")
    sql5 = "select leixing from bank where account=%s"
    bata5 = select(sql5,a,mode="all")
    if len(bata)>0 and len(bata4) > 0 and password == bata2[0][0]:
        if sql5[0][0] == "一类" and jine<50000:
            sql6 = "update bank set money=money- %s where account=%s"
            c = [jine,zhuanchu]
            bata6 = update(sql6,c)
            sql8 ="update bank set money=moeny +%s where account=%s"
            d = [jine,zhuanru]
            bate8 =update(sql8,d)
            print()

        elif sql5[0][0] == "二类" and jine < 20000:
            sql7 = "update bank set money=money- %s where account=%s"
            c = [jine,zhuanchu]
            bata7 = update(sql7,c)
            sql9 = "update bank set money=moeny +%s where account=%s"
            d = [jine, zhuanru]
            bate9 = update(sql9, d)
            print()
            print()
        else:
            print("金额过大")
    if len(bata) == 0 or len(bata4) == 0:
        print("转出账号或者转入账号不是本银行")
    if len(bata) > 0 and password != bata2[0][0]:
        print("密码不正确")

# 银行的查询逻辑
def bank_account(account,password,):
    # 查询账号是否存在
    sql3 = "select * from bank where account = %s "
    param3 = [account]
    data3 = select(sql3,param3,mode= "one")
    if len(data3)  == 0 :
        return 3
    else :
        sql4 = "select * from bank where password = %s "
        param4 = [password]
        data4 = select(sql4, param4, mode="one")
        if len(data4) == 0:
            return 2
        else:
            return 1

    # 正常查询
    # bank[account] = {
    #     "account":account,
    #     "password":password,
    # }
    # return 1


# 查询的输入数据
def query():
    account =  int(input("请输入账号："))
    password = str(input("请输入密码："))
    status = bank_account(account,password)

    if status == 3:
        print("该用户不存在！")
    elif status == 2:
        print("密码错误！")
    elif status  == 1:
        print("查询成功！以下显示卡户的个人信息：")

        sql4 = "select * from bank where password = %s "
        param4 = [password]
        data4 = select(sql4, param4, mode="one")
        for i in data4 :
            print(i)
        # print ("个人信息查询结果：%s" % str (bank[account]))
        # print(bank)
#拜拜

while True:
    welcome()
    chose = input("请输入业务编号：")
    if chose == "1":
        addUser()
    elif chose == "2":
        cunqian()
        break
    elif chose == "3":
        cash()
    elif chose == "4":
        zhuanzhang()
    elif chose == "5":
        query()
    elif chose == "6":
        print("baibai")
        break



































































