import xlrd




data = xlrd.open_workbook('12.xls')#

table = data.sheets()[0]          #通过索引顺序获取


table = data.sheet_by_name('Sheet1')#通过名称获取


names = data.sheet_names()    #返回book中所有工作表的名字

nrows = table.nrows
ncols=table.ncols
for i in range(nrows):
    for j in range(ncols):
        print(table.cell_value(i,j),end='\t')
