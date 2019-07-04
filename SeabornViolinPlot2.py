import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('iris')
sb.violinplot(x="species", y="sepal_length", data=df)
plt.show()