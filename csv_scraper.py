import csv
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
import pandas as pd
from matplotlib.ticker import FuncFormatter
import numpy as np


class CSVScraper:
    
    
    """Parses through CSV files for COVID-19 data"""


    def __init__(self, vaccine_path: str, cases_path: str) -> None:

        """Initiailize functions"""

        self.vaccine_path = vaccine_path
        self.cases_path = cases_path

        self.doses_delivered = {}
        self.doses_administered = {}
        self.cases = {}
        self.deaths = {}

        self.data_scraper()

        self.print_vaccine_pt()
        self.print_cases_pt()

    def data_scraper(self):

        """Stores data in dictionaries"""
        
        with open(self.vaccine_path, 'r') as file:

            reader = csv.reader(file, delimiter = ',')
            header = next(reader)

            for row in reader:

                self.doses_delivered[row[0]] = int(row[1])
                self.doses_administered[row[0]] = int(row[4])
    
        with open(self.cases_path, 'r') as file:

            reader = csv.reader(file, delimiter = ',')
            header = next(reader)

            for row in reader:

                self.cases[row[0]] = int(row[1])
                self.deaths[row[0]] = int(row[6])

    
    def print_vaccine_pt(self) -> None:

        """Prints the vaccine rollout in pretty table"""

        pt = PrettyTable(field_names=['State/Territory/Federal Entity', 'Doses Delivered', 'Doses Administered'])
        for key in self.doses_delivered:
            table_row = [key, self.doses_delivered[key], self.doses_administered[key]]
            pt.add_row(table_row)
        print('Vaccines Delivered and Adminsitered by State\n', pt)

    def print_cases_pt(self) -> None:

        """Prints total cases and deaths in pretty table"""

        pt = PrettyTable(field_names=['State/Territory', 'Total Cases', 'Total Deaths'])
        for key in self.cases:
            table_row = [key, self.cases[key], self.deaths[key]]
            pt.add_row(table_row)
        print('Total COVID-19 Cases and Deaths by State\n', pt)
    

vaccine_path = r'C:\Users\Chris\Desktop\2021S CS-545-WS\covid19_vaccinations_in_the_united_states.csv'
cases_path = r'C:\Users\Chris\Desktop\2021S CS-545-WS\united_states_covid19_cases_and_deaths_by_state.csv'
test = CSVScraper(vaccine_path, cases_path)