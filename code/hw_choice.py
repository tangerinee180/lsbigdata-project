import pandas as pd
import numpy as np
sheet_name = 'Sheet2'
gsheet_url = "https://docs.google.com/spreadsheets/d/1RC8K0nzfpR3anLXpgtb8VDjEXtZ922N5N0LcSY5KMx8/gviz/tq?tqx=out:csv&sheet=Sheet2"
df = pd.read_csv(gsheet_url)
df

#랜덤하게 두명을 뽑아서 보여주는 코드
np.random.seed(20240730)
np.random.choice(df["이름"],size=2,replace=False)

