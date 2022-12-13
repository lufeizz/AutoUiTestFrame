from Public.Pages.BasePage import BasePage
from time import sleep
from Public.Common.DoExcel import ReadExcel


class Search(BasePage):
    SearchId = ("css","#sb_form_q")
    SearchBtn = ("xpath","//*[@id='search_icon']")

    def Search_Value(self,SearchValue):
        #给输入框进行赋值操作
        searchVale = self.findElement(self.SearchId)
        self.type(searchVale,SearchValue)
        #单机Baidu按钮
        sleep(2)
        searchBtn = self.findElement(self.SearchBtn)
        self.click(searchBtn)
        sleep(2)
        self.quit()


#验证Search_Value()类的正确性，为测试代码，实际框架运行时需注释
# search = Search()
# url = ReadExcel("Data.xls","Data").read_excel(1,0)
# baidu_value = ReadExcel("Data.xls","Data").read_excel(1,1)
# search.open(url)
# search.Search_Value(baidu_value)
