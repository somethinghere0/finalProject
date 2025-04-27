import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json
import requests

csv_file_path = 'ES2 Project data - Sheet1.csv'

data = pd.read_csv(csv_file_path)

type = data["type"].astype(str)
mortality = data["death rate (mortality)"]
newCases = data["new cases"]
incedence = data["rate of new cases (incedence)"]
deaths = data["deaths"]
survival = data["Relative survival (%) (% who survive 5 yrs after dx)"]


def tymort():
    plt.figure()
    plt.bar(type, mortality)
    plt.xlabel('Type')
    plt.ylabel('Mortality') 
    plt.title('Mortality by Type')

def tyin():
    plt.figure()
    plt.bar(type, incedence)
    plt.xlabel('Type')
    plt.ylabel('Incedence')

def tynew():
    plt.figure()
    plt.bar(type, newCases)
    plt.xlabel('Type')
    plt.ylabel('New Cases')


tymort()
tyin()
tynew()
plt.show()
