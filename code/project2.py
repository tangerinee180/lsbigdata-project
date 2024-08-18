import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt    
import plotly
import json

    
#############챕터 11 연습

geo_seoul = json.load(open("data/SIG_Seoul.geojson",encoding="UTF-8"))

type(geo_seoul)
len(geo_seoul)
geo_seoul.keys()

geo_seoul["features"][0]["properties"]
geo_seoul["features"][1]["properties"]
geo_seoul["features"][2]["properties"]
geo_seoul["features"][3]["properties"]

geo_seoul["features"][0]["geometry"]
geo_seoul["features"][0]["geometry"]["coordinates"]
geo_seoul["features"][0]["geometry"]["coordinates"][0]
geo_seoul["features"][0]["geometry"]["coordinates"][0][0]

def draw_map(x):
    import numpy as np
    import matplotlib as plt
    coordinate_list = geo_seoul["features"][x]["geometry"]["coordinates"][0][0]
    coordinate_array = np.array(coordinate_list)
    x = coordinate_array[:,0]
    y = coordinate_array[:,1]
    plt.rcParams.update({"font.family": "Malgun Gothic"})
    plt.plot(x,y)
    plt.show()
    plt.clf()
    return geo_seoul["features"][x]["properties"]["SIG_KOR_NM"]

draw_map(2)
#조별

def df_gu(x):
    import numpy as np
    import pandas as pd
    coordinate_list = geo_seoul["features"][x]["geometry"]["coordinates"][0][0]
    coordinate_array = np.array(coordinate_list)
    df = pd.DataFrame({})
    df["gu_name"] = [geo_seoul["features"][x]["properties"]["SIG_KOR_NM"]]*len(coordinate_array)
    df["x"] = coordinate_array[:,0]
    df["y"] = coordinate_array[:,1]
    return df
'''
def df_gu(x):
    coordinate_list = geo_seoul["features"][x]["geometry"]["coordinates"][0][0]
    coordinate_array = np.array(coordinate_list)
    gu_name = geo_seoul["features"][x]["properties"]["SIG_KOR_NM"]
    df = pd.DataFrame({
        "gu_name": [gu_name] * len(coordinate_array),
        "x": coordinate_array[:, 0],
        "y": coordinate_array[:, 1]
    })
    return df
'''
df_gu(0)
result = pd.DataFrame({})
for x in range(len(geo_seoul["features"])):
    result = pd.concat([result,df_gu(x)])
    df = df_gu(x)
    plt.plot(df["x"],df["y"])
plt.show()
result = result.reset_index(drop=True)
result

# 1 
plt.plot(result['x'],result['y'])
#sns.lineplot(data = result,x = 'x', y = 'y', hue= "gu_name")
plt.legend(fontsize = 2)
plt.show()
plt.clf()


# 2
for x in range(len(geo_seoul["features"])):
    result = pd.concat([result,df_gu(x)])
sns.scatterplot(data = result,x = 'x', y = 'y', hue= "gu_name",s=2)

plt.show()
plt.clf()


result = pd.concat([df_gu(x) for x in range(len(geo_seoul["features"]))]).reset_index(drop=True)

#선생님 방법
gu_name=list()
for i in range(25):
    gu_name.append(geo_seoul["features"][i]["properties"]["SIG_KOR_NM"])

gu_name = [geo_seoul["features"][i]["properties"]["SIG_KOR_NM"] for i in range(len(geo_seoul["features"]))]
def make_seouldf(num):
    gu_name=geo_seoul["features"][num]["properties"]["SIG_KOR_NM"]
    coordinate_list=geo_seoul["features"][num]["geometry"]["coordinates"]
    coordinate_array=np.array(coordinate_list[0][0])
    x=coordinate_array[:,0]
    y=coordinate_array[:,1]
    return pd.DataFrame({"gu_name":gu_name, "x": x, "y": y})

make_seouldf(1)

result=pd.DataFrame({})
for i in range(25):
    result=pd.concat([result, make_seouldf(i)], ignore_index=True)    

result

import pandas as pd
gangnam_df = result.assign(is_gangnam = np.where(result["gu_name"] == "강남구", "강남", "안강남"))

sns.scatterplot(data = gangnam_df,
                x = "x", y = "y", palette = {"안강남" : "grey", "강남" : "red"}, hue = "is_gangnam", s = 2,
                legend = False)
plt.show()
plt.clf()
gangnam_df["is_gangnam"].unique()


geo = json.load(open("data/SIG.geojson", encoding='UTF-8'))
geo["features"][0]["properties"]
geo["features"][0]["geometry"]

df_pop = pd.read_csv("data/Population_SIG.csv")
df_pop.head
df_pop.info()

df_pop["code"] = df_pop["code"].astype(str)
df_seoulpop = df_pop.iloc[1:26]
df_seoulpop["code"] = df_seoulpop["code"].astype(str)
df_seoulpop.info



#!pip install folium

    import folium
my_map = folium.Map(location =[result["y"].mean(),result["x"].mean()],
             zoom_start = 15)
my_map.save("map_seoul2.html")
result["x"].mean()
result["y"].mean()
my_map = folium.Map(location =[37.551,126.973],
           zoom_start = 12,
           tiles = "cartodbpositron")
my_map.save("map_seoul3.html")


folium.Choropleth(
    geo_data = geo_seoul,
    data = df_seoulpop,
    columns = ('code','pop'),
    key_on = "feature.properties.SIG_CD")\
    .add_to(my_map)
my_map.save("map_seoul3.html")
bins = list(df_pop['pop'].quantile([0.0,0.2,0.4,0.6,0.8,1.0]))
#배경지도 재생성
map_sig = folium.Map(location =[35.95,127.7],
           zoom_start = 8,
           tiles = "cartodbpositron")

folium.Choropleth(
    geo_data = geo,
    data = df_pop,
    columns = ('code','pop'),
    key_on = "feature.properties.SIG_CD",
    fill_color = "YlGnBu",
    fill_opacity = 1,
    line_opacity = 0.5,
    bins = bins)\
    .add_to(map_sig)

# 코로플릿 with bins
# matplotlib 팔레트
# tab10, tab20, Set1, Paired, Accent, Dark2, Pastel1, hsv 
# seaborn 팔레트
# deep, muted, bright, pastel, dark, colorblind, viridis, inferno, magma, plasma

bins = list(df_seoulpop["pop"].quantile([0, 0.2, 0.4, 0.6, 0.8, 1]))
folium.Choropleth(
    geo_data=geo_seoul,
    data=df_seoulpop,
    columns=("code", "pop"),
    fill_color="viridis",
    bins=bins,
    key_on = "feature.properties.SIG_CD").add_to(map_sig)
    
map_sig.save("map_seoul.html")

# 점 찍는 법
# make_seouldf(0).iloc[:,1:3].mean()
folium.Marker([37.583744, 126.983800], popup="종로구").add_to(map_sig)
map_sig.save("map_seoul.html")











#
map_seoul = folium.Map(location =[37.5,127],
           zoom_start = 12,
           tiles = "cartodbpositron")
bins = list(foreigner['pop'].quantile([0.0,0.2,0.4,0.6,0.8,1]))

folium.Choropleth(
    geo_data = geo_seoul,
    data = foreigner,
    columns = ('code','pop'),
    key_on = "feature.properties.ADM_DR_CD",
    fill_color = "Blues",
    nan_fill_color = "White",
    fill_opacity = 1,
    line_opacity = 0.5,
    bins = bins)\
    .add_to(map_seoul)
map_seoul



[geo_seoul["features"][1]["properties"]["SIG_KOR_NM"]]*len(df)

coordinate_list = geo_seoul["features"][x]["geometry"]["coordinates"][0][0]

plt.rcParams.update({"figure.dpi": 150,
"figure.figsize": [8, 6],
"font.size": 11,
"font.family": "Malgun Gothic"})


coordinate_list = geo_seoul["features"][0]["geometry"]["coordinates"][0][0]
coordinate_list = np.array(coordinate_list)
x = coordinate_list[:,0]
y = coordinate_list[:,1]

plt.plot(x,y)
plt.show()
plt.clf()
foreigner = pd.read_csv("data/Foreigner_EMD_Seoul.csv")
foreigner.head()
foreigner.info()

foreigner["code"] = foreigner["code"].astype(str)
bins = list(foreigner['pop'].quantile([0.0,0.2,0.4,0.6,0.8,1]))
map_seoul = folium.Map(location =[37.5,127],
           zoom_start = 12,
           tiles = "cartodbpositron")

folium.Choropleth(
    geo_data = geo_seoul,
    data = foreigner,
    columns = ('code','pop'),
    key_on = "feature.properties.ADM_DR_CD",
    fill_color = "Blues",
    nan_fill_color = "White",
    fill_opacity = 1,
    line_opacity = 0.5,
    bins = bins)\
    .add_to(map_seoul)
map_seoul


geo_seoul_sig = json.load(open("data/SIG_Seoul.geojson",encoding="UTF-8"))


folium.Choropleth(geo_data = geo_seoul_sig,
                  fill_opacity = 0,
                  line_weight = 4)\
                  .add_to(map_seoul)
map_seoul
map_seoul.save("map_seoul.html")
map_sig.save("map_sig.html")




import webbrowser
webbrowser.open_new("map_seoul.html")
webbrowser.open_new("map_sig.html")
