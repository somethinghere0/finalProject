import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json
import requests

csv_file_path = 'ES2 Project data - Sheet1.csv'
csvTwo = "ES2 Project data - 5 year survival by stage.csv"
csvThree = "ES2 Project data - funding.csv"

data = pd.read_csv(csv_file_path).dropna(subset=["type"])
dataTwo = pd.read_csv(csvTwo)
dataThree = pd.read_csv(csvThree).dropna(subset=["type", "federal funding (2019)"])

type = data["type"].astype(str)
mortality = data["death rate (mortality)"]
newCases = data["new cases"]
incedence = data["rate of new cases (incedence)"]
deaths = data["deaths"]
survival = data["Relative survival (%) (% who survive 5 yrs after dx)"]

filtered_data = dataTwo.dropna(subset=["type", "distant"])
typeT = filtered_data["type"].astype(str)
distant = filtered_data["distant"]
stages = filtered_data["all stages"]
localized = filtered_data["localized"]
regional = filtered_data["regional"]

TypeH = dataThree["type"].astype(str)
Funding = dataThree["federal funding (2019)"]

def tymort():
    plt.figure()
    plt.bar(type, mortality)
    plt.xlabel('Type')
    plt.ylabel('Mortality') 
    plt.title('Mortality Rates by Cancer Type')
    plt.xticks(rotation=80, fontsize=8)

def tyin():
    plt.figure()
    plt.bar(type, incedence)
    plt.xlabel('Type')
    plt.title('Incidence Rates by Cancer Type')
    plt.xticks(rotation=80, fontsize=5)

def tynew():
    plt.figure()
    plt.bar(type, newCases)
    plt.xlabel('Type')
    plt.ylabel('New Cases')
    plt.title('New Cases by Cancer Type')
    plt.xticks(rotation=80, fontsize=8)

def local():
    plt.figure()
    plt.bar(typeT, localized)
    plt.xlabel('Type')
    plt.ylabel('Five year survival if localized')
    plt.title('Five year survival rate for localized caner')
    plt.xticks(rotation=80, fontsize=8)

def reg():
    valid_data = filtered_data[filtered_data["regional"] != "No Data"].dropna(subset=["regional"])
    filtered_typeT = valid_data["type"].astype(str)
    filtered_regional = valid_data["regional"].astype(float)
    plt.figure()
    plt.bar(filtered_typeT, filtered_regional)
    plt.xlabel('Type')
    plt.ylabel('Five year survival if regional (%)')
    plt.title('Five year survival if regional')
    plt.xticks(rotation=80, fontsize=8)
    plt.ylim(0, 100)

def dist():
    plt.figure()
    plt.bar(typeT, distant)
    plt.xlabel('Type')   
    plt.ylabel('Five year survival if distant')
    plt.title('Five year survival if Distant')
    plt.xticks(rotation=80, fontsize=8)

def stage():
    valid_data = filtered_data[filtered_data["regional"] != "No Data"].dropna(subset=["regional"])
    filtered_typeT = valid_data["type"].astype(str)
    filtered_regional = valid_data["regional"].astype(float)
    plt.figure()
    plt.scatter(filtered_typeT, filtered_regional, color="y", marker="x", label = "Regional")
    plt.scatter(typeT, localized, color="r", marker="s", label = "Localized")
    plt.scatter(typeT, distant, color="b", label = "Distant")
    plt.xlabel('Type')
    plt.ylabel('Five year survival rates by stage')
    plt.title('Five Year Survival Rate for Each Stage by Type')
    plt.xticks(rotation=80, fontsize=8)
    plt.grid(axis='x')
    
def funding():
    plt.figure()
    plt.bar(TypeH, Funding, color = "g")
    plt.xlabel('Type')
    plt.ylabel('2019 Federal Funding (Millions)')
    plt.title('Funding by Type')
    plt.xticks(rotation=80, fontsize=8)

def johnAdams():
    plt.figure()
    plt.bar(TypeH, Funding, color = "g")
    plt.xlabel('Type')
    plt.ylabel('2019 Federal Funding (Millions)')
    plt.title('Funding by Type')
    plt.xticks(rotation=80, fontsize=8)

#dist()
#reg()
#local()
#tymort()
#tyin()
#tynew()
#tyStage()
funding()
plt.show()

tyin()
tynew()
plt.show()
