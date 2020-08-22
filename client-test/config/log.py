
"""

import logging
logging.basicConfig(level=log_level, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', datefmt='%a, %d %b %Y %H:%M:%S', filename='parser_result.log', filemode='w')

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')

"""
import logging
import time
import sys
import os
#
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filemode='w')
#
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')


"""


logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
                    filename='new.log',
                    filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    #日志格式
                    )
如果在logging.basicConfig()设置filename 和filemode，则只会保存log到文件，不会输出到控制台。


"""
# logging.basicConfig(format="%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s")
# logging.StreamHandler()
# logging.debug("This message should go to the log file")
# logging.info("so should this")
# logging.warning("And this ,too")


"""

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.filter()

fh = logging.FileHandler("C://Users//msi//Desktop//example.txt",mode="a",encoding="UTF8")
sh = logging.StreamHandler()

fh.setLevel(logging.WARNING)
sh.setLevel(logging.WARN)

fh.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))

logger.addHandler(sh)
logger.addHandler(fh)
fh.close()

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')

"""


class Login(object):
    # 单例模式，保证运行脚本时不重复登录N多遍
    __instance = None
    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = super(Login,cls).__new__(cls,*args,**kwargs)
        return cls.__instance

log_path = os.path.dirname(os.path.abspath(__file__))

class Log(object):

    def __init__(self):
       self.logname = os.path.join(log_path, '{0}.log'.format(time.strftime('%Y-%m-%d')))

    def __printconsole(self,level,message):
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        fh = logging.FileHandler(filename=self.logname,mode="a",encoding="utf8")
        sh = logging.StreamHandler()

        fh.setLevel(logging.DEBUG)
        sh.setLevel(logging.DEBUG)

        fm = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        fh.setFormatter(fm)

        logger.addHandler(fh)
        logger.addHandler(sh)

        if level == "info":
            logging.info(message)

        elif level == 'debug':
            logger.debug(message)

        elif level == 'warning':
            logger.warning(message)

        elif level == 'error':
            logger.critical(message)
        elif level == "critical":
            logger.critical(message)
        #
        # logger.removeHandler(fh)
        # logger.removeHandler(sh)
        # fh.close()

    def debug(self,message):
        try:
            if isinstance(message,str):
                pass

            else:
                message = str(message)
        except Exception as reason:
            print(reason)

        self.__printconsole("level",message=time.strftime('%Y-%m-%d %H:%M:%S') + '\t' + message + '\n')

    def info(self,message):

        try:
            if isinstance(message,str):
                pass
            else:
                message = str(message)

        except Exception as reason:

            print(reason)

        self.__printconsole(level="info",message=time.strftime("%Y %m %d %H-%M-%S") + "\t" + message + "\n" )

    def warning(self,message):

        try:
            if isinstance(message,str):
                pass
            else:
                message = str(message)
        except Exception as reason:
            print(reason)

        self.__printconsole(level="warning",message=time.strftime("%Y %m %d %H-%M-%S") + "\t" + message + "\n")

    def error(self,message):
        try:
            if isinstance(message, str):
                pass
            else:
                message = str(message)
        except Exception as reason:
            print(reason)

        self.__printconsole(level="error", message=time.strftime("%Y %m %d %H-%M-%S") + "\t" + message + "\n")

    def critical(self,message):

        try:
            if isinstance(message, str):
                pass
            else:
                message = str(message)
        except Exception as reason:
            print(reason)

        self.__printconsole(level="critical", message=time.strftime("%Y %m %d %H-%M-%S") + "\t" + message + "\n")



Log().warning("dsfsfsf")