import pandas
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

#import requests, io #internet and input tools
import zipfile as zf #zip file tools
import shutil #file management tools
import os #operating system tools (check files)

from bokeh.io import export_png, export_svgs, show
from bokeh.models import ColumnDataSource, DataTable, TableColumn




col_list = [' State/Territory/Federal Entity ', ' Total Doses Delivered ', ' Doses Delivered per 100K ', ' Total Doses Administered ', ' Doses Administered per 100k ']
df = pandas.read_csv(r'C:\Users\Chris\Desktop\Project\Data\covid19_vaccinations.csv', skiprows=3, usecols=col_list)

columns = [TableColumn(field=column, title=column) for column in df.columns] # bokeh columns
source = ColumnDataSource(df)
data_table = DataTable(columns=columns, source=source) # bokeh table

show(data_table)




