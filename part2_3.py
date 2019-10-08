import tushare as ts
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns',1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth',1000)

ts.set_token('f6affddf3196b99ed9bbfd53e5dc7b5bd29acebe5e5ed8d9e28eda84')

df = ts.get_hist_data(code='sh000001', start='2019-08-01', end='2019-08-31')
print(df)
# 收盘价均值
print('上证指数均值（收盘价）:'+ str(df["close"].mean()))
# 收盘价方差
print('上证指数方差（收盘价）:'+ str(df["close"].var()))
# 收盘价标准差
print('上证指数标准差（收盘价）:'+ str(df["close"].std()))
sns.set()
# 绘制收盘价曲线
#df.plot(y="close")
# 绘制收盘价柱状图
#df.plot(kind = 'bar',y="close")
# 绘制收盘价直方图
df['close'].plot.hist(stacked=True,bins=10,y="close")
# 绘制收盘价密度图
df['close'].plot.kde()
plt.show()