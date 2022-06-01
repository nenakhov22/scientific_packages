import numpy as np
import pandas as pd
normal_sample = np.random.normal(loc = 0.0, scale = 1.0, size = 10000)
random_sample = np.random.random(size = 10000)
gamma_sample = np.random.gamma(2, size = 10000)
df = pd.DataFrame({'normal': normal_sample, 'random': random_sample, 'gamma': gamma_sample})
df.head()
df.describe()
print(df.describe())
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure()
_ = plt.boxplot([df['normal'], df['random'], df['gamma']], whis = [10, 90])
plt.show()

dff = pd.DataFrame(data = df, columns = ["normal", "random", "gamma"])
sns.boxplot(x = None, y = None, data = dff)
bp = sns.boxplot(x = "variable", y = 'value', data = pd.melt(dff), whis = [0, 100])

plt.show()
