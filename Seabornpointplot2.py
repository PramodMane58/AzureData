import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt

df = sb.load_dataset('titanic')
sb.pointplot(x = "sex", y = "survived", data=df)
plt.show()