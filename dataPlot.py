import csv
import pandas as pd
from prettytable import PrettyTable
import matplotlib.pyplot as plt

class WebScraper:

    def __init__ (self) -> None:
        self.cases = {}
        self.deaths = {}
        self.csvToTable(self.cases, self.deaths)
        self.csvToPlot()

    def csvToTable(cases, deaths):  
        with open('totalCases_Deaths.csv', 'r') as csvfile:
            table = PrettyTable()
            table.field_names = ["State", "Total Cases", "Total Deaths"]

            reader = csv.reader(csvfile, delimiter = ',')

            header = next(reader)
            header = next(reader)
            header = next(reader)
            header = next(reader)

            for row in reader:
                cases[row[0]] = float(row[1])
                deaths[row[0]] = float(row[6])

            for key in cases:
                table.add_row([key, cases[key], deaths[key]])

            print(table)

            csvfile.close()

    def csvToPlot(self) -> None:
        df = pd.read_csv('totalCases_Deaths.csv', skiprows=3)
        df = df[:-1]

        df.set_index(['State/Territory'])[['Total Cases', 'Total Deaths']].plot(kind='bar')
        plt.show()