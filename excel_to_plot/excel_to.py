import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.dates as mdates
import datetime

# 从第二个工作表内提取数据
df1 = pd.read_excel('data.xlsx', sheet_name=1)

# 将时间列转换为datetime类型
df1['时间'] = df1['时间'].apply(lambda t: datetime.datetime.combine(datetime.date.today(), t))

plt.plot(df1['时间'], df1['速度'])
#给y轴40的位置添加一个虚线
plt.axhline(y=30, color='r', linestyle='--')
plt.xlabel('时间')
plt.ylabel('速度')
plt.title('HS05')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))  # 设置x轴的格式
plt.gca().xaxis.set_major_locator(mdates.MinuteLocator(interval=1))  # 设置x轴的刻度间隔
plt.gcf().autofmt_xdate()  # 自动旋转日期标签，以避免重叠
plt.show()

# 从第三个工作表内提取数据
df2 = pd.read_excel('data.xlsx', sheet_name=2)

# 将时间列转换为datetime类型
df2['时间'] = df2['时间'].apply(lambda t: datetime.datetime.combine(datetime.date.today(), t))

plt.plot(df2['时间'], df2['速度'])
#给y轴40的位置添加一个虚线
plt.axhline(y=30, color='r', linestyle='--')

plt.xlabel('时间')
plt.ylabel('速度')
plt.title('HS18')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))  # 设置x轴的格式
plt.gca().xaxis.set_major_locator(mdates.MinuteLocator(interval=1))  # 设置x轴的刻度间隔
plt.gcf().autofmt_xdate()  # 自动旋转日期标签，以避免重叠
plt.show()
