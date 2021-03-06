from nptdms import TdmsFile
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import click

tdms_file = TdmsFile.read("TestFiles/WVF_2020.08.07_00.00.00.tdms")

channel = tdms_file["Vel"]["Untitled"]
time = channel.time_track(absolute_time=True)
data = channel[:]


df = pd.DataFrame({'Time':time, 'Amplitude':data})

print(df)

sns.set_theme(style="darkgrid")
sns.lineplot(x = 'Time', y = 'Amplitude', data=df)
sns.despine()
plt.show()
