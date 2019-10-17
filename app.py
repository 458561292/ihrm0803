import os
import logging
import logging.handlers

BASE_URL = "http://182.92.81.159/api/sys/"
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

TOKEN = None
ID = None


# 添加日志信息
def my_log_config():
    # 1.创建日志器
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # 2.创建处理器
    ch = logging.StreamHandler()
    # 3.创建格式化器
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt=fmt)
    # 4.三者组合
    ch.setFormatter(formatter)
    logger.addHandler(ch)
