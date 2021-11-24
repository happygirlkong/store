import xlrd

# 工作簿对象
wb = xlrd.open_workbook(filename=r"E:\pythonProject\课程\day-9\百度合作单位-人员管理-二期.xls")
st = wb.sheet_by_index(0)
rows = st.nrows

a = 0#手机号
b = 0
c = 0
d = 0#年龄
e = 0#男女
f = 0
g = 0#工资
h = 0
i = 0#公司
k = 0# 疫情地区

for j  in range(1,rows):
    data = st.row_values(j)
    if data[5] .startswith('14' or '17'):
        a += 1
    elif data[5].startswith('13'):
        b += 1
    elif data[5].startswith('15'):
        c += 1
    if data[8] == "男":
        d += 1
    elif data[8] =='女' :
        e += 1
    if data[7] > 45 :
        f += 1
    if data[11] > 8000:
        g += 1
    elif data[11] < 3000:
        h += 1
    if data[13] .endswith('传媒有限公司'):
        i += 1
    if data[9] .startswith('黑龙江'or'北京'or'福建'or'四川'):
        k += 1

print("a、表格的总人数为：%s人" %j)
print('b、使用电信：%s人 ,使用移动:%s人 ,使用联通：%s人' %(a,b,c))
print("c、男生人数为：%s人 ,女生人数为:%s人" %(d,e))
print('d、45岁以上的人数为：%s人' %f)
print('e、工资8000以上的人数为：%s人 ,工资3000以下的人数为：%s人' %(g,h))
print('f、去传媒有限公司的人数为:%s人'%i)
print('g、高危地区的人数为：%s人'%k)


import xlrd
import pymysql


# import importlib
# importlib.reload(sys) #出现呢reload错误使用


def open_excel():
    try:
        book = xlrd.open_workbook("百度合作单位-人员管理-二期.xlsx")  # 文件名，把文件与py文件放在同一目录下
    except:
        print("open excel file failed!")
    try:
        sheet = book.sheet_by_name("人员管理")  # execl里面的worksheet1
        return sheet
    except:
        print("locate worksheet in excel failed!")


# 连接数据库
try:
    db = pymysql.connect(host="loacalhost", user="root",
                         passwd="",
                         db="baidu",
                         charset='utf8')
except:
    print("could not connect to mysql server")


def search_count():
    cursor = db.cursor()
    select = "select count(id) from user"  # 获取表中xxxxx记录数
    cursor.execute(select)  # 执行sql语句
    line_count = cursor.fetchone()
    print(line_count[0])


def insert_deta():
    sheet = open_excel()
    cursor = db.cursor()
    for i in range(1, sheet.nrows):  # 第一行是标题名，对应表中的字段名所以应该从第二行开始，计算机以0开始计数，所以值是1
        account = sheet.cell(i, 0).value  # 取第i行第0列
        iden= sheet.cell(i, 1).value  # 取第i行第1列，下面依次类推
        username = sheet.cell(i, 2).value
        truename = sheet.cell(i, 3).value
        password=sheeet.cell(i,4).value
        phone=sheeet.cell(i,5).value
        mailbox=sheeet.cell(i,6).value
        age=sheeet.cell(i,7).value
        sex=sheeet.cell(i,8).value
        address=sheeet.cell(i,9).value
        datetime=sheeet.cell(i,10).value
        sal=sheeet.cell(i,11).value
        company=sheeet.cell(i,12).value
        print(account)
        print(iden)
        print(username)
        print(truename)
        print(password)
        print(phone)
        print(mailbox)
        print(age)
        print(sex)
        print(address)
        print(datetime)
        print(sal)
        print(company)

        value = account,iden,username,truename,password,phone,mialbox,age,sex,address,datetime,sal,company)
        print(value)
        sql = "INSERT INTO user(account,iden,username,truename,password,phone,mialbox,age,sex,address,datetime,sal,company)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, value)  # 执行sql语句
        db.commit()
    cursor.close()  # 关闭连接


insert_deta()

db.close()  # 关闭数据
print("ok ")