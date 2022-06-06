import pandas as pd
import numpy as np
data = pd.read_csv("titanic.csv")
print(data)
data_1 = pd.pivot_table(data[["Sex", "Survived"]], index = ["Sex"], columns = ["Survived"], aggfunc = len)
#print(data['Fare'].agg(['max','mean','std']))
data['Pclass'] = data['Pclass'].replace(to_replace=[1, 2, 3], value=['элита', 'средний класс', 'рабочий класс'])

data['Expensive'] = [0 for i in range(data.shape[0])]
#print(data.columns)
data.loc[data.Fare > 40,'Expensive'] = data.loc[data.Fare > 40,'Expensive'].replace(to_replace=0, value=1)
print(data)
data_2=pd.pivot_table(data[["Expensive", "Survived"]],index = ["Expensive"],columns = ["Survived"],aggfunc = len)
print(data_2)
