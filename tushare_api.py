#!/usr/bin/env python
# coding:utf-8

"""
function: 转换tushare的函数接口，封装成统一的名字，获取数据
@author: zkang kai
@contact: 474918208@qq.com
"""

import tushare as ts


def get_hist_data_from_tushare(
        code=None,
        start=None,
        end=None,
        ktype='D',
        retry_count=3,
        pause=0.001):
    """
        获取个股历史交易记录
    Parameters
    ------
      code:string
                  股票代码 e.g. 600848
      start:string
                  开始日期 format：YYYY-MM-DD 为空时取到API所提供的最早日期数据
      end:string
                  结束日期 format：YYYY-MM-DD 为空时取到最近一个交易日数据
      ktype：string
                  数据类型，D=日k线 W=周 M=月 5=5分钟 15=15分钟 30=30分钟 60=60分钟，默认为D
      retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数
      pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
    return
    -------
      DataFrame
          属性:日期 ，开盘价， 最高价， 收盘价， 最低价， 成交量， 价格变动 ，涨跌幅，5日均价，10日均价，20日均价，5日均量，10日均量，20日均量，换手率
    """
    return ts.get_hist_data(code, start, end, ktype, retry_count, pause)


def get_tick_data_from_tushre(
        code=None,
        date=None,
        retry_count=3,
        pause=0.001,
        src='sn'):
    """
        获取分笔数据
    Parameters
    ------
        code:string
                  股票代码 e.g. 600848
        date:string
                  日期 format: YYYY-MM-DD
        retry_count : int, 默认 3
                  如遇网络等问题重复执行的次数
        pause : int, 默认 0
                 重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
        src : 数据源选择，可输入sn(新浪)、tt(腾讯)、nt(网易)，默认sn
     return
     -------
        DataFrame 当日所有股票交易数据(DataFrame)
              属性:成交时间、成交价格、价格变动，成交手、成交金额(元)，买卖类型
    """
    return ts.get_tick_data(code, date, retry_count, pause, src)


def get_sina_dd_from_tushare(
        code=None,
        date=None,
        vol=400,
        retry_count=3,
        pause=0.001):
    """
        获取sina大单数据
    Parameters
    ------
        code:string
                  股票代码 e.g. 600848
        date:string
                  日期 format：YYYY-MM-DD
        retry_count : int, 默认 3
                  如遇网络等问题重复执行的次数
        pause : int, 默认 0
                 重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
     return
     -------
        DataFrame 当日所有股票交易数据(DataFrame)
              属性:股票代码    股票名称    交易时间    价格    成交量    前一笔价格    类型（买、卖、中性盘）
    """
    return ts.get_sina_dd(code, date, vol, retry_count, pause)


def get_today_ticks_from_tushare(code=None, retry_count=3, pause=0.001):
    """
        获取当日分笔明细数据
    Parameters
    ------
        code:string
                  股票代码 e.g. 600848
        retry_count : int, 默认 3
                  如遇网络等问题重复执行的次数
        pause : int, 默认 0
                 重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
     return
     -------
        DataFrame 当日所有股票交易数据(DataFrame)
              属性:成交时间、成交价格、价格变动，成交手、成交金额(元)，买卖类型
    """
    return ts.get_today_ticks(code, retry_count, pause)


def get_today_all_from_tushare():
    """
        一次性获取最近一个日交易日所有股票的交易数据
    return
    -------
      DataFrame
           属性：代码，名称，涨跌幅，现价，开盘价，最高价，最低价，最日收盘价，成交量，换手率，成交额，市盈率，市净率，总市值，流通市值
    """
    return ts.get_today_all()


def get_realtime_quotes_from_tushare(symbols=None):
    """
        获取实时交易数据 getting real time quotes data
       用于跟踪交易情况（本次执行的结果-上一次执行的数据）
    Parameters
    ------
        symbols : string, array-like object (list, tuple, Series).

    return
    -------
        DataFrame 实时交易数据
              属性:0：name，股票名字
            1：open，今日开盘价
            2：pre_close，昨日收盘价
            3：price，当前价格
            4：high，今日最高价
            5：low，今日最低价
            6：bid，竞买价，即“买一”报价
            7：ask，竞卖价，即“卖一”报价
            8：volumn，成交量 maybe you need do volumn/100
            9：amount，成交金额（元 CNY）
            10：b1_v，委买一（笔数 bid volume）
            11：b1_p，委买一（价格 bid price）
            12：b2_v，“买二”
            13：b2_p，“买二”
            14：b3_v，“买三”
            15：b3_p，“买三”
            16：b4_v，“买四”
            17：b4_p，“买四”
            18：b5_v，“买五”
            19：b5_p，“买五”
            20：a1_v，委卖一（笔数 ask volume）
            21：a1_p，委卖一（价格 ask price）
            ...
            30：date，日期；
            31：time，时间；
    """
    return ts.get_realtime_quotes(symbols)


def get_h_data_from_tushare(
        code,
        start=None,
        end=None,
        autype='qfq',
        index=False,
        retry_count=3,
        pause=0.001,
        drop_factor=True):
    '''
    获取历史复权数据
    Parameters
    ------
      code:string
                  股票代码 e.g. 600848
      start:string
                  开始日期 format：YYYY-MM-DD 为空时取当前日期
      end:string
                  结束日期 format：YYYY-MM-DD 为空时取去年今日
      autype:string
                  复权类型，qfq-前复权 hfq-后复权 None-不复权，默认为qfq
      retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数
      pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
      drop_factor : bool, 默认 True
                是否移除复权因子，在分析过程中可能复权因子意义不大，但是如需要先储存到数据库之后再分析的话，有该项目会更加灵活
    return
    -------
      DataFrame
          date 交易日期 (index)
          open 开盘价
          high  最高价
          close 收盘价
          low 最低价
          volume 成交量
          amount 成交金额
    '''
    return ts.get_h_data(
        code,
        start,
        end,
        autype,
        index,
        retry_count,
        pause,
        drop_factor)


def get_index_from_tushare():
    """
    获取大盘指数行情
    return
    -------
      DataFrame
          code:指数代码
          name:指数名称
          change:涨跌幅
          open:开盘价
          preclose:昨日收盘价
          close:收盘价
          high:最高价
          low:最低价
          volume:成交量(手)
          amount:成交金额（亿元）
    """
    return ts.get_index()


def get_k_data_from_tushare(
        code=None,
        start='',
        end='',
        ktype='D',
        autype='qfq',
        index=False,
        retry_count=3,
        pause=0.001):
    """
    获取k线数据
    ---------
    Parameters:
      code:string
                  股票代码 e.g. 600848
      start:string
                  开始日期 format：YYYY-MM-DD 为空时取上市首日
      end:string
                  结束日期 format：YYYY-MM-DD 为空时取最近一个交易日
      autype:string
                  复权类型，qfq-前复权 hfq-后复权 None-不复权，默认为qfq
      ktype：string
                  数据类型，D=日k线 W=周 M=月 5=5分钟 15=15分钟 30=30分钟 60=60分钟，默认为D
      retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数
      pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
    return
    -------
      DataFrame
          date 交易日期 (index)
          open 开盘价
          high  最高价
          close 收盘价
          low 最低价
          volume 成交量
          amount 成交额
          turnoverratio 换手率
          code 股票代码
    """
    return ts.get_k_data(
        code,
        start,
        end,
        ktype,
        autype,
        index,
        retry_count,
        pause)


def get_hists_from_tushare(
        symbols,
        start=None,
        end=None,
        ktype='D',
        retry_count=3,
        pause=0.001):
    """
    批量获取历史行情数据，具体参数和返回数据类型请参考get_hist_data接口
    """
    return ts.get_hists(symbols, start, end, ktype, retry_count, pause)


def get_day_all_from_tushare(date=None):
    """
    获取每日收盘行情
    Parameters:
    -------------
    date:交易日期，格式:YYYY-MM-DD

    Return:
    -------------
    DataFrame
    code 代码, name 名称, p_change 涨幅%,
    price 现价, change 涨跌, open 今开, high 最高,
    low 最低, preprice 昨收, pe 市盈(动),
    volratio 量比, turnover 换手%, range 振幅%%,
    volume 总量, selling 内盘, buying 外盘,
    amount 总金额, totals 总股本(万), industry 细分行业,
    area 地区, floats 流通股本(万), fvalues 流通市值,
    abvalues AB股总市值, avgprice 均价, strength 强弱度%,
    activity 活跃度, avgturnover 笔换手, attack 攻击波%,
    interval3 近3月涨幅 ，interval 近6月涨幅
    """
    return ts.get_day_all(date)


def bar_from_tushare(
        code,
        conn=None,
        start_date=None,
        end_date=None,
        freq='D',
        asset='E',
        market='',
        adj=None,
        ma=[],
        factors=[],
        retry_count=3):
    """
    BAR数据
    Parameters:
    ------------
    code:证券代码，支持股票,ETF/LOF,期货/期权,港股
    con:服务器连接 ，通过ts.api()或者ts.xpi()获得
    start_date:开始日期  YYYY-MM-DD/YYYYMMDD
    end_date:结束日期 YYYY-MM-DD/YYYYMMDD
    freq:支持1/5/15/30/60分钟,周/月/季/年
    asset:证券类型 E:股票和交易所基金，INDEX:沪深指数,X:期货/期权/港股/中概美国/中证指数/国际指数
    market:市场代码，通过ts.get_markets()获取
    adj:复权类型,None不复权,qfq:前复权,hfq:后复权
    ma:均线,支持自定义均线频度，如：ma5/ma10/ma20/ma60/maN
    factors因子数据，目前支持以下两种：
        vr:量比,默认不返回，返回需指定：factor=['vr']
        tor:换手率，默认不返回，返回需指定：factor=['tor']
                    以上两种都需要：factor=['vr', 'tor']
    retry_count:网络重试次数

    Return
    ----------
    DataFrame
    code:代码
    open：开盘close/high/low/vol成交量/amount成交额/maN均价/vr量比/tor换手率

         期货(asset='X')
    code/open/close/high/low/avg_price：均价  position：持仓量  vol：成交总量
    """
    return ts.bar(
        code,
        conn,
        start_date,
        end_date,
        freq,
        asset,
        market,
        adj,
        ma,
        factors,
        retry_count)


def tick_from_tushare(
        code,
        conn=None,
        date='',
        asset='E',
        market='',
        retry_count=3):
    """
    tick数据
    Parameters:
    ------------
    code:证券代码，支持股票,ETF/LOF,期货/期权,港股
    conn:服务器连接 ，通过ts.api()或者ts.xpi()获得
    date:日期
    asset:证券品种，E:沪深交易所股票和基金, INDEX:沪深交易所指数， X:其他证券品种，大致如下：
                     支持的扩展行情包括(asset='X')：
                            郑州商品期权         OZ 大连商品期权         OD 上海商品期权         OS
                            上海个股期权         QQ 香港指数         FH 郑州商品         QZ 大连商品         QD 上海期货         QS
                            香港主板         KH 香港权证         KR 开放式基金         FU 货币型基金         FB
                            招商理财产品         LC 招商货币产品         LB 国际指数         FW 国内宏观指标         HG 中国概念股         CH
                            美股知名公司         MG B股转H股         HB 股份转让         SB 股指期货         CZ 香港创业板         KG 香港信托基金         KT
                             国债预发行         GY 主力期货合约         MA
                              中证指数         ZZ 港股通         GH
    market:市场代码，通过ts.get_markets()获取

    Return
    ----------
    DataFrame
    date:日期
    time:时间
    price:成交价
    vol:成交量
    type:买卖方向，0-买入 1-卖出 2-集合竞价成交
            期货  0:开仓  1:多开   -1:空开
         期货多一列数据oi_change:增仓数据

    """
    return ts.tick(code, conn, date, asset, market, retry_count)


def quotes_from_tushare(
        symbols,
        conn=None,
        asset='E',
        market=[],
        retry_count=3):
    """
        获取实时快照
    Parameters
    ------
        symbols : string, array-like object (list, tuple, Series).

    return
    -------
        DataFrame 实时快照，5档行情
    """
    return ts.quotes(symbols, conn, asset, market, retry_count)


def reset_instrument_from_tushare(xapi=None):
    """
            重新设置本地证券列表
    """
    return ts.reset_instrument(xapi)


def get_instrument_from_tushare(xapi=None):
    """
            获取证券列表
    """
    return ts.get_instrument(xapi)


def get_markets_from_tushare(xapi=None):
    """
            获取市场代码
    """
    return ts.get_markets(xapi)


def get_stock_basics(date=None):
    """
        获取沪深上市公司基本情况
    Parameters
    date:日期YYYY-MM-DD，默认为上一个交易日，目前只能提供2016-08-09之后的历史数据

    Return
    --------
    DataFrame
               code,代码
               name,名称
               industry,细分行业
               area,地区
               pe,市盈率
               outstanding,流通股本
               totals,总股本(万)
               totalAssets,总资产(万)
               liquidAssets,流动资产
               fixedAssets,固定资产
               reserved,公积金
               reservedPerShare,每股公积金
               eps,每股收益
               bvps,每股净资
               pb,市净率
               timeToMarket,上市日期
    """
    pass


def get_report_data(year, quarter):
    """
        获取业绩报表数据
    Parameters
    --------
    year:int 年度 e.g:2014
    quarter:int 季度 :1、2、3、4，只能输入这4个季度
       说明：由于是从网站获取的数据，需要一页页抓取，速度取决于您当前网络速度
       
    Return
    --------
    DataFrame
        code,代码
        name,名称
        eps,每股收益
        eps_yoy,每股收益同比(%)
        bvps,每股净资产
        roe,净资产收益率(%)
        epcf,每股现金流量(元)
        net_profits,净利润(万元)
        profits_yoy,净利润同比(%)
        distrib,分配方案
        report_date,发布日期
    """
    pass



def get_profit_data(year, quarter):
    """
        获取盈利能力数据
    Parameters
    --------
    year:int 年度 e.g:2014
    quarter:int 季度 :1、2、3、4，只能输入这4个季度
       说明：由于是从网站获取的数据，需要一页页抓取，速度取决于您当前网络速度
       
    Return
    --------
    DataFrame
        code,代码
        name,名称
        roe,净资产收益率(%)
        net_profit_ratio,净利率(%)
        gross_profit_rate,毛利率(%)
        net_profits,净利润(万元)
        eps,每股收益
        business_income,营业收入(百万元)
        bips,每股主营业务收入(元)
    """
    pass


def get_operation_data(year, quarter):
    """
        获取营运能力数据
    Parameters
    --------
    year:int 年度 e.g:2014
    quarter:int 季度 :1、2、3、4，只能输入这4个季度
       说明：由于是从网站获取的数据，需要一页页抓取，速度取决于您当前网络速度
       
    Return
    --------
    DataFrame
        code,代码
        name,名称
        arturnover,应收账款周转率(次)
        arturndays,应收账款周转天数(天)
        inventory_turnover,存货周转率(次)
        inventory_days,存货周转天数(天)
        currentasset_turnover,流动资产周转率(次)
        currentasset_days,流动资产周转天数(天)
    """
    pass


def get_growth_data(year, quarter):
    """
        获取成长能力数据
    Parameters
    --------
    year:int 年度 e.g:2014
    quarter:int 季度 :1、2、3、4，只能输入这4个季度
       说明：由于是从网站获取的数据，需要一页页抓取，速度取决于您当前网络速度
       
    Return
    --------
    DataFrame
        code,代码
        name,名称
        mbrg,主营业务收入增长率(%)
        nprg,净利润增长率(%)
        nav,净资产增长率
        targ,总资产增长率
        epsg,每股收益增长率
        seg,股东权益增长率
    """
    pass


def get_debtpaying_data(year, quarter):
    """
        获取偿债能力数据
    Parameters
    --------
    year:int 年度 e.g:2014
    quarter:int 季度 :1、2、3、4，只能输入这4个季度
       说明：由于是从网站获取的数据，需要一页页抓取，速度取决于您当前网络速度
       
    Return
    --------
    DataFrame
        code,代码
        name,名称
        currentratio,流动比率
        quickratio,速动比率
        cashratio,现金比率
        icratio,利息支付倍数
        sheqratio,股东权益比率
        adratio,股东权益增长率
    """
    pass
 
def get_cashflow_data(year, quarter):
    """
        获取现金流量数据
    Parameters
    --------
    year:int 年度 e.g:2014
    quarter:int 季度 :1、2、3、4，只能输入这4个季度
       说明：由于是从网站获取的数据，需要一页页抓取，速度取决于您当前网络速度
       
    Return
    --------
    DataFrame
        code,代码
        name,名称
        cf_sales,经营现金净流量对销售收入比率
        rateofreturn,资产的经营现金流量回报率
        cf_nm,经营现金净流量与净利润的比率
        cf_liabilities,经营现金净流量对负债比率
        cashflowratio,现金流量比率
    """
    pass 

def get_balance_sheet(code):
    """
        获取某股票的历史所有时期资产负债表
    Parameters
    --------
    code:str 股票代码 e.g:600518
       
    Return
    --------
    DataFrame
        行列名称为中文且数目较多，建议获取数据后保存到本地查看
    """
    pass

def get_profit_statement(code):
    """
        获取某股票的历史所有时期利润表
    Parameters
    --------
    code:str 股票代码 e.g:600518
       
    Return
    --------
    DataFrame
        行列名称为中文且数目较多，建议获取数据后保存到本地查看
    """
    pass
      
def get_cash_flow(code):
    """
        获取某股票的历史所有时期现金流表
    Parameters
    --------
    code:str 股票代码 e.g:600518
       
    Return
    --------
    DataFrame
        行列名称为中文且数目较多，建议获取数据后保存到本地查看
    """
    pass


"""
宏观经济数据接口 
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
"""
def get_gdp_year():
    """
        获取年度国内生产总值数据
    Return
    --------
    DataFrame
        year :统计年度
        gdp :国内生产总值(亿元)
        pc_gdp :人均国内生产总值(元)
        gnp :国民生产总值(亿元)
        pi :第一产业(亿元)
        si :第二产业(亿元)
        industry :工业(亿元)
        cons_industry :建筑业(亿元)
        ti :第三产业(亿元)
        trans_industry :交通运输仓储邮电通信业(亿元)
        lbdy :批发零售贸易及餐饮业(亿元)
    """
    pass
  
def get_gdp_quarter():
    """
        获取季度国内生产总值数据
    Return
    --------
    DataFrame
        quarter :季度
        gdp :国内生产总值(亿元)
        gdp_yoy :国内生产总值同比增长(%)
        pi :第一产业增加值(亿元)
        pi_yoy:第一产业增加值同比增长(%)
        si :第二产业增加值(亿元)
        si_yoy :第二产业增加值同比增长(%)
        ti :第三产业增加值(亿元)
        ti_yoy :第三产业增加值同比增长(%)
    """
    pass

def get_gdp_for():
    """
        获取三大需求对GDP贡献数据
    Return
    --------
    DataFrame
        year :统计年度
        end_for :最终消费支出贡献率(%)
        for_rate :最终消费支出拉动(百分点)
        asset_for :资本形成总额贡献率(%)
        asset_rate:资本形成总额拉动(百分点)
        goods_for :货物和服务净出口贡献率(%)
        goods_rate :货物和服务净出口拉动(百分点)
    """
    pass

def get_gdp_pull():
    """
        获取三大产业对GDP拉动数据
    Return
    --------
    DataFrame
        year :统计年度
        gdp_yoy :国内生产总值同比增长(%)
        pi :第一产业拉动率(%)
        si :第二产业拉动率(%)
        industry:其中工业拉动(%)
        ti :第三产业拉动率(%)
    """
    pass

def get_gdp_contrib():
    """
        获取三大产业贡献率数据
    Return
    --------
    DataFrame
        year :统计年度
        gdp_yoy :国内生产总值
        pi :第一产业献率(%)
        si :第二产业献率(%)
        industry:其中工业献率(%)
        ti :第三产业献率(%)
    """
    pass


def get_cpi():
    """
        获取居民消费价格指数数据
    Return
    --------
    DataFrame
        month :统计月份
        cpi :价格指数
    """
    pass

def get_ppi():
    """
        获取工业品出厂价格指数数据
    Return
    --------
    DataFrame
        month :统计月份
        ppiip :工业品出厂价格指数
        ppi :生产资料价格指数
        qm:采掘工业价格指数
        rmi:原材料工业价格指数
        pi:加工工业价格指数    
        cg:生活资料价格指数
        food:食品类价格指数
        clothing:衣着类价格指数
        roeu:一般日用品价格指数
        dcg:耐用消费品价格指数
    """
    pass


def get_deposit_rate():
    """
        获取存款利率数据
    Return
    --------
    DataFrame
        date :变动日期
        deposit_type :存款种类
        rate:利率（%）
    """
    pass


def get_loan_rate():
    """
        获取贷款利率数据
    Return
    --------
    DataFrame
        date :执行日期
        loan_type :存款种类
        rate:利率（%）
    """
    pass


def get_rrr():
    """
        获取存款准备金率数据
    Return
    --------
    DataFrame
        date :变动日期
        before :调整前存款准备金率(%)
        now:调整后存款准备金率(%)
        changed:调整幅度(%)
    """
    pass

def get_money_supply():
    """
        获取货币供应量数据
    Return
    --------
    DataFrame
        month :统计时间
        m2 :货币和准货币（广义货币M2）(亿元)
        m2_yoy:货币和准货币（广义货币M2）同比增长(%)
        m1:货币(狭义货币M1)(亿元)
        m1_yoy:货币(狭义货币M1)同比增长(%)
        m0:流通中现金(M0)(亿元)
        m0_yoy:流通中现金(M0)同比增长(%)
        cd:活期存款(亿元)
        cd_yoy:活期存款同比增长(%)
        qm:准货币(亿元)
        qm_yoy:准货币同比增长(%)
        ftd:定期存款(亿元)
        ftd_yoy:定期存款同比增长(%)
        sd:储蓄存款(亿元)
        sd_yoy:储蓄存款同比增长(%)
        rests:其他存款(亿元)
        rests_yoy:其他存款同比增长(%)
    """
    pass

def get_money_supply_bal():
    """
        获取货币供应量(年底余额)数据
    Return
    --------
    DataFrame
        year :统计年度
        m2 :货币和准货币(亿元)
        m1:货币(亿元)
        m0:流通中现金(亿元)
        cd:活期存款(亿元)
        qm:准货币(亿元)
        ftd:定期存款(亿元)
        sd:储蓄存款(亿元)
        rests:其他存款(亿元)
    """
    pass

def get_gold_and_foreign_reserves():
    """
    获取外汇储备
    Returns
    -------
    DataFrame
        month :统计时间
        gold:黄金储备(万盎司)
        foreign_reserves:外汇储备(亿美元)
    """
    pass



"""
获取股票分类数据接口 
Created on 2015/02/01
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
"""

def get_industry_classified(standard='sina'):
    """
        获取行业分类数据
    Parameters
    ----------
    standard
    sina:新浪行业 sw：申万 行业
    
    Returns
    -------
    DataFrame
        code :股票代码
        name :股票名称
        c_name :行业名称
    """
    pass

def get_concept_classified():
    """
        获取概念分类数据
    Return
    --------
    DataFrame
        code :股票代码
        name :股票名称
        c_name :概念名称
    """
    pass

def get_area_classified():
    """
        获取地域分类数据
    Return
    --------
    DataFrame
        code :股票代码
        name :股票名称
        area :地域名称
    """
    pass

def get_gem_classified():
    """
        获取创业板股票
    Return
    --------
    DataFrame
        code :股票代码
        name :股票名称
    """
   pass 

def get_sme_classified():
    """
        获取中小板股票
    Return
    --------
    DataFrame
        code :股票代码
        name :股票名称
    """
    pass


def get_st_classified():
    """
        获取风险警示板股票
    Return
    --------
    DataFrame
        code :股票代码
        name :股票名称
    """
    pass


def get_hs300s():
    """
    获取沪深300当前成份股及所占权重
    Return
    --------
    DataFrame
        code :股票代码
        name :股票名称
        date :日期
        weight:权重
    """
    pass

def get_sz50s():
    """
    获取上证50成份股
    Return
    --------
    DataFrame
        code :股票代码
        name :股票名称
    """
    pass

def get_zz500s():
    """
    获取中证500成份股
    Return
    --------
    DataFrame
        code :股票代码
        name :股票名称
    """
    pass

def get_terminated():
    """
    获取终止上市股票列表
    Return
    --------
    DataFrame
        code :股票代码
        name :股票名称
        oDate:上市日期
        tDate:终止上市日期 
    """
    pass

def get_suspended():
    """
    获取暂停上市股票列表
    Return
    --------
    DataFrame
        code :股票代码
        name :股票名称
        oDate:上市日期
        tDate:终止上市日期 
    """
    pass


"""
新闻事件数据接口 
Created on 2015/02/07
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
"""

def get_latest_news(top=None, show_content=False):
    """
        获取即时财经新闻
    
    Parameters
    --------
        top:数值，显示最新消息的条数，默认为80条
        show_content:是否显示新闻内容，默认False
    
    Return
    --------
        DataFrame
            classify :新闻类别
            title :新闻标题
            time :发布时间
            url :新闻链接
            content:新闻内容（在show_content为True的情况下出现）
    """
    pass


def latest_content(url):
    '''
        获取即时财经新闻内容
    Parameter
    --------
        url:新闻链接
    
    Return
    --------
        string:返回新闻的文字内容
    '''
    pass


def get_notices(code=None, date=None):
    '''
    个股信息地雷
    Parameters
    --------
        code:股票代码
        date:信息公布日期
    
    Return
    --------
        DataFrame，属性列表：
        title:信息标题
        type:信息类型
        date:公告日期
        url:信息内容URL
    '''
    pass


def notice_content(url):
    '''
        获取信息地雷内容
    Parameter
    --------
        url:内容链接
    
    Return
    --------
        string:信息内容
    '''
    pass
    

def guba_sina(show_content=False):
    """
       获取sina财经股吧首页的重点消息
    Parameter
    --------
        show_content:是否显示内容，默认False
    
    Return
    --------
    DataFrame
        title, 消息标题
        content, 消息内容（show_content=True的情况下）
        ptime, 发布时间
        rcounts,阅读次数
    """
    pass



"""
投资参考数据接口 
Created on 2015/03/21
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
"""

def profit_data(year=2017, top=25, 
              retry_count=3, pause=0.001):
    """
    获取分配预案数据
    Parameters
    --------
    year:年份
    top:取最新n条数据，默认取最近公布的25条
    retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数 
      pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
    
    returns
    -------
    DataFrame
    code:股票代码
    name:股票名称
    year:分配年份
    report_date:公布日期
    divi:分红金额（每10股）
    shares:转增和送股数（每10股）
    """
    pass


def profit_divis():
        '''
                        获取分送送股数据
            -------
            Return:DataFrame
                code:代码    
                name:证券简称    
                year:分配年度    
                bshares:送股  
                incshares:转增股
                totals:送转总数 
                cash:派现   
                plandate:预案公布日    
                regdate:股权登记日    
                exdate:除权除息日    
                eventproc:事件进程 ,预案或实施
                anndate:公告日期
                
    '''
    pass


def forecast_data(year, quarter):
    """
        获取业绩预告数据
    Parameters
    --------
    year:int 年度 e.g:2014
    quarter:int 季度 :1、2、3、4，只能输入这4个季度
       说明：由于是从网站获取的数据，需要一页页抓取，速度取决于您当前网络速度
       
    Return
    --------
    DataFrame
        code,代码
        name,名称
        type,业绩变动类型【预增、预亏等】
        report_date,发布日期
        pre_eps,上年同期每股收益
        range,业绩变动范围
        
    """
   pass 


def xsg_data(year=None, month=None, 
            retry_count=3, pause=0.001):
    """
    获取限售股解禁数据
    Parameters
    --------
    year:年份,默认为当前年
    month:解禁月份，默认为当前月
    retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数 
    pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
    
    Return
    ------
    DataFrame
    code:股票代码
    name:名称
    date:解禁日期
    count:解禁数量（万股）
    ratio:占总盘比率
    """
    pass


def fund_holdings(year, quarter,
                  retry_count=3, pause=0.001):
    """
    获取基金持股数据
    Parameters
    --------
    year:年份e.g 2014
    quarter:季度（只能输入1，2，3，4这个四个数字）
    retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数 
    pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
    
    Return
    ------
    DataFrame
    code:股票代码
    name:名称
    date:报告日期
    nums:基金家数
    nlast:与上期相比（增加或减少了）
    count:基金持股数（万股）
    clast:与上期相比
    amount:基金持股市值
    ratio:占流通盘比率
    """
    pass 


def new_stocks(retry_count=3, pause=0.001):
    """
    获取新股上市数据
    Parameters
    --------
    retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数 
    pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
    
    Return
    ------
    DataFrame
    code:股票代码
    xcode:申购代码
    name:名称
    ipo_date:上网发行日期
    issue_date:上市日期
    amount:发行数量(万股)
    markets:上网发行数量(万股)
    price:发行价格(元)
    pe:发行市盈率
    limit:个人申购上限(万股)
    funds：募集资金(亿元)
    ballot:网上中签率(%)
    """
    pass



def new_cbonds(default=1, retry_count=3, pause=0.001):
    """
    获取可转债申购列表
    Parameters
    --------
    retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数 
    pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
    
    Return
    ------
    DataFrame
    bcode:债券代码
    bname:债券名称
    scode:股票代码
    sname:股票名称
    xcode:申购代码
    amount:发行总数(亿元)
    marketprice:最新市场价格
    convprice:转股价格
    firstdayprice:首日收盘价
    ipo_date:上网发行日期
    issue_date:上市日期
    ballot:中签率(%)
    return：打新收益率(%)
    perreturn:每中一股收益（万元）
    
    """
    pass


def sh_margins(start=None, end=None, retry_count=3, pause=0.001):
    """
    获取沪市融资融券数据列表
    Parameters
    --------
    start:string
                  开始日期 format：YYYY-MM-DD 为空时取去年今日
    end:string
                  结束日期 format：YYYY-MM-DD 为空时取当前日期
    retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数 
    pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
    
    Return
    ------
    DataFrame
    opDate:信用交易日期
    rzye:本日融资余额(元)
    rzmre: 本日融资买入额(元)
    rqyl: 本日融券余量
    rqylje: 本日融券余量金额(元)
    rqmcl: 本日融券卖出量
    rzrqjyzl:本日融资融券余额(元)
    """
    pass


def sh_margin_details(date='', symbol='', 
                      start='', end='',
                      retry_count=3, pause=0.001):
    """
    获取沪市融资融券明细列表
    Parameters
    --------
    date:string
                明细数据日期 format：YYYY-MM-DD 默认为空''
    symbol：string
                标的代码，6位数字e.g.600848，默认为空  
    start:string
                  开始日期 format：YYYY-MM-DD 默认为空''
    end:string
                  结束日期 format：YYYY-MM-DD 默认为空''
    retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数 
    pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
    
    Return
    ------
    DataFrame
    opDate:信用交易日期
    stockCode:标的证券代码
    securityAbbr:标的证券简称
    rzye:本日融资余额(元)
    rzmre: 本日融资买入额(元)
    rzche:本日融资偿还额(元)
    rqyl: 本日融券余量
    rqmcl: 本日融券卖出量
    rqchl: 本日融券偿还量
    """
    pass

def sz_margins(start=None, end=None, retry_count=3, pause=0.001):
    """
    获取深市融资融券数据列表
    Parameters
    --------
    start:string
                  开始日期 format：YYYY-MM-DD 默认为上一周的今天
    end:string
                  结束日期 format：YYYY-MM-DD 默认为今日
    retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数 
    pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
    
    Return
    ------
    DataFrame
    opDate:信用交易日期(index)
    rzmre: 融资买入额(元)
    rzye:融资余额(元)
    rqmcl: 融券卖出量
    rqyl: 融券余量
    rqye: 融券余量(元)
    rzrqye:融资融券余额(元)
    """
    pass


def sz_margin_details(date='', retry_count=3, pause=0.001):
    """
    获取深市融资融券明细列表
    Parameters
    --------
    date:string
                明细数据日期 format：YYYY-MM-DD 默认为空''
    retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数 
    pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
    
    Return
    ------
    DataFrame
    opDate:信用交易日期
    stockCode:标的证券代码
    securityAbbr:标的证券简称
    rzmre: 融资买入额(元)
    rzye:融资余额(元)
    rqmcl: 融券卖出量
    rqyl: 融券余量
    rqye: 融券余量(元)
    rzrqye:融资融券余额(元)
    """
    pass

def top10_holders(code=None, year=None, quarter=None, gdtype='0',
                  retry_count=3, pause=0.001):
    pass

def moneyflow_hsgt():
    """
    获取沪深港通资金流向
    return:
    DataFrame,单位: 百万元
    --------------
    date: 交易日期
    ggt_ss: 港股通(沪)
    ggt_sz: 港股通(深)
    hgt: 沪港通
    sgt: 深港通
    north_money: 北向资金流入
    south_money: 南向资金流入
    """
    pass

"""
上海银行间同业拆放利率（Shibor）数据接口
Created on 2014/07/31
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
"""

def shibor_data(year=None):
    """
    获取上海银行间同业拆放利率（Shibor）
    Parameters
    ------
      year:年份(int)
      
    Return
    ------
    date:日期
    ON:隔夜拆放利率
    1W:1周拆放利率
    2W:2周拆放利率
    1M:1个月拆放利率
    3M:3个月拆放利率
    6M:6个月拆放利率
    9M:9个月拆放利率
    1Y:1年拆放利率
    """
    pass


def shibor_quote_data(year=None):
    """
    获取Shibor银行报价数据
    Parameters
    ------
      year:年份(int)
      
    Return
    ------
    date:日期
    bank:报价银行名称
    ON:隔夜拆放利率
    ON_B:隔夜拆放买入价
    ON_A:隔夜拆放卖出价
    1W_B:1周买入
    1W_A:1周卖出
    2W_B:买入
    2W_A:卖出
    1M_B:买入
    1M_A:卖出
    3M_B:买入
    3M_A:卖出
    6M_B:买入
    6M_A:卖出
    9M_B:买入
    9M_A:卖出
    1Y_B:买入
    1Y_A:卖出
    """
    pass


def shibor_ma_data(year=None):
    """
    获取Shibor均值数据
    Parameters
    ------
      year:年份(int)
      
    Return
    ------
    date:日期
       其它分别为各周期5、10、20均价
    """
    pass

def lpr_data(year=None):
    """
    获取贷款基础利率（LPR）
    Parameters
    ------
      year:年份(int)
      
    Return
    ------
    date:日期
    1Y:1年贷款基础利率
    """
    pass 

def lpr_ma_data(year=None):
    """
    获取贷款基础利率均值数据
    Parameters
    ------
      year:年份(int)
      
    Return
    ------
    date:日期
    1Y_5:5日均值
    1Y_10:10日均值
    1Y_20:20日均值
    """
    pass

"""
龙虎榜数据
Created on 2015年6月10日
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
"""

def top_list(date = None, retry_count=3, pause=0.001):
    """
    获取每日龙虎榜列表
    Parameters
    --------
    date:string
                明细数据日期 format：YYYY-MM-DD 如果为空，返回最近一个交易日的数据
    retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数 
    pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
    
    Return
    ------
    DataFrame
        code：代码
        name ：名称
        pchange：涨跌幅     
        amount：龙虎榜成交额(万)
        buy：买入额(万)
        bratio：占总成交比例
        sell：卖出额(万)
        sratio ：占总成交比例
        reason：上榜原因
        date  ：日期
    """
    pass

def cap_tops(days= 5, retry_count= 3, pause= 0.001):
    """
    获取个股上榜统计数据
    Parameters
    --------
        days:int
                  天数，统计n天以来上榜次数，默认为5天，其余是10、30、60
        retry_count : int, 默认 3
                     如遇网络等问题重复执行的次数 
        pause : int, 默认 0
                    重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
    Return
    ------
    DataFrame
        code：代码
        name：名称
        count：上榜次数
        bamount：累积购买额(万)     
        samount：累积卖出额(万)
        net：净额(万)
        bcount：买入席位数
        scount：卖出席位数
    """
   pass 
    

def broker_tops(days= 5, retry_count= 3, pause= 0.001):
    """
    获取营业部上榜统计数据
    Parameters
    --------
    days:int
              天数，统计n天以来上榜次数，默认为5天，其余是10、30、60
    retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数 
    pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
    Return
    ---------
    broker：营业部名称
    count：上榜次数
    bamount：累积购买额(万)
    bcount：买入席位数
    samount：累积卖出额(万)
    scount：卖出席位数
    top3：买入前三股票
    """
    pass


def inst_tops(days= 5, retry_count= 3, pause= 0.001):
    """
    获取机构席位追踪统计数据
    Parameters
    --------
    days:int
              天数，统计n天以来上榜次数，默认为5天，其余是10、30、60
    retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数 
    pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
                
    Return
    --------
    code:代码
    name:名称
    bamount:累积买入额(万)
    bcount:买入次数
    samount:累积卖出额(万)
    scount:卖出次数
    net:净额(万)
    """
    pass 


def inst_detail(retry_count= 3, pause= 0.001):
    """
    获取最近一个交易日机构席位成交明细统计数据
    Parameters
    --------
    retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数 
    pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
                
    Return
    ----------
    code:股票代码
    name:股票名称     
    date:交易日期     
    bamount:机构席位买入额(万)     
    samount:机构席位卖出额(万)     
    type:类型
    """
    pass 



def trade_cal():
    '''
            交易日历
    isOpen=1是交易日，isOpen=0为休市
    '''
    pass

def is_holiday(date):
    '''
            判断是否为交易日，返回True or False
    '''
    pass 


"""
电影票房 
Created on 2015/12/24
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
"""

def realtime_boxoffice(retry_count=3,pause=0.001):
    """
    获取实时电影票房数据
    数据来源：EBOT艺恩票房智库
    Parameters
    ------
        retry_count : int, 默认 3
                  如遇网络等问题重复执行的次数
        pause : int, 默认 0
                 重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
     return
     -------
        DataFrame 
              BoxOffice     实时票房（万） 
              Irank         排名
              MovieName     影片名 
              boxPer        票房占比 （%）
              movieDay      上映天数
              sumBoxOffice  累计票房（万） 
              time          数据获取时间
    """
    pass

def day_boxoffice(date=None, retry_count=3, pause=0.001):
    """
    获取单日电影票房数据
    数据来源：EBOT艺恩票房智库
    Parameters
    ------
        date:日期，默认为上一日
        retry_count : int, 默认 3
                  如遇网络等问题重复执行的次数
        pause : int, 默认 0
                 重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
     return
     -------
        DataFrame 
              AvgPrice      平均票价
              AvpPeoPle     场均人次
              BoxOffice     单日票房（万）
              BoxOffice_Up  环比变化 （%）
              IRank         排名
              MovieDay      上映天数
              MovieName     影片名 
              SumBoxOffice  累计票房（万） 
              WomIndex      口碑指数 
    """
    pass

def month_boxoffice(date=None, retry_count=3, pause=0.001):
    """
    获取单月电影票房数据
    数据来源：EBOT艺恩票房智库
    Parameters
    ------
        date:日期，默认为上一月，格式YYYY-MM
        retry_count : int, 默认 3
                  如遇网络等问题重复执行的次数
        pause : int, 默认 0
                 重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
     return
     -------
        DataFrame 
              Irank         排名
              MovieName     电影名称
              WomIndex      口碑指数
              avgboxoffice  平均票价
              avgshowcount  场均人次
              box_pro       月度占比
              boxoffice     单月票房(万)     
              days          月内天数
              releaseTime   上映日期
    """
    pass

def day_cinema(date=None, retry_count=3, pause=0.001):
    """
        获取影院单日票房排行数据
        数据来源：EBOT艺恩票房智库
        Parameters
        ------
            date:日期，默认为上一日
            retry_count : int, 默认 3
                      如遇网络等问题重复执行的次数
            pause : int, 默认 0
                     重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
         return
         -------
            DataFrame 
                  Attendance         上座率
                  AvgPeople          场均人次
                  CinemaName         影院名称  
                  RowNum             排名
                  TodayAudienceCount 当日观众人数
                  TodayBox           当日票房
                  TodayShowCount     当日场次
                  price              场均票价（元）
    """
    pass


"""
获取基金净值数据接口 
Created on 2016/04/03
@author: leo
@group : lazytech
@contact: lazytech@sina.cn
"""
def get_nav_open(fund_type='all'):
    """
        获取开放型基金净值数据
    Parameters
    ------
        type:string
            开放基金类型:
                1. all 		所有开放基金
                2. equity	股票型开放基金
                3. mix 		混合型开放基金
                4. bond		债券型开放基金
                5. monetary	货币型开放基金
                6. qdii		QDII型开放基金
     return
     -------
        DataFrame
            开放型基金净值数据(DataFrame):
                symbol      基金代码
                sname       基金名称
                per_nav     单位净值
                total_nav   累计净值
                yesterday_nav  前一日净值
                nav_a       涨跌额
                nav_rate    增长率(%)
                nav_date    净值日期
                fund_manager 基金经理
                jjlx        基金类型
                jjzfe       基金总份额
    """
    pass

def get_nav_close(fund_type='all', sub_type='all'):
    """
        获取封闭型基金净值数据
    Parameters
    ------
        type:string
            封闭基金类型:
                1. all      所有封闭型基金
                2. fbqy     封闭-权益
                3. fbzq     封闭债券

        sub_type:string
            基金子类型:

                1. type=all sub_type无效
                2. type=fbqy 封闭-权益
                    *all    全部封闭权益
                    *ct     传统封基
                    *cx     创新封基

                3. type=fbzq  封闭债券
                    *all    全部封闭债券
                    *wj     稳健债券型
                    *jj     激进债券型
                    *cz     纯债债券型
     return
     -------
        DataFrame
            开放型基金净值数据(DataFrame):
                symbol      基金代码
                sname       基金名称
                per_nav     单位净值
                total_nav   累计净值
                nav_rate    增长率(%)
                discount_rate 折溢价率(%)
                nav_date    净值日期
                start_date  成立日期
                end_date    到期日期
                fund_manager 基金经理
                jjlx        基金类型
                jjzfe       基金总份额
    """
    pass

def get_nav_grading(fund_type='all', sub_type='all'):
    """
        获取分级子基金净值数据
    Parameters
    ------
        type:string
            封闭基金类型:
                1. all      所有分级基金
                2. fjgs     分级-固收
                3. fjgg     分级-杠杆

        sub_type:string
            基金子类型(type=all sub_type无效):
                *all    全部分级债券
                *wjzq   稳健债券型
                *czzq   纯债债券型
                *jjzq   激进债券型
                *gp     股票型
                *zs     指数型
     return
     -------
        DataFrame
            开放型基金净值数据(DataFrame):
                symbol      基金代码
                sname       基金名称
                per_nav     单位净值
                total_nav   累计净值
                nav_rate    增长率(%)
                discount_rate 折溢价率(%)
                nav_date    净值日期
                start_date  成立日期
                end_date    到期日期
                fund_manager 基金经理
                jjlx        基金类型
                jjzfe       基金总份额
    """
    pass

def get_nav_history(code, start=None, end=None, retry_count=3, pause=0.001, timeout=10):
    '''
    获取历史净值数据
    Parameters
    ------
      code:string
                  基金代码 e.g. 000001
      start:string
                  开始日期 format：YYYY-MM-DD 为空时取当前日期
      end:string
                  结束日期 format：YYYY-MM-DD 为空时取去年今日
      retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数
      pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
      timeout: int 默认 10s
                请求大量数据时的网络超时
    return
    -------
      DataFrame
          date 发布日期 (index)
          value 基金净值(股票/混合/QDII型基金) / 年华收益(货币/债券基金)
          total 累计净值(股票/混合/QDII型基金) / 万分收益(货币/债券基金)
          change 净值增长率(股票/混合/QDII型基金)
    '''
    pass

def get_fund_info(code):
    '''
    获取基金基本信息
    Parameters
    ------
      code:string
                  基金代码 e.g. 000001
    return
    -------
      DataFrame
          jjqc      基金全称
          jjjc      基金简称
          symbol    基金代码
          clrq      成立日期
          ssrq      上市日期
          xcr       存续期限
          ssdd      上市地点
          Type1Name 运作方式
          Type2Name 基金类型
          Type3Name 二级分类
          jjgm      基金规模(亿元)
          jjfe      基金总份额(亿份)
          jjltfe    上市流通份额(亿份)
          jjferq    基金份额日期
          quarter   上市季度
          glr       基金管理人
          tgr       基金托管人
    '''
    pass


'''
全球市场
Created on 2016/11/27
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
'''

def global_realtime(symbols=None):
    """
    全球实时指数
    """
    pass


'''
Created on 2017年06月04日
@author: debugo
@contact: me@debugo.com
'''

def get_cffex_daily(date = None):
    """
        获取中金所日交易数据
    Parameters
    ------
        date: 日期 format：YYYY-MM-DD 或 YYYYMMDD 或 datetime.date对象 为空时为当天
    Return
    -------
        DataFrame
            中金所日交易数据(DataFrame):
                symbol        合约代码
                date          日期
                open          开盘价
                high          最高价
                low          最低价
                close         收盘价
                volume        成交量
                open_interest   持仓量
                turnover      成交额
                settle        结算价
                pre_settle    前结算价
                variety       合约类别
        或 None(给定日期没有交易数据)
    """
    pass

def get_czce_daily(date=None, type="future"):
    """
        获取郑商所日交易数据
    Parameters
    ------
        date: 日期 format：YYYY-MM-DD 或 YYYYMMDD 或 datetime.date对象 为空时为当天
        type: 数据类型, 为'future'期货 或 'option'期权二者之一
    Return
    -------
        DataFrame
            郑商所每日期货交易数据:
                symbol        合约代码
                date          日期
                open          开盘价
                high          最高价
                low           最低价
                close         收盘价
                volume        成交量
                open_interest 持仓量
                turnover      成交额
                settle        结算价
                pre_settle    前结算价
                variety       合约类别
        或 
        DataFrame
           郑商所每日期权交易数据
                symbol        合约代码
                date          日期
                open          开盘价
                high          最高价
                low           最低价
                close         收盘价
                pre_settle      前结算价
                settle         结算价
                delta          对冲值  
                volume         成交量
                open_interest     持仓量
                oi_change       持仓变化
                turnover        成交额
                implied_volatility 隐含波动率
                exercise_volume   行权量
                variety        合约类别
        None(类型错误或给定日期没有交易数据)
    """
    pass

def get_shfe_vwap(date = None):
    """
        获取上期所日成交均价数据
    Parameters
    ------
        date: 日期 format：YYYY-MM-DD 或 YYYYMMDD 或 datetime.date对象 为空时为当天
    Return
    -------
        DataFrame
            郑商所日交易数据(DataFrame):
                symbol        合约代码
                date          日期
                time_range    vwap时段，分09:00-10:15和09:00-15:00两类
                vwap          加权平均成交均价
        或 None(给定日期没有数据)
    """    
    pass

def get_shfe_daily(date = None):
    """
        获取上期所日交易数据
    Parameters
    ------
        date: 日期 format：YYYY-MM-DD 或 YYYYMMDD 或 datetime.date对象 为空时为当天
    Return
    -------
        DataFrame
            上期所日交易数据(DataFrame):
                symbol        合约代码
                date          日期
                open          开盘价
                high          最高价
                low           最低价
                close         收盘价
                volume        成交量
                open_interest 持仓量
                turnover      成交额
                settle        结算价
                pre_settle     前结算价
                variety       合约类别
        或 None(给定日期没有交易数据)
    """    
    pass

def get_dce_daily(date = None, type="future", retries=0):
    """
        获取大连商品交易所日交易数据
    Parameters
    ------
        date: 日期 format：YYYY-MM-DD 或 YYYYMMDD 或 datetime.date对象 为空时为当天
        type: 数据类型, 为'future'期货 或 'option'期权二者之一
        retries: int, 当前重试次数，达到3次则获取数据失败
    Return
    -------
        DataFrame
            大商所日交易数据(DataFrame):
                symbol        合约代码
                date          日期
                open          开盘价
                high          最高价
                low           最低价
                close         收盘价
                volume        成交量
                open_interest   持仓量
                turnover       成交额
                settle        结算价
                pre_settle    前结算价
                variety       合约类别
        或 
        DataFrame
           郑商所每日期权交易数据
                symbol        合约代码
                date          日期
                open          开盘价
                high          最高价
                low           最低价
                close         收盘价
                pre_settle      前结算价
                settle         结算价
                delta          对冲值  
                volume         成交量
                open_interest     持仓量
                oi_change       持仓变化
                turnover        成交额
                implied_volatility 隐含波动率
                exercise_volume   行权量
                variety        合约类别
        或 None(给定日期没有交易数据)
    """
    pass

def get_future_daily(start = None, end = None, market = 'CFFEX'):
    """
        获取中金所日交易数据
    Parameters
    ------
        start: 开始日期 format：YYYY-MM-DD 或 YYYYMMDD 或 datetime.date对象 为空时为当天
        end: 结束数据 format：YYYY-MM-DD 或 YYYYMMDD 或 datetime.date对象 为空时为当天
        market: 'CFFEX' 中金所, 'CZCE' 郑商所,  'SHFE' 上期所, 'DCE' 大商所 之一。默认为中金所 
    Return
    -------
        DataFrame
            中金所日交易数据(DataFrame):
                symbol      合约代码
                date       日期
                open       开盘价
                high       最高价
                low       最低价
                close      收盘价
                volume      成交量
                open_interest 持仓量
                turnover    成交额
                settle     结算价
                pre_settle   前结算价
                variety     合约类别
        或 None(给定日期没有交易数据)
    """
    pass


def get_shfe_vwap(date = None):
    """
        获取上期所日成交均价数据
    Parameters
    ------
        date: 日期 format：YYYY-MM-DD 或 YYYYMMDD 或 datetime.date对象 为空时为当天
    Return
    -------
        DataFrame
            郑商所日交易数据(DataFrame):
                symbol        合约代码
                date          日期
                time_range    vwap时段，分09:00-10:15和09:00-15:00两类
                vwap          加权平均成交均价
        或 None(给定日期没有数据)
    """    
    pass



"""
数字货币行情数据
Created on 2017年9月9日
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
"""



def coins_tick(broker='hb', code='btc'):
    """
    实时tick行情
    params:
    ---------------
    broker: hb:火币
            ok:okCoin
            chbtc:中国比特币
    code: hb:btc,ltc
        ----okcoin---
        btc_cny：比特币    ltc_cny：莱特币    eth_cny :以太坊     etc_cny :以太经典    bcc_cny :比特现金 
        ----chbtc----
        btc_cny:BTC/CNY
        ltc_cny :LTC/CNY
        eth_cny :以太币/CNY
        etc_cny :ETC币/CNY
        bts_cny :BTS币/CNY
        eos_cny :EOS币/CNY
        bcc_cny :BCC币/CNY
        qtum_cny :量子链/CNY
        hsr_cny :HSR币/CNY
    return:json
    ---------------
    hb:
    {
    "time":"1504713534",
    "ticker":{
        "symbol":"btccny",
        "open":26010.90,
        "last":28789.00,
        "low":26000.00,
        "high":28810.00,
        "vol":17426.2198,
        "buy":28750.000000,
        "sell":28789.000000
        }
    }
    ok:
    {
    "date":"1504713864",
    "ticker":{
        "buy":"28743.0",
        "high":"28886.99",
        "last":"28743.0",
        "low":"26040.0",
        "sell":"28745.0",
        "vol":"20767.734"
        }
    }
    chbtc: 
        {
         u'date': u'1504794151878',
         u'ticker': {
             u'sell': u'28859.56', 
             u'buy': u'28822.89', 
             u'last': u'28859.56', 
             u'vol': u'2702.71', 
             u'high': u'29132', 
             u'low': u'27929'
         }
        }

        
    """
    pass 


def coins_bar(broker='hb', code='btc', ktype='D', size='2000'):
    """
            获取各类k线数据
    params:
    broker:hb,ok,chbtc
    code:btc,ltc,eth,etc,bcc
    ktype:D,W,M,1min,5min,15min,30min,60min
    size:<2000
    return DataFrame: 日期时间，开盘价，最高价，最低价，收盘价，成交量
    """
    pass

def coins_snapshot(broker='hb', code='btc', size='5'):
    """
            获取实时快照数据
    params:
    broker:hb,ok,chbtc
    code:btc,ltc,eth,etc,bcc
    size:<150
    return Panel: asks,bids
    """
    pass

def coins_trade(broker='hb', code='btc'):
    """
    获取实时交易数据
    params:
    -------------
    broker: hb,ok,chbtc
    code:btc,ltc,eth,etc,bcc
    
    return:
    ---------------
    DataFrame
    'tid':order id
    'datetime', date time 
    'price' : trade price
    'amount' : trade amount
    'type' : buy or sell
    """
    pass
