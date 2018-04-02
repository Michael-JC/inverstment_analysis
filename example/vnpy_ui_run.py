# encoding: UTF-8

# 重载sys模块，设置默认字符串编码方式为utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 判断操作系统
import platform
system = platform.system()

# vn.trader模块
from event import EventEngine
from trader.vtEngine import MainEngine
from ui.uiMainWindow import createQApp, MainWindow

# 加载底层接口
from gateway import (
    ctpGateway,
    oandaGateway,
    ibGateway,
    huobiGateway,
    okcoinGateway)

if system == 'Windows':
    from gateway import femasGateway, xspeedGateway

if system == 'Linux':
    from gateway import xtpGateway

# 加载上层应用
from app import (riskManager, ctaStrategy, spreadTrading, dataRecorder)

# ----------------------------------------------------------------------


def main():
    """主程序入口"""
    # 创建Qt应用对象
    qApp = createQApp()

    # 创建事件引擎
    ee = EventEngine()

    # 创建主引擎
    me = MainEngine(ee)

    # 添加交易接口
    me.addGateway(ctpGateway)
    me.addGateway(oandaGateway)
    me.addGateway(ibGateway)

    # 添加上层应用
    me.addApp(ctaStrategy)
    me.addApp(riskManager)
    me.addApp(spreadTrading)
    me.addApp(dataRecorder)

    # 创建主窗口
    mw = MainWindow(me, ee)
    mw.showMaximized()

    # 在主线程中启动Qt事件循环
    sys.exit(qApp.exec_())


if __name__ == '__main__':
    main()
