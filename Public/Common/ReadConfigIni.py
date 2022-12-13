import configparser
import codecs
import os


class ReadconfigIni():
    """
    实例化configparser
    """

    def __init__(self, filename):
        self.cf = configparser.ConfigParser()
        self.cf.read(filename)

    # 读操作
    def getConfigValue(self, config, name):
        value = self.cf.get(config, name)
        return value


#验证ReadConfigIni（）类的正确性，该部分为测试代码，实际框架运行时需注释掉
# file_path = os.path.split(os.path.realpath(__file__))[0]
# print(file_path)
# read_config = ReadconfigIni(os.path.join(file_path,"config.ini"))
# print(read_config)
# value = read_config.getConfigValue("url","BingUrl")
# print(value)
