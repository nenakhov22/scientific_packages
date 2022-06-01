import numpy as np
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as mpl
from mpl_toolkits.mplot3d import axes3d

data = pd.read_csv('anime.csv', delimiter=',')
data.loc[(data['Episodes'] == '?'), 'Episodes'] = np.nan
data.head(10)
print(data.columns, data.dtypes)
data.columns = data.columns.str.lower()
print("rating:")

print(data['rating'].describe())

data['voters'] = data['voters'].str.replace(',','')
data['voters'] = data['voters'].astype(int)
perc =[.90]
data.describe(percentiles = perc, include = ['float64','int64'])

data.groupby(['production', 'title']).sum()

data.fillna({'episodes':0,'source':' ',	'genre': ' ',	'airdate':' ',	'rating' :' ',	'voters': 0,	'theme': ' '})

data['episodes'] = data['episodes'].astype(float)
print(data['episodes'].describe())

genresList = list(data['genre'].str.split(','))
genres = dict()
listGeneres = sum(genresList, [])
fig, ax = mpl.subplots()
fig.set_figwidth(22)
fig.set_figheight(6)
ax.bar(list(sorted(set(listGeneres))), [listGeneres.count(x) for x in sorted(set(listGeneres))], 1, 50)

fig2, bx = mpl.subplots()
fig2.set_figwidth(40)
fig2.set_figheight(10)

company = dict((x, list(data['production']).count(x)) for x in set(data['production']))
sorted_company = sorted(company.items(), key=lambda x: x[1])
print(dict(sorted_company))
bx.bar(dict(sorted_company).keys(), dict(sorted_company).values())
mpl.xticks(rotation=90)

fig3, cx = mpl.subplots()
fig3.set_figwidth(40)
fig3.set_figheight(10)


ep = dict((x, list(data['episodes'].dropna()).count(x)) for x in set(data['episodes'].dropna()))
ep_sorted = sorted(ep.items(), key=lambda x: x[0])
print(ep_sorted)
cx.bar(dict(ep_sorted).keys(), dict(ep_sorted).values())
mpl.show()

print("Топ 3 источника")
teasss = data.groupby(['source']).size()
teasss.sort_values().iloc[-3:]

src1 = data.groupby(['source']).size().sort_values()
src1.head()
segse=src.to_list()
ax = mpl.bar(src.index, segse)

ratings = data.groupby(['production'])['rating'].mean().sort_values().dropna()
ax = mpl.bar(ratings.index, ratings)

ratings = data.rating.dropna().apply(int).value_counts().sort_index().rename(lambda t: f'[{t}; {t+1})')
ax = mpl.bar(ratings.index, ratings)
