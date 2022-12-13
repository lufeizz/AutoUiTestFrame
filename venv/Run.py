from HTMLTestRunner import HTMLTestRunner
import unittest
import time,os
from Public.Common import SendMail as cc
from Config import globalconfig
# 把当前文件所在文件夹的父文件夹路径加入到PYTHONPATH
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#测试报告所在路径
# report_path = globalconfig.report_path
#测试用例路径
# TestCase_path = globalconfig.TestCase_path

def AutoRun(TestCaseName):
    """
    :param TestCaseName: 测试用例名称
    :return:
    """
    discover = unittest.defaultTestLoader.discover(globalconfig.TestCase_path,pattern=TestCaseName)
    now = time.strftime('%Y-%m-%d %H_%M_%S')    #获取当前系统时间
    #拼接出测试报告名称
    filename = globalconfig.report_path+'\\'+now+'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,title='测试报告',description='用例执行情况')
    runner.run(discover)
    fp.close()
    #在测试报告目录下获取最新的测试报告
    new_report = cc.newReport(globalconfig.report_path)
    cc.sendReport(new_report)

#以邮件的形式发送测试报告
if __name__ == "__main__":
    AutoRun("TC_bing.py")