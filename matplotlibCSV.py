import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dateutil.relativedelta import relativedelta
from datetime import datetime

def deleteRow(dataFrame,rowName):
    try:
        del dataFrame[rowName]
    except:
        print("ERROR No Row:",rowName)        

file = "./testFiles/LD4__2020.01.15"
df = pd.read_csv(file,header=[0,1],sep='\t')

deleteRow(df,'2X Phase')
deleteRow(df,'Speed')
deleteRow(df,'2X Amp')
deleteRow(df,'Overall')
deleteRow(df,'DC Gap')

print(df.columns)

# df["Time"] = (df["Time"]-2082844800)
df = df.apply(pd.to_numeric)
print(df["Time"])

for row in range(len(df)):
    df.loc[row,"Time"] = pd.to_datetime(df.loc[row,"Time"]-2082844800, unit='s')

# df["Time"]= pd.to_datetime((df["Time"]-2082844800), unit='s')
df.columns = df.columns.map('_'.join)

print(df)

# df.resample("3600").median()
# get current axis
# ax = plt.gca()

# for col in df.columns:
#     df.plot(kind='line', y=col,ax=ax)


# plt.show()