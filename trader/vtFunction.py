# encoding: UTF-8

"""
包含一些开发中常用的函数
"""

import os
import decimal
import json
from datetime import datetime


MAX_NUMBER = 10000000000000
MAX_DECIMAL = 4


#----------------------------------------------------------------------
def safeUnicode(value):
    """检查接口数据潜在的错误，保证转化为的字符串正确"""
    # 检查是数字接近0时会出现的浮点数上限
    if isinstance(value, int) or isinstance(value, float):
        if value > MAX_NUMBER:
            value = 0

    # 检查防止小数点位过多
    if isinstance(value, float):
        d = decimal.Decimal(str(value))
        if abs(d.as_tuple().exponent) > MAX_DECIMAL:
            value = round(value, ndigits=MAX_DECIMAL)

    return unicode(value)


#----------------------------------------------------------------------
def todayDate():
    """获取当前本机电脑时间的日期"""
    return datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)


#----------------------------------------------------------------------
def loadIconPath(iconName):
    """加载程序图标路径"""
    global iconPathDict
    return iconPathDict.get(iconName, '')


def load_json_path(json_name, module_path):
    """加载json配置"""
    global jsonPathDict
    return jsonPathDict.get(json_name, '')

#----------------------------------------------------------------------


def getTempPath(name):
    """获取存放临时文件的路径"""
    tempPath = os.path.join(os.getcwd(), 'temp')
    if not os.path.exists(tempPath):
        os.makedirs(tempPath)

    path = os.path.join(tempPath, name)
    return path


#----------------------------------------------------------------------

# 图标路径
iconPathDict = {}

path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'ico')
#path = os.path.join(os.path.dirname(os.getcwd()), 'ico')
for root, subdirs, files in os.walk(path):
    for fileName in files:
        if '.ico' in fileName:
            iconPathDict[fileName] = os.path.join(root, fileName)


# JSON配置文件路径
jsonPathDict = {}

path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config')
#path = os.path.join(os.path.dirname(os.getcwd()), 'config')
for root, subdirs, files in os.walk(path):
    for fileName in files:
        if '.json' in fileName:
            jsonPathDict[fileName] = os.path.join(root, fileName)


# 读取全局配置
settingFileName = "VT_setting.json"
settingFilePath = load_json_path(settingFileName,__file__)

globalSetting = {}      # 全局配置字典
with open(settingFilePath, 'r') as f:
    globalSetting = json.load(f)
