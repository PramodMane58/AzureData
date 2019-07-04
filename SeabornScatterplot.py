
import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('tips')
print(df.columns)
sb.scatterplot(x="total_bill", y="day", data=df)
plt.show()