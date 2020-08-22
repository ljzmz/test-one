import logging
import time
import os

log_path = os.path.dirname(os.path.abspath(__file__))
class Log(object):
    def __init__(self):
        self.logname = os.path.join(log_path, '{0}.log'.format(time.strftime('%Y-%m-%d')))

    def __printconsole(self, level, message):

        # 先建立一个收集器
        logger = logging.getLogger()
        # 设置收集的等级
        logger.setLevel(logging.DEBUG)

        # 建立两个处理器有一个用在控制台输出，一个用于写入文本
        fh = logging.FileHandler(filename=self.logname,mode="a",encoding="utf8")
        fh.setLevel(logging.CRITICAL)

        sh = logging.StreamHandler()
        sh.setLevel(logging.WARN)

        # 给这两个控制器设定输出格式
        #fm = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)")
        fm = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        fh.setFormatter(fmt=fm)
        sh.setFormatter(fmt=fm)

        logger.addHandler(fh)
        logger.addHandler(sh)

        if level == "debug":
            logger.debug(message)
        elif level == "info":
            logger.info(message)
        elif level == "warning":
            logger.warning(message)
        elif level == "error":
            logger.error(message)
        elif level == "critical":
            logger.critical(message)

        logger.removeHandler(fh)
        logger.removeHandler(sh)
        fh.close()



    def debug(self, message):
        try:
            if isinstance(message, str):
                pass

            else:
                message = str(message)
        except Exception as reason:
            print(reason)

        self.__printconsole("dug", message=time.strftime('%Y-%m-%d %H:%M:%S') + '\t' + message + '\n')

    def info(self, message):

        try:
            if isinstance(message, str):
                pass
            else:
                message = str(message)

        except Exception as reason:

            print(reason)

        self.__printconsole(level="info", message=time.strftime("%Y %m %d %H-%M-%S") + "\t" + message + "\n")

    def warning(self, message):

        try:
            if isinstance(message, str):
                pass
            else:
                message = str(message)
        except Exception as reason:
            print(reason)

        self.__printconsole(level="warning", message=time.strftime("%Y %m %d %H-%M-%S") + "\t" + message + "\n")

    def error(self, message):
        try:
            if isinstance(message, str):
                pass
            else:
                message = str(message)
        except Exception as reason:
            print(reason)

        self.__printconsole(level="error", message=time.strftime("%Y %m %d %H-%M-%S") + "\t" + message + "\n")

    def critical(self, message):

        try:
            if isinstance(message, str):
                pass
            else:
                message = str(message)
        except Exception as reason:
            print(reason)

        self.__printconsole(level="critical", message=time.strftime("%Y %m %d %H-%M-%S") + "\t" + message + "\n")


Log().warning("sdfsdfsdfsf")