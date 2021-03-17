import pandas
import numpy as np
import os #operating system tools (check files)
from bokeh.io import export_png, export_svgs, show
from bokeh.models import ColumnDataSource, DataTable, TableColumn


class PNGTables:


    """Parses through CSV files for COVID-19 data and prints data
    into separate PNG files by state"""


    def __init__(self, vaccine_path: str, cases_path: str) -> None:

        """Initiailize functions"""

        self.vaccine_path = vaccine_path
        self.cases_path = cases_path

        self.export_vaccine_tables()
        self.export_cases_tables()

    def export_vaccine_tables(self):

        """Exports vaccine data in PNG files"""

        os.chdir(self.vaccine_path)

        col_list = [' State/Territory/Federal Entity ',
        ' Total Doses Delivered ', ' Doses Delivered per 100K ',
        ' Total Doses Administered ', ' Doses Administered per 100k '] #Limit data frame to specific columns needed

        df = pandas.read_csv('covid19_vaccinations.csv', skiprows=3, usecols=col_list)

        columns = [TableColumn(field=column, title=column) for column in df.columns] #bokeh columns
        source = ColumnDataSource(df)

        states = source.data[' State/Territory/Federal Entity '] #Create a list of states to parse through

        #Below exports data table by State
        for state in states:
            state = state.strip()
            source = ColumnDataSource(df.loc[df[' State/Territory/Federal Entity '] == f' {state} '])
            data_table = DataTable(columns=columns, source=source, index_position=None, width=1000)
            export_png(data_table, filename= f'{state}_Vaccinations.png')

    
    def export_cases_tables(self):

        """Exports case and death data in PNG files"""

        os.chdir(self.cases_path)

        col_list = [' State/Territory ',
        ' Total Cases ', ' Confirmed Cases ', ' Cases in Last 7 Days ',
        ' Case Rate per 100000 ', ' Total Deaths '] #Limit data frame to specific columns needed

        df = pandas.read_csv('covid19_cases.csv', skiprows=3, usecols=col_list)

        columns = [TableColumn(field=column, title=column) for column in df.columns] #bokeh columns
        source = ColumnDataSource(df)

        states = source.data[' State/Territory '] #Create a list of states to parse through

        #Below exports data table by State
        for state in states:
            state = state.strip()
            source = ColumnDataSource(df.loc[df[' State/Territory '] == f' {state} '])
            data_table = DataTable(columns=columns, source=source, index_position=None, width=1000)
            export_png(data_table, filename= f'{state}_Cases.png')

vaccine_path = r'C:\Users\Chris\Desktop\Project\Vaccinations_PNG'
export_path = r'C:\Users\Chris\Desktop\Project\Vaccinations_PNG'

test = PNGTables()
test.export_vaccine_tables()
test.export_cases_tables()





