# -*- coding:utf-8 -*-
# @Time   : 2019/10/10 9:36
# @Author : Dg
import xlrd
import xlwt
from xlutils.copy import copy


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


def write_excel(name, sheet_name, data):
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


if __name__ == "__main__":
    read_excel(r'')
    # write_excel()
    # change_excel()
