# 此code 以jupyter codeing 

from pandas_datareader import data as pdr
import yfinance as yf # YahooHK 財經網拿資料
from datetime import datetime

# Output_1 將指定股票抓下呈現 numpy data
yf.pdr_override()
# y_symbols = ['2330.TW']  # 台積電代號
y_symbols = ['BTC-USD']   # Bit-coint 代號
start_date = datetime(2021,1,1)
end_date = datetime(2023,8,31)
df = pdr.get_data_yahoo(y_symbols,start=start_date,end=end_date)

# Output_1 以蠟燭圖顯示資料,以及交易量
import mplfinance as mpf
mpf.plot(df,type='candle',mav=(5,20,60),volume=True)
