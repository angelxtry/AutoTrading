from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd


gs = pd.read_csv('GS.csv')
# print(gs)
# print(gs['Date'])
print(gs.info())
fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(gs['Adj Close'])
# print(gs['Date'][0])
date_list = list(i for i in range(0, len(gs)-1, len(gs)//4))
ax.set_xticks(date_list)
ax.set_xticklabels([gs['Date'][i] for i in date_list])
ax.xaxis.set_ticks_position('bottom')

plt.show()
