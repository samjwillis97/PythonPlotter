import pandas as pd
import plotly.express as px

file = "./VPU5LBP_Trend_2020.06.23_19.00.00.csv"
df = pd.read_csv(file,header=[0,1])
# df = pd.read_csv(file,header=[0,1],index_col=0)
df.columns = df.columns.map('_'.join)


headers = df.loc[[0]]
testTime = df.iloc[0]['Time_s']
del df['Time_s']

print(headers)
print(testTime)

fig = px.line(df)
fig.show()