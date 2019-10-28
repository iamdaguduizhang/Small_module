# -*- coding:utf-8 -*-
# @Time   : 2019/10/10 9:36
# @Author : Dg
import os
import redis
import xlrd
import xlwt
from xlutils.copy import copy

R_PASS = os.environ["REDIS_PASS"]
print (R_PASS)
exit()
r = redis.Redis(host='116.255.163.127', port=6379, password=R_PASS)


def read_excel(path):
    """根据路径读取excel表格，结果为一个列表，里边元素为列表形式的每行数据"""
    """[
        ['姓名', '年龄', '性别', '分数'],
        ['mary', 20, '女', 89.9]
        ]
    """
    # 打开文件
    file_name = path
    workbook = xlrd.open_workbook(file_name)
    #获取sheet
    sheet_name= workbook.sheet_names()[0]
    # 根据sheet索引或者名称获取sheet内容
    # sheet的名称，行数，列数
    sheet_ = workbook.sheet_by_name(sheet_name)
    print (sheet_.name,sheet_.nrows)
    rows = []
    for x in range(1, sheet_.nrows):
        rows.append(sheet_.row_values(x))
    return rows


def write_excel(name, data, sheet_name='1'):
    # 只能写不能读
    stus = [
            ['姓名', '年龄', '性别', '分数'],
            ['mary', 20, '女', 89.9]
            ]
    book = xlwt.Workbook()  # 新建一个excel
    sheet = book.add_sheet(sheet_name)  # 添加一个sheet页
    row = 0  # 控制行
    for stu in data:
        col = 0  # 控制列
        for s in stu:  # 再循环里面list的值，每一列
            sheet.write(row, col, s)
            col += 1
        row += 1
    book.save('{}.xls'.format(name))  # 保存到当前目录下


def change_excel(x, y, data):
    # xlutils:修改excel
    book1 = xlrd.open_workbook('stu_1.xls')
    book2 = copy(book1)  # 拷贝一份原来的excel
    sheet = book2.get_sheet(0)  # 获取第几个sheet页，book2现在的是xlutils里的方法，不是xlrd的
    # 行，列，要写入的值
    sheet.write(x-1, y-1, data)
    sheet.write(1, 0, 'hello')
    book2.save('stu_2.xls')


def xianyu():
    """闲鱼的"""

    # 闲鱼添加任务字典
    lt = read_excel(r'C:\Users\Administrator\Desktop\xianyu_add_taskdict.xlsx')
    print (lt)
    task_dict = {}
    for x in lt:
        task_dict[int(x[0])] = x[1].split(';')
    print(task_dict)
    r.set('task_dict', str(task_dict))


def taobao():
    lt = read_excel(r'C:\Users\Administrator\Desktop\taobao_task.xlsx')
    taobao_task_dict = {}
    taobao_task_lt = []
    for x in lt:
        taobao_task_lt.append(int(x[0]))
        lt_ = []
        lt_.append(x[1])
        lt_.append(int(x[2]))
        taobao_task_dict[int(x[0])] = lt_
    print(taobao_task_dict)
    print(taobao_task_lt)
    r.set('taobao_task_lt', str(taobao_task_lt))
    r.set('taobao_task_dict', str(taobao_task_dict))


if __name__ == "__main__":
    xianyu()

    # with open(r'C:\Users\Administrator\Desktop\History\pythonSeleniumWebdriverChrome-master\pythonSeleniumWebdriverChrome-master\ChromeDriver\python\A_bilibli\5', 'r') as f:
    #     lt = eval(f.read())
    # write_excel('bilibli', lt, )
    # for x in lt:
    #     # print (x)
    #     uid = x[0].split('/')[-1]
    #     with open("uid.txt", "a") as fp2:
    #         fp2.write(str(uid) + "\n")
    # change_excel()
