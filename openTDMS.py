from nptdms import TdmsFile
import pandas as pd
import numpy as np
import plotly.express as px
import ntpath

file = "testFiles/LD1_2020.06.22_19.58.18.tdms"
file_name = ntpath.basename(file)
main_df = pd.DataFrame()

tdms_file = TdmsFile.read(file)
for group in tdms_file.groups():
    group_name = group.name
    for channel in group.channels():        
        data = []
        temp_df = pd.DataFrame()
        channel_name = group_name + " " + channel.name
        # Access dictionary of properties:
        properties = channel.properties
        # Access numpy array of data for channel:
        block = channel[:]
        for samples in block:
            data.append(samples)     
        temp_df[channel_name] = data
        main_df = pd.concat([main_df,temp_df], ignore_index=False, axis=1)

fig = px.line(main_df,title=file_name)
fig.show()