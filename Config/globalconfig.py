import os
from Public.Common.ReadConfigIni import ReadconfigIni

#读取配置文件
#获取config.ini的路径
file_path = os.path.split(os.path.realpath(__file__))[0]
#print(file_path)

#读取配置文件
read_config = ReadconfigIni(os.path.join(file_path,"config.ini"))
#print(read_config)

#借助config.ini获取项目的参数
project_path = read_config.getConfigValue("project","project_path")
#print(project_path)

#日志路径
log_path = os.path.join(project_path,"Report","Log")
# print(log_path)

#测试用例路径
TestCase_path = os.path.join(project_path,"TestCase")
# print(TestCase_path)

#测试报告路径
report_path = os.path.join(project_path,"Report","TestReport")
# print(report_path)

#测试数据路径
data_path = os.path.join(project_path,"Data")
#print(data_path)