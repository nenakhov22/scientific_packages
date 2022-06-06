import numpy as np
import pandas as pd
import random as random
import matplotlib.pyplot as plt


data = pd.read_csv('anime.csv', delimiter=',')  #1
print(data.head(10)) #2
data.loc[(data['Episodes'] == '?'), 'Episodes'] = np.nan
data['Episodes'] = data['Episodes'].astype(float)

data.columns = data.columns.str.lower().str.replace(' ', '_') #4

data['voters'] = data['voters'].str.replace(',','').replace('N/A',np.nan)
data['voters'] = data['voters'].astype(int)
#print(data['Episodes'])
print(data.dtypes)  #3


#print(data['voters'])
categ = [i for i in data.columns if i not in {'episodes', 'rating', 'voters'}]
#data[categ] = data[categ].astype('category')
#for column in data.columns:
   # if data[column].dtypes != 'object':
       # print(column)
       # a,b=np.unique(np.array(list(data[column])), return_counts=True)
       # for i in range(len(a)):
           # print(a[i],':',b[i])
        #print('\n')
#print('\n')

#5

perc =[.25,.75,.90]
print(data.describe(percentiles = perc, include = ['float64','int32']))


print(data.info())



genresList = data['genre'].str.split(',')
#print(data.info())
#print('\n')

#6
for column in data.columns:
    if data[column].dtypes == 'object':
        print(column)
        a, b = np.unique(np.array(list(data[column])), return_counts=True)
        for i in range(len(a)):
            print(a[i],':',b[i])
        print('\n')
print('\n')

comp = data.groupby(['production']).size()
#print('\n\n\n\n',comp)

#8.a
company = dict((x, list(data['production']).count(x)) for x in set(data['production']))
sorted_company = sorted(company.items(), key=lambda x: x[1])
fig1, ax1 = plt.subplots()
ax1.bar(dict(sorted_company).keys(), dict(sorted_company).values())
plt.xticks(rotation=90)
plt.xticks(fontsize=4)
fig1.suptitle("зависимость между названием компаний и количеством выпущенных этой компанией аниме")



#8.b

fig3, ax3 = plt.subplots()
eps = data.groupby(['episodes']).size()
ax3.bar(eps.index, eps)
ax3.set_xlabel('amount of episodes')
ax3.set_ylabel('amount of repeating')

#8.c
fig4, ax4 = plt.subplots()

src = data.groupby(['source']).size()
src1 = src.sort_values().iloc[-3:]
ax4.bar(src1.index,src1)


#8.d
themes = pd.Series([i.split(',') for i in list(data.theme)]).explode()

themes = themes.groupby(themes).size().sort_values()
fig5, ax5 = plt.subplots()
ax5.bar(themes.index,themes)
plt.xticks(rotation=90)
plt.tick_params(labelsize=10)
#print('\n\n\n',themes)


#8.e

import re

regex_year = re.compile('\d{4}')
years = list()
year_default = "0"
for i in range(data.shape[0]):
  date = str(data['airdate'][i])
  found_year = regex_year.findall(date)
  if len(found_year) > 0:
    years.append(found_year[0])
  else:
    years.append(year_default)

data_with_year = data.assign(year = years)
year_anime_count = data_with_year['year'].value_counts().sort_index()
year_anime_count = year_anime_count.drop(year_anime_count.index[0])
fig6,ax6=plt.subplots()
plt.bar(year_anime_count.keys(), year_anime_count.values)
plt.title("производство аниме в разные годы")
plt.xticks(rotation=90)
#print(dict(sorted_company))
##




#9


fig8, ax8= plt.subplots()

ratings = data.groupby(['production'])['rating'].mean().sort_values().dropna()
plt.bar(ratings.index, ratings)
plt.xticks(rotation=90)
plt.xticks(fontsize=3.5)



#10

divide_dict={i:0 for i in range(10)}
labels_x=[f"[{i}-{i+1})" for i in range(10)]
for rate in data.rating:
    for i in range(10):
        if rate>=i and rate<i+1:
            divide_dict[i] += 1
fig9, ax9 = plt.subplots()
ax9.bar(labels_x,divide_dict.values())


#11

genres_dict = dict()
themes_dict = dict()
genres = set()
themes = set()
for i in range(data.shape[0]):
  genres_dict[data.loc[i]['title']] = set(data.loc[i]['genre'].split(','))
  genres = genres.union(genres_dict[data.loc[i]['title']])
  themes_dict[data.loc[i]['title']] = set(data.loc[i]['theme'].split(','))
  themes = themes.union(themes_dict[data.loc[i]['title']])
popular_anime = data.loc[data.rating >= 8]
not_popular_anime = data.loc[data.rating < 5]

popular_genre_dict = dict()
popular_theme_dict = dict()

for anime in popular_anime['title']:
  for genre in genres_dict[anime]:
    if genre not in popular_genre_dict:
      popular_genre_dict[genre] = 1
    else:
      popular_genre_dict[genre] = popular_genre_dict[genre] + 1
  for theme in themes_dict[anime]:
    if theme not in popular_theme_dict:
      popular_theme_dict[theme] = 1
    else:
      popular_theme_dict[theme] = popular_theme_dict[theme] + 1

not_popular_genre_dict = dict()
not_popular_theme_dict = dict()

for anime in not_popular_anime['title']:
  for genre in genres_dict[anime]:
    if genre not in not_popular_genre_dict:
     not_popular_genre_dict[genre] = 1
    else:
      not_popular_genre_dict[genre] = not_popular_genre_dict[genre] + 1
  for theme in themes_dict[anime]:
    if theme not in not_popular_theme_dict:
      not_popular_theme_dict[theme] = 1
    else:
      not_popular_theme_dict[theme] = not_popular_theme_dict[theme] + 1


colors = dict()
for theme in themes:
  colors[theme] = (random.random(), random.random(), random.random())
#print(colors)

fig10, (ax10, ax10_1) = plt.subplots(1, 2, figsize=(40,20))
fig10.suptitle('зависимость рейтинга от темы аниме', fontsize=30)
ax10.pie(popular_theme_dict.values(), labels=popular_theme_dict.keys(),textprops={'fontsize': 5},autopct='%1.2f%%', colors=[colors[key] for key in popular_theme_dict.keys()])
ax10.set_title("популярные", fontsize=20)
ax10_1.pie(not_popular_theme_dict.values(), labels=not_popular_theme_dict.keys(),textprops={'fontsize': 5},autopct='%1.2f%%', colors=[colors[key] for key in not_popular_theme_dict.keys()])
ax10_1.set_title("непопулярные", fontsize=20)

for genre in genres:
  colors[genre] = (random.random(), random.random(), random.random())


fig11, (ax11, ax11_1) = plt.subplots(1, 2, figsize=(40,20))
fig11.suptitle('зависимость рейтинга от темы аниме', fontsize=30)
ax11.pie(popular_genre_dict.values(), labels=popular_genre_dict.keys(),textprops={'fontsize': 5},autopct='%1.2f%%', colors=[colors[key] for key in popular_genre_dict.keys()])
ax11.set_title("популярные", fontsize=20)
ax11_1.pie(not_popular_genre_dict.values(), labels=not_popular_genre_dict.keys(),textprops={'fontsize': 5},autopct='%1.2f%%', colors=[colors[key] for key in not_popular_genre_dict.keys()])
ax11_1.set_title("непопулярные", fontsize=20)


#12
animes = data['title'].unique()
voters_in_group = [0 for i in range(10)]
for anime in animes:
  anime_data = data.loc[data.title == anime]
  if np.isnan(float(anime_data['rating'])) or np.isnan(int(anime_data['voters'])):
    continue
  voters_in_group[int(anime_data['rating'])] = voters_in_group[int(anime_data['rating'])] + int(anime_data['voters'])
fig12, ax12 = plt.subplots()
ax12.bar([f"[{i}-{i+1})" for i in range(10)], voters_in_group)
fig12.suptitle('зависимость рейтинга аниме от количество зрителей')
plt.show()
