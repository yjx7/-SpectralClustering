# encoding=utf-8
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import matplotlib.colors
import pandas as pd
from sklearn.cluster import SpectralClustering
color=['red','blue','grey','green','yellow','purple','orange','black','pink','silver','teal','fuchsia','maroon','olive','navy','aqua','blueviolet','brown','aquamarine','powderblue']
cm = matplotlib.colors.ListedColormap(color)
data = xlrd.open_workbook('b.xls')
route=pd.read_excel('route.xls')
route=np.array(route)[:,:-1]
route=list(route)
table1 = data.sheets()[0]#工地数据
#各工地的xy坐标
gd_x=table1.col_values(1)[1:]
gd_y=table1.col_values(2)[1:]
def juju(route):
    labels=SpectralClustering(affinity='nearest_neighbors',n_clusters=20, n_neighbors=3).fit_predict(route)
    julei=list(labels)
    data=[]
    for i in range(20):
        team = []
        for j in range(92):
            if julei[j]==i:
                team.append(j)
        data.append(team)
    route=pd.read_excel('route.xls')
    route=np.array(route)[:,:-1]
    route=list(route)
    summin=[]
    index=[]
    for i in range(20):
        lei=data[i]
        sumarray=[]
        for j in range(len(lei)):
            sum = 0
            for k in range(len(lei)):
                    sum=sum+route[lei[j]][lei[k]]#lei[k] 到lei[j]
            sumarray.append(sum)
        mins=min(sumarray)
        summin.append(mins)
        minindex=sumarray.index(mins)
        index.append(lei[minindex]+1)
    return [np.sum(summin),index,summin,labels]

juleiminroute=[]
other=[]
for i in range(500):

    jieshou=juju(route)
    juleiminroute.append(jieshou[0])
    other.append(jieshou[1:])

minroute=np.min(juleiminroute)
indexx=juleiminroute.index(minroute)
otherinf=other[indexx]
labels=otherinf[-1]

X=[]
for i in range(len(gd_x)):
    X.append([gd_x[i],gd_y[i]])
X=np.array(X)

plt.style.use('ggplot')
plt.scatter(X[:, 0], X[:, 1], c=labels,cmap=cm)
X=pd.Series(gd_x)
Y=pd.Series(gd_y)

for i, a, b in zip(X.index + 1, X, Y):
    plt.annotate(
        '%s' % i,
        xy=(a, b),
        xytext=(0, -10),
        textcoords='offset points',
        ha='center',
        va='top'
    )

print otherinf
print minroute
plt.show()