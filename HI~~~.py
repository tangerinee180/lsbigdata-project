import pandas as pd
import numpy as np
import seaborn as sns    
import matplotlib.pyplot as plt    
import math
import scipy.stats    

house_train_raw = pd.read_csv("data/train.csv")
house_train = house_train_raw.copy()
house_train = house_train[["Id","OverallQual","GrLivArea","TotalBsmtSF","SalePrice"]]
#지상 면적 구간

np.min(house_train["GrLivArea"])
np.max(house_train["GrLivArea"])

cut_lim = [i*200 for i in range(1,29)]
labels = [f"{i*2}-{i*2+2}" for i in range(2, 29)]
num = range(21)
house_train["gr_area"] = pd.cut(house_train["GrLivArea"],bins=cut_lim,labels=labels)
house_train["gr_area"] = house_train["gr_area"].astype(object)

#총 면적
house_train["tot_area"] = house_train["GrLivArea"]+house_train["TotalBsmtSF"]/6
np.max(house_train["tot_area"])
np.min(house_train["tot_area"])
cut_lim2 = [i*200 for i in range(2,39)]
labels2 = [f"{i*2}-{i*2+2}" for i in range(2, 38)]
house_train["total_area"] = pd.cut(house_train["tot_area"],bins=cut_lim2,labels=labels2)
house_train["total_area"] = house_train["total_area"].astype(object)
'''
df = house_train.groupby(["OverallQual","gr_area"],as_index=False).agg(price_mean = ("SalePrice","mean"))
df2 = house_train.groupby("gr_area",as_index=False).agg(price_mean = (("SalePrice","mean"))).sort_values("price_mean")
'''
df3 = house_train.groupby("total_area",as_index=False).agg(price_mean = (("SalePrice","mean"))).sort_values("price_mean")
df3['area_start'] = df3['total_area'].apply(lambda x: int(x.split('-')[0]))
df3_after = df3.sort_values('area_start').drop(columns='area_start').reset_index(drop=True)


sns.lineplot(data=df3_after,x=df3["total_area"],y=df3["price_mean"])
plt.title("Price by Area")
plt.xlabel("Total Area")
plt.ylabel("Home Price")

plt.show()
plt.clf()
