
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv')
sb.boxplot(x='continent',y='lifeExp',data=data)
plt.show()