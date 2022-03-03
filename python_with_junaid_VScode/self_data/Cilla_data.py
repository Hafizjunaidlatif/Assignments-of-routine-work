## import library
# import matplotlib
# from matplotlib import pyplot as plt
# import pandas as pd

#import data from file  ,,, excel / csv
chilla = pd.read_csv("data_chilla.csv")
print(chilla)

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(x="gender", hue="age" data=chilla)
plt.show()