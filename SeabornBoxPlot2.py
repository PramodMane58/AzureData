import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
#sb.set_style("darkgrid")
sb.boxplot(x='day',y='tips',data=data)
plt.show()