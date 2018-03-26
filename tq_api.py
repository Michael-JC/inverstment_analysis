
# encoding: UTF-8

"""
对接天勤行情的网关接口，可以提供国内期货的报价/K线/Tick序列等数据的实时推送和历史仿真
使用时需要在本机先启动一个天勤终端进程
天勤行情终端: http://www.tq18.cn
"""


from time import sleep
import json
import threading
import tornado
from tornado import websocket
from sortedcontainers import SortedDict
from pymongo import MongoClient, ASCENDING

########################################################################


class TqApi(object):
    """天勤行情接口"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""

        self.client = None      # websocket客户端

    #----------------------------------------------------------------------
    def connect(self):
        """
        建立行情连接。
        """
        self.start()

        # 启动tornado的IO线程
        loop_thread = threading.Thread( target=lambda: tornado.ioloop.IOLoop.current().start())
        loop_thread.setDaemon(True)
        loop_thread.start()

    #----------------------------------------------------------------------
    def subscribe_quote(self, ins_list):
        """
        订阅实时行情.
        指定一个合约列表，订阅其实时报价信息
        每次调用此函数时，都会覆盖前一次的订阅设定，不在订阅列表里的合约，会停止行情推送
        :param ins_list: ins_list 是一个列表，列出全部需要实时行情的合约代码。
        :param callback_func (可选): callback_func 是一个回调函数，每当有报价数据变更时会触发。此函数应该接受一个参数 ins_id
        :example:
            订阅 cu1803,SR709,IF1709 这三个合约的报价:  subscribe_quote(["cu1803", ”SR709", "IF1709"])
        """
        req = {
            "aid": "subscribe_quote",
            "ins_list": ",".join(ins_list),
        }
        self.send_json(req)

    #----------------------------------------------------------------------
    def subscribe_chart(
            self,
            ins_id,
            duration_seconds,
            data_length=200):
        """
        订阅历史行情序列.
        订阅指定合约及周期的历史行情序列（K线数据序列或Tick数据序列），这些序列数据会持续推送
        :param ins_id: 合约代码，需注意大小写
        :param duration_seconds: 历史数据周期，以秒为单位。目前支持的周期包括：
                3秒，5秒，10秒，15秒，20秒，30秒，1分钟，2分钟，3分钟，5分钟，10分钟，15分钟，20分钟，30分钟，1小时，2小时，4小时，1日
                特别的，此值指定为0表示订阅tick序列。
        :param data_length: 需要获取的序列长度。每个序列最大支持请求 8964 个数据
        :param callback_func (可选): callback_func 是一个回调函数，每当序列数据变更时会触发。此函数应该接受2个参数 ins_id, duration_seconds
        :example:
            订阅 cu1803 的1分钟线： subscribe_chart("cu1803", 60)
            订阅 IF1709 的tick线： subscribe_chart("IF1709", 0)
        """
        chart_id = self._generate_chart_id(ins_id, duration_seconds)

        # 限制最大数据长度
        if data_length > 8964:
            data_length = 8964

        req = {
            "aid": "set_chart",
            "chart_id": chart_id,
            "ins_list": ins_id,
            "duration": duration_seconds * 1000000000,
            "view_width": data_length,
        }
        self.send_json(req)

    #----------------------------------------------------------------------
    @tornado.gen.coroutine
    def start(self):
        """启动websocket客户端"""
        self.client = yield tornado.websocket.websocket_connect(url="ws://127.0.0.1:7777/")

        # 协程式读取数据
        while True:
            msg = yield self.client.read_message()
            self.on_receive_msg(msg)

    #----------------------------------------------------------------------
    def send_json(self, obj):
        """发送JSON内容"""
        s = json.dumps(obj)

        # 如果已经创建了客户端则直接发出请求
        if self.client:
            self.client.write_message(s)
            print "send sub",s

    #----------------------------------------------------------------------
    def on_receive_msg(self, msg):
        """收到数据推送"""
        pack = json.loads(msg)
        l = pack.get("data",[])

        for price in l:
            for first_name,first_data in price.items():
                try:
                    if first_name == "ins_list":
                        pass
                        #db = mc["tq_ins_list"]
                        #if isinstance(first_data, dict):
                        #    cl.insert_one(data)
                    elif first_name == "quotes":
                        db = mc["tq_quotes"]
                        for second_name,second_data in first_data.items():
                            if second_name == "":
                                print "tq_quotes_name_null",second_data
                                continue
                            cl = db[second_name]
                            cl.insert_one(second_data)
                    elif first_name == "klines":
                        db = mc["tq_klines"]
                        for second_name, second_data in first_data.items():
                            if second_name == "":
                                print "tq_klines_name_null",second_data
                                continue
                            cl = db[second_name]
                            for third_name,third_data in second_data.items():
                                third_name = third_name / 1000000000
                                print "tq_line",third_data['last_id']
                                klines_data = third_data['data']
                                cl = db["tq_klines" + str(third_name)]
                                for one_klines_data in klines_data.values():
                                    cl.insert_one(one_klines_data)
                    elif first_name == "ticks":
                        db = mc["tq_ticks"]
                        for second_name, second_data in first_data.items():
                            if second_name == "":
                                print "tq_ticks_name_null",second_data
                                continue
                            cl = db[second_name]
                            print "tq_ticks" ,second_data['last_id']
                            ticks_data = second_data['data']
                            for one_ticks_data in ticks_data.values():
                                cl.insert_one(one_ticks_data)
                except Exception,e:
                    print e.message 

    #----------------------------------------------------------------------
    def _generate_chart_id(self, ins_id, duration_seconds):
        """生成图表编号"""
        chart_id = "VN_%s_%d" % (ins_id, duration_seconds)
        return chart_id


def insert_quotes_to_mongodb(price_data ={}):
    db = mc["tq_api_quotes"]
    for code,data in price_data.items():
        cl = db[code]
        cl.insert_one(data)

def insert_klines_to_mongodb(price_data ={}):
    db = mc["tq_api_klines"]
    for code,data in price_data.items():
        cl = db[code]
        cl.insert_one(data)

def insert_ticks_to_mongodb(price_data ={}):
    db = mc["tq_api_ticks"]
    for code,data in price_data.items():
        cl = db[code]
        cl.insert_one(data)

if __name__ == "__main__":
    mc = MongoClient("localhost",27017)
    db = mc["tq_api"]

    cl = db['log']
    cl.insert_one({'data':'this is a test'})

    api = TqApi()

    api.connect()

    # 订阅Tick推送
    api.subscribe_quote(["SHFE.cu1810","SHFE.cu1804"])

    # 订阅Tick图表
    while True:
        if api.client:
            api.subscribe_chart(["SHFE.cu1810","SHFE.cu1804"],60)
            break
        sleep(2)

    # 订阅K线图表
   # api.subscribe_chart(symbol, 60, 1000, onChart)

    raw_input()
