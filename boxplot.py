import numpy as np
import pandas as pd
normal_sample = np.random.normal(loc = 0.0, scale = 1.0, size = 10000)
random_sample = np.random.random(size = 10000)
gamma_sample = np.random.gamma(2, size = 10000)

df = pd.DataFrame({'Norm' : normal_sample, 'Ran' : random_sample, 'Gamma' : gamma_sample})

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure()

_ = plt.boxplot(df['Ran'])
