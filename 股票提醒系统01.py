       
import tushare #股票提醒系统 要用到tushare模块，它是一个开源的python财经数据接口包 
import time
#获取股票数据，封装在一个函数里面
def getrealtimedata(share):		
	dataNow=tushare.get_realtime_quotes(share.code)
	share.name=dataNow.loc[0][0] #股票名，要提取下面的数据，name接收，用loc获取DataFrame这种数据类型,第一个中括号代表第几行，第二个中括号代表一行里面的第几个数据，和列表类似。
	share.price=float(dataNow.loc[0][3]) #当前价格
	share.high=dataNow.loc[0][4] #最高价
	share.low=dataNow.loc[0][5] #最低价
	share.volumn=dataNow.loc[0][8] #成交量,这是100股
	share.amount=dataNow.loc[0][9] #成交金额
	share.openToday=dataNow.loc[0][1] #当天开盘价
	share.pre_close=dataNow.loc[0][2] #昨日收盘价
	share.timee=dataNow.loc[0][30] #时间
	share.describe='股票名:'+share.name,'当前价格:'+str(share.price)#只提取股票名和当前价格
	return share

#设定一个股票的类，封装在一个类里面。
class Share():
	def __init__(self,code,buy,sale):
		self.name=''
		self.price=''
		self.high=''
		self.low=''
		self.volumn=''
		self.amount=''
		self.openToday=''
		self.pre_close=''
		self.timee=''
		self.describe=''
		self.code=code
		self.buy=buy
		self.sale=sale

def main(sharelist): 
	for share in sharelist:

		sss=getrealtimedata(share)#调用方法
		print(sss.describe)

		if sss.price<=sss.buy:
			print('达到买点,如果有钱,请赶紧买!')
		elif sss.price>=sss.sale:
			print('达到卖点,手里有货的话,赶紧卖!')
		else:
			print('别买,也别卖,等着!')

while True:#多只股票处理方法
	share1=Share('600106',5,6)#重庆路桥
	share2=Share('601988',3,3.8)#中国银行
	share3=Share('000591',9.82,10)#太阳能
	share4=Share('600519',1700,1800)#贵州茅台
	list1=[share1,share2,share3,share4]
	print('--------------------')
	main(list1)
	time.sleep(10)

