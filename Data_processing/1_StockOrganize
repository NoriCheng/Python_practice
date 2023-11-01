import mplfinance as mpf
df_2330_all=pd.DataFrame()
def 處理日期(x):
    x=str(int(x[0:3])+1911)+x[3:]
    return x
for n in range(7):
    file = fr'C:\Users\USER\Desktop\Python\2330\STOCK_DAY_2330_2023{n+1:02d}.csv'
    df_2330 = pd.read_csv(file,encoding="big5",header=1,skipfooter=6,engine='python',thousands=',')
    df_2330 = df_2330[['日期','開盤價','最高價','最低價','收盤價','成交股數']] \
                .rename(columns={'日期':'Date','開盤價':'Open',
                        '最高價':'High','最低價':'Low',
                        '收盤價':'Close','成交股數':'Volume'})
    # 將民國改成西元年
    df_2330["Date"]=df_2330["Date"].apply(處理日期)
#     df_2330["Date"]=df_2330["Date"].str.replace(\
#         df_2330.loc[0,"Date"][0:3],str(int(df_2330.loc[0,"Date"][0:3])+1911))
#    s_bool = df_2330["Date"].str.contains('\d{3}[/]\d{2}[/]\d{2}',regex=True)
    df_2330_all=pd.concat([df_2330_all,df_2330])
    
df_2330_all=df_2330_all.reset_index(drop=True) # 將列索引重新排序 0開始
df_2330_all=df_2330_all.set_index('Date')   # 指定 Date行 為 列索引
df_2330_all.index=pd.to_datetime(df_2330_all.index) # 轉換index dtypes 至 datetime dtypes
mpf.plot(df_2330_all,type='candle') # 繪製蠟燭圖
