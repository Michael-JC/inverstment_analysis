# encoding: UTF-8

import json
import time
import datetime
import random

from pymongo import MongoClient, ASCENDING

from data.shcifco.vnshcifco import ShcifcoApi, PERIOD_1MIN
from trader.vtObject import VtBarData
from trader.app.ctaStrategy.ctaBase import MINUTE_DB_NAME


# 加载配置
config = open('.\config\shzq_data_config.json')
setting = json.load(config)

MONGO_HOST = setting['MONGO_HOST']
MONGO_PORT = setting['MONGO_PORT']
SHCIFCO_IP = setting['SHCIFCO_IP']
SHCIFCO_PORT = setting['SHCIFCO_PORT']
SHCIFCO_TOKEN = setting['SHCIFCO_TOKEN']
SYMBOLS = setting['SYMBOLS']

api = ShcifcoApi(SHCIFCO_IP, SHCIFCO_PORT, SHCIFCO_TOKEN)       # 历史行情服务API对象
mc = MongoClient(MONGO_HOST, MONGO_PORT)                        # Mongo连接
db = mc[MINUTE_DB_NAME]                                         # 数据库


#----------------------------------------------------------------------
def generateVtBar(d):
    """生成K线"""
    bar = VtBarData()

    bar.symbol = d['symbol']
    bar.vtSymbol = d['symbol']
    bar.date = d['date']
    bar.time = ':'.join([d['time'][:2], d['time'][2:]])
    bar.open = d['open']
    bar.high = d['high']
    bar.low = d['low']
    bar.close = d['close']
    bar.volume = d['volume']
    bar.openInterest = d['openInterest']
    bar.datetime = datetime.datetime.strptime(
        ' '.join([bar.date, bar.time]), '%Y%m%d %H:%M')

    return bar

#----------------------------------------------------------------------


def downMinuteBarBySymbol(symbol, num):
    """下载某一合约的分钟线数据"""
    start = time.time()

    cl = db[symbol]                                                 # 集合
    cl.ensure_index([('datetime', ASCENDING)], unique=True)         # 添加索引

    l = api.getHisBar(symbol, num, period=PERIOD_1MIN)
    if not l:
        print u'%s数据下载失败' % symbol
        return

    for d in l:
        bar = generateVtBar(d)
        d = bar.__dict__
        flt = {'datetime': bar.datetime}
        cl.replace_one(flt, d, True)

    end = time.time()
    cost = (end - start) * 1000

    print u'合约%s数据下载完成%s - %s，耗时%s毫秒' % (symbol, generateVtBar(l[0]).datetime,
                                         generateVtBar(l[-1]).datetime, cost)

#----------------------------------------------------------------------


def downloadAllMinuteBar(num):
    """下载所有配置中的合约的分钟线数据"""
    print '-' * 50
    print u'开始下载合约分钟线数据'
    print '-' * 50

    for symbol in SYMBOLS:
        downMinuteBarBySymbol(symbol, num)
        time.sleep(1)

    print '-' * 50
    print u'合约分钟线数据下载完成'
    print '-' * 50


def load_data_auto():
    taskCompletedDate = None

    # 生成一个随机的任务下载时间，用于避免所有用户在同一时间访问数据服务器
    taskTime = datetime.time(hour=17, minute=random.randint(1, 59))

    # 进入主循环
    while True:
        t = datetime.datetime.now()

        # 每天到达任务下载时间后，执行数据下载的操作
        if t.time() > taskTime and (
                taskCompletedDate is None or t.date() != taskCompletedDate):
            # 下载1000根分钟线数据，足以覆盖过去两天的行情
            downloadAllMinuteBar(1000)

            # 更新任务完成的日期
            taskCompletedDate = t.date()
        else:
            print u'当前时间%s，任务定时%s' % (t, taskTime)

        time.sleep(60)


def load_data_now():
    downloadAllMinuteBar(1000)


if __name__ == '__main__':
    load_data_now()
    # load_data_auto()
