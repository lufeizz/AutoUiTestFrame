import logging
import os
import time
from Config import globalconfig
log_path = globalconfig.log_path

class Logger():

    def __init__(self,LogFile,CmdLevel,FileLevel):
        self.logger = logging.getLogger(LogFile)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') #定义输出Handler的格式

        #设置日志文件名称
        self.LogFileName = os.path.join(log_path,"{0}.log".format(time.strftime("%Y-%m-%d")))

        #设置控制台日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(CmdLevel)

        #设置文件日志
        fh = logging.FileHandler(self.LogFileName)
        fh.setFormatter(fmt)
        fh.setLevel(FileLevel)

        # 给logger添加Handler
        self.logger.addHandler(fh)
        self.logger.addHandler(sh)

    def debug(self,message):
        self.logger.debug(message)

    def info(self,message):
        self.logger.info(message)

    def warning(self,message):
        self.logger.warning(message)

    def error(self,message):
        self.logger.error(message)

    def critical(self,message):
        self.logger.critical(message)



# if __name__ == '__main__':
#     logger = Logger('logging.log',CmdLevel=logging.DEBUG,FileLevel=logging.ERROR)
#     #应用日志
#     logger.debug("debug message")
#     logger.info("info message")
#     logger.warning("warning message")
#     logger.error("error message")
#     logger.critical("critical message")