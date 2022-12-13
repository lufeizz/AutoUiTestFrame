import unittest
import logging
from time import sleep
from Public.Common import Log
from Public.Common import TestCaseInfo,DoExcel,CommonConfig as cc
from Public.Pages import Bing

#从测试数据Excel中读取测试数据
bing_search_value = DoExcel.ReadExcel("Data.xls","Data").read_excel(1,1)
url_value = DoExcel.ReadExcel("Data.xls","Data").read_excel(1,0)


class Test_Baidu_Search(unittest.TestCase):

    def setUp(self) -> None:
        self.base_url = url_value
        self.testcaseInfo = TestCaseInfo.TestCaseInfo(id=1,name="bing search",owner="leo")

    def test_searchBaidu(self):
        try:
            self.testcaseInfo.starttime = cc.getCurrentTime()
            #实例化baidu文件中的search类
            self.baiduSearch = Bing.Search()
            self.baiduSearch.open(self.base_url)
            sleep(2)
            self.baiduSearch.Search_Value(bing_search_value)
            sleep(2)

            #调用日志
            logger = Log.Logger("FOX",CmdLevel=logging.INFO,FileLevel=logging.INFO)
            logger.info("成功了")
            logger.debug("也成功了")
            self.testcaseInfo.result = "successful"
        except Exception as err:
            self.testcaseInfo.errorinfo = str(err)
            logger = Log.Logger("FOX",CmdLevel=logging.DEBUG,FileLevel=logging.INFO)
            logger.info("失败了")
            logger.debug("也失败了")
            self.testcaseInfo.result = 'fail'

    def tearDown(self) -> None:
        pass


# if __name__ == '__main__':
#     unittest.main()