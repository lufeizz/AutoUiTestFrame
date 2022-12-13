import xlrd
import os
from Config import globalconfig
data_path = globalconfig.data_path


#读取Excel封装到一个类中
#实现数据驱动测试

class ReadExcel():
    """
    打开excel读取数据
    """
    #打开excel
    # def __init__(self,filename,sheetname):
    #     self.workbook = xlrd.open_workbook(filename)
    #     self.sheetName = self.workbook.sheet_by_name(sheetname)

    #读取其他目录下的Excel文件
    def __init__(self,filename,sheetname):
        datapath = os.path.join(data_path,filename)
        self.workbook = xlrd.open_workbook(datapath)
        self.sheetName = self.workbook.sheet_by_name(sheetname)
    #获取某个单元格数据
    def read_excel(self,rownum,colnum):
        value = self.sheetName.cell(rownum,colnum).value
        return value


#验证ReadExcel（）类的正确性，该部分为测试代码，实际框架运行时需注释掉
# cellValue = ReadExcel("Data.xls","Data").read_excel(1,0)
# print(cellValue)