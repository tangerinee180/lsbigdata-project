import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt    

mpg = pd.read_csv('data/mpg.csv')

sns.scatterplot(data=mpg,x="cty",y="hwy",hue="cty")
plt.show()
plt.clf()


midwest = pd.read_csv("data/midwest.csv")

sns.scatterplot(data = midwest,x='poptotal',y="popasian").set(xlim=[0,50000],ylim=[0,10000])
plt.show()
plt.clf()


mpg = pd.read_csv('data/mpg.csv')

mpg_cty = mpg.query('category == "suv"').groupby('manufacturer', as_index = False) \
                .agg(mean_cty = ('cty', 'mean'))

a = mpg_cty.sort_values(by = 'mean_cty', ascending = False).head()

plt.clf()
sns.barplot(data = a, x = 'manufacturer', y = 'mean_cty')
plt.title('best cty manufacturer')
plt.show()
