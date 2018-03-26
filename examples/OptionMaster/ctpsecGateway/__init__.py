# encoding: UTF-8

from trader import vtConstant
from trader.gateway.ctpGateway import CtpGateway

gatewayClass = CtpGateway
gatewayName = 'CTPSEC'
gatewayDisplayName = 'CTP证券'
gatewayType = vtConstant.GATEWAYTYPE_FUTURES
gatewayQryEnabled = True
