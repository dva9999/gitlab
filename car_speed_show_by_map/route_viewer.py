import pandas as pd
import folium

def draw(data, m, color):

    # 添加路线
    folium.PolyLine(list(zip(data['纬度'], data['经度'])), color=color, weight=2.5, opacity=0.8).add_to(m)


    # 添加标记（每个点标注速度和时间）
    for index, row in data.iterrows():
        if index % 10 == 0:
            popup_text = f"{row['速度']} km/h<br>{row['时间']}"
            div_text = f"<div style='font-size: 12pt; color:{color}'><div style='width: 10px; height: 10px; border: 1px solid black; border-radius: 5px; background-color:{color}'></div>{row['速度']}</div>"
            #folium.Marker([row['纬度'], row['经度']], popup=popup_text, icon=folium.Icon(color=color, icon="cny")).add_to(m)
            folium.Marker([row['纬度'], row['经度']], tooltip=popup_text, popup=popup_text, icon=folium.DivIcon(html=div_text)).add_to(m)

tiles= 'https://wprd01.is.autonavi.com/appmaptile?x={x}&y={y}&z={z}&lang=zh_cn&size=1&scl=1&style=7'
a_data = pd.read_csv('1.csv')
#m_data = pd.read_csv('HS26-2024-09-08.csv')

# 创建地图
m = folium.Map(location=[a_data['纬度'].mean(), a_data['经度'].mean()], tiles=tiles, attr='高德', zoom_start=13)
draw(a_data, m, 'red')
#draw(m_data, m, 'green')

# 保存地图
m.save('route_map.html')
