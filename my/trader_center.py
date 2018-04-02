#!/usr/bin/env python
# coding:utf-8

"""
function: 该类用来加载所有的可连接的gateway,提供对内统一的下单接口
@author: zkang kai
@contact: 474918208@qq.com
"""


class trader_center(object):
    """
    交易中心，策略下单或手动下单被调用，根据选择的参数进行路由下单
    """

    def __init__(self, eventEngine):
        """Constructor"""
        # 绑定事件引擎
        self.eventEngine = eventEngine
        self.eventEngine.start()

        # 接口实例
        self.gatewayDict = OrderedDict()
        self.gatewayDetailList = []

    #----------------------------------------------------------------------
    def addGateway(self, gatewayModule):
        """添加底层接口"""
        gatewayName = gatewayModule.gatewayName

        # 创建接口实例
        self.gatewayDict[gatewayName] = gatewayModule.gatewayClass(
            self.eventEngine, gatewayName)

        # 设置接口轮询
        if gatewayModule.gatewayQryEnabled:
            self.gatewayDict[gatewayName].setQryEnabled(
                gatewayModule.gatewayQryEnabled)

        # 保存接口详细信息
        d = {
            'gatewayName': gatewayModule.gatewayName,
            'gatewayDisplayName': gatewayModule.gatewayDisplayName,
            'gatewayType': gatewayModule.gatewayType
        }
        self.gatewayDetailList.append(d)

    #----------------------------------------------------------------------
    def getGateway(self, gatewayName):
        """获取接口"""
        if gatewayName in self.gatewayDict:
            return self.gatewayDict[gatewayName]
        else:
            # TODO: 增加对日志的处理
            # self.writeLog(vt_text.GATEWAY_NOT_EXIST.format(gateway=gatewayName))
            return None

    #----------------------------------------------------------------------
    def connect(self, gatewayName):
        """连接特定名称的接口"""
        gateway = self.getGateway(gatewayName)

        if gateway:
            gateway.connect()

    #----------------------------------------------------------------------
    def subscribe(self, subscribeReq, gatewayName):
        """订阅特定接口的行情"""
        gateway = self.getGateway(gatewayName)

        if gateway:
            gateway.subscribe(subscribeReq)

    #----------------------------------------------------------------------
    def sendOrder(self, orderReq, gatewayName):
        """对特定接口发单"""
        # TODO 如果创建了风控引擎，且风控检查失败则不发单 #if self.rmEngine and not self.rmEngine.checkRisk(orderReq, gatewayName):
        #    return ''

        gateway = self.getGateway(gatewayName)

        if gateway:
            vtOrderID = gateway.sendOrder(orderReq)
            return vtOrderID
        else:
            return ''

    #----------------------------------------------------------------------
    def cancelOrder(self, cancelOrderReq, gatewayName):
        """对特定接口撤单"""
        gateway = self.getGateway(gatewayName)

        if gateway:
            gateway.cancelOrder(cancelOrderReq)

    #----------------------------------------------------------------------
    def qryAccount(self, gatewayName):
        """查询特定接口的账户"""
        gateway = self.getGateway(gatewayName)

        if gateway:
            gateway.qryAccount()

    #----------------------------------------------------------------------
    def qryPosition(self, gatewayName):
        """查询特定接口的持仓"""
        gateway = self.getGateway(gatewayName)

        if gateway:
            gateway.qryPosition()

    #----------------------------------------------------------------------
    def exit(self):
        """退出程序前调用，保证正常退出"""
        # 安全关闭所有接口
        for gateway in self.gatewayDict.values():
            gateway.close()

        # 停止事件引擎
        self.eventEngine.stop()

    #----------------------------------------------------------------------
    def writeLog(self, content):
        """快速发出日志事件"""
        log = VtLogData()
        log.logContent = content
        log.gatewayName = 'MAIN_ENGINE'
        event = Event(type_=EVENT_LOG)
        event.dict_['data'] = log
        self.eventEngine.put(event)

    #----------------------------------------------------------------------
    def getOrder(self, vtOrderID):
        """查询委托"""
        return self.dataEngine.getOrder(vtOrderID)

    #----------------------------------------------------------------------
    def getAllWorkingOrders(self):
        """查询所有的活跃的委托（返回列表）"""
        return self.dataEngine.getAllWorkingOrders()

    #----------------------------------------------------------------------
    def getAllGatewayDetails(self):
        """查询引擎中所有底层接口的信息"""
        return self.gatewayDetailList
