import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt    
import plotly



house_train_raw = pd.read_csv("data/train.csv")
house_train = house_train_raw.copy()

house_test_raw = pd.read_csv("data/test.csv")
house_test = house_test_raw.copy()

house_train = house_train.groupby("YearBuilt",as_index=False).agg(Living_area = ("GrLivArea","mean"),
                                        overall_cond = ("OverallCond","mean"),
                                        sale_price_mean = ("SalePrice","mean"),
                                        sale_price_sum = ("SalePrice","sum"))
max_sale_sum =max(house_train['sale_price_sum'])

year = house_train[house_train["sale_price_sum"]==max_sale_sum]["YearBuilt"]

print("The year with the highest transaction amount :",year)

house_train.groupby("YearBuilt")

house_test = pd.merge(house_test,house_train,on="YearBuilt",how="left")

#sub
sub_df = pd.read_csv("data/sample_submission.csv")
sub_df

#SalePrice 바꿔치기
sub_df = pd.merge(house_test,sub_df,on="Id",how="left")

sub_df.to_csv("data/submission1.csv",index=False)

