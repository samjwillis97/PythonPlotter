import pandas as pd
import plotly.express as px

def deleteRow(dataFrame,rowName):
    try:
        del dataFrame[rowName]
    except:
        print("ERROR No Row:",rowName)        

file = "./testFiles/LD4__2020.01.15"
df = pd.read_csv(file,header=[0,1],sep='\t')

deleteRow(df,'Test')

df.columns = df.columns.map('_'.join)
print(df.columns)

# fig = px.line(df)
# fig.show()
