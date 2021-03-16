import csv
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
import pandas as pd
from matplotlib.ticker import FuncFormatter
import numpy as np


class WebScraper:
    
    
    """Parses through CSV files for data"""


    PT_FIELD_NAMES = ['State', 'Doses Delivered', 'Doses Administered']
    #pretty_table = PrettyTable(field_names = ['State', 'Doses Delivered', 'Doses Administered'])

    def __init__(self) -> None:
        
        self.doses_delivered = {}
        self.doses_administered = {}
        self.vaccine_scraper()
        self.print_vaccine_pt()

    def vaccine_scraper(self):

        """Stores vaccine data in dictionaries"""

        
        with open(r'C:\Users\Chris\Desktop\2021S CS-545-WS\covid19_vaccinations_in_the_united_states.csv', 'r') as file:

            # doses_delivered = self.dos
            # doses_administered = {}
            
            reader = csv.reader(file, delimiter = ',')
            header = next(reader)

            for row in reader:

                self.doses_delivered[row[0]] = int(row[1])
                self.doses_administered[row[0]] = int(row[4])
    
    def print_vaccine_pt(self) -> None:

        """Prints the vaccine rollout in pretty table"""

        pt = PrettyTable(field_names=['State', 'Doses Delivered', 'Doses Administered'])
        for key in self.doses_delivered:
            table_row = [key, self.doses_delivered[key], self.doses_administered[key]]
            pt.add_row(table_row)
        print('Vaccines Delivered and Adminsitered by State\n', pt)
    


test = WebScraper()
#test.vaccine_scraper()




