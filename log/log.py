import logging
from config.config import logfile

# 创建日志记录器
logger = logging.getLogger()
logger.setLevel(logging.INFO)
# 设置日志输出格式
format = logging.Formatter('%(asctime) s%(filename)s[line:%(lineno)d)]%(levelname)s %(message)s')
# 创建一个Handler用于将日志写入文件
fh = logging.FileHandler(filename=logfile,mode='a',encoding='utf-8')
fh.setLevel(logging.INFO)
fh.setFormatter(format)
logger.addHandler(fh)
# 创建一个Handler用于控制台输出日志
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(format)
logger.addHandler(ch)
