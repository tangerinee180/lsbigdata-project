import plotly.express as px
import seaborn as sns
from sklearn.linear_model import LinearRegression

# 데이터셋 로드
penguins = sns.load_dataset("penguins")

# 산점도 생성
fig = px.scatter(
    penguins,
    x="bill_length_mm",
    y="bill_depth_mm",
    color="species",
    #trendline="ols",
    size_max=10  # 점 크기 최대값 설정
)

# 레이아웃 업데이트
fig.update_layout(
    title=dict(text="팔머펭귄 종별 부리 길이 vs. 깊이", font=dict(color="white", size=20)),
    paper_bgcolor="black",
    plot_bgcolor="black",
    font=dict(color="white", size=14),
    xaxis=dict(
        title=dict(text="부리 길이 (mm)", font=dict(color="white", size=16)), 
        tickfont=dict(color="white", size=12),
        gridcolor='rgba(255, 255, 255, 0.2)'  # 그리드 색깔 조정
    ),
    yaxis=dict(
        title=dict(text="부리 깊이 (mm)", font=dict(color="white", size=16)), 
        tickfont=dict(color="white", size=12),
        gridcolor='rgba(255, 255, 255, 0.2)'  # 그리드 색깔 조정
    ),
    legend=dict(title=dict(text="펭귄 종", font=dict(color="white", size=16)), font=dict(color="white", size=12))
)

# 점 크기 업데이트
fig.update_traces(marker=dict(size=12))  # 점 크기 설정

# 그래프 출력
fig.show()

model = LinearRegression()
penguins.dropna(inplace=True)
x=penguins[["bill_length_mm"]]

y=penguins["bill_depth_mm"]

model.fit(x,y)
linear_fit = model.predict(x)

fig.add_trace(
    go.Scatter(
        mode = "lines",
        x=penguins["bill_length_mm"],
        y=linear_fit,=
        name = "선형회귀직선",
        line=dict(dash="dot",color="white")
    )
)
fig.show()
slope = model.coef_
intercept = model.intercept_
print(slope,intercept)


penguins_dummies = pd.get_dummies(penguins,
columns =['species'],
drop_first=False)
#아델리에 대한 정보도 있는 것
x = penguins_dummies[["bill_length_mm",'species_Chinstrap',"species_Gentoo"]]
y = penguins_dummies[["bill_depth_mm"]]

model = LinearRegression()

model.fit(x,y)

slope = model.coef_
intercept = model.intercept_
print(slope,intercept)

regline_y = model.predict(x)
import matplotlib.pyplot as plt    
plt.scatter(x["bill_length_mm"],regline_y)
plt.show()
plt.clf()
y = slope[0]*penguins_dummies["bill_length_mm"] + slope[1]*penguins_dummies["'species_Chinstrap'"]\
+0slope[2]*penguins_dummies["species_Gentoo"] + intercept

y^ = 0.2*x1 + (-5.1)*1 + 10.56 = 0.2*x1 + 5.46
