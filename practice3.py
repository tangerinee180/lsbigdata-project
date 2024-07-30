import pandas as pd

mpg_raw = pd.read_csv("data/mpg.csv")

mpg = mpg_raw.copy()
cty_category = mpg.groupby("category",as_index=False).agg(cty_mean = ("cty","mean"))
cty_category.sort_values("cty_mean",ascending=False)
hwy_category = mpg.groupby("category",as_index=False).agg(hwy_mean = ("hwy","mean"))
hwy_category.sort_values("hwy_mean",ascending=False).head(3)
mpg.query("category =='compact' ").groupby("manufacturer",as_index=False).agg(count = ("category","count")).sort_values("count",ascending=False)
