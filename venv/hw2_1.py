import tushare as ts
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


pd.set_option('display.max_columns',1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth',1000)

ts.set_token('f6affddf3196b99ed9bbfd53e5dc7b5bd29acebe5e5ed8d9e28eda84')


df = ts.get_hist_data(code='601666', start='2018-01-01', end='2018-12-31')
dfs = ts.get_hist_data(code='sh000001', start='2018-01-01', end='2018-12-31')

y = df['close']
x = dfs['close']
print(y.shape)
print(y.info())
print(x.shape)
print(x.info())


# plt.scatter(x,y, facecolor='None', edgecolor='k', alpha=0.3)
# plt.show()
#
# model = sm.OLS(x,y)
# results = model.fit()
# results.summary()



