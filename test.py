import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json

with open('clinical.project-fm-ad.2025-04-27.json', 'r') as file:
    data = json.load(file)

columns_of_interest = ["disease_type", "primary_site"]
cleaned_data = [
    entry for entry in data
    if all(entry.get(column, "").lower() != "not reported" for column in columns_of_interest)
]

types = []
for entry in cleaned_data:
    if entry["disease_type"] not in types:
        types.append(entry["disease_type"])

countf = 0
countm = 0
fcount = 0
mcount = 0

for i in range(len(cleaned_data)):
    gender = cleaned_data[i]["demographic"]["gender"].lower()
    diagnoses_list = cleaned_data[i]["diagnoses"]

    if diagnoses_list:
        primary_diagnosis = diagnoses_list[0]["primary_diagnosis"].lower()

        if gender == "female":
            countf += 1
            if primary_diagnosis == "adenocarcinoma, nos":
                fcount += 1
        elif gender == "male":
            countm += 1
            if primary_diagnosis == "adenocarcinoma, nos":
                mcount += 1

proportions = [
    fcount / countf if countf else 0,
    mcount / countm if countm else 0
]

labels = ['Female', 'Male']
plt.bar(labels, proportions, color=['pink', 'lightblue'])
plt.ylabel('Proportion with Adenocarcinoma, NOS')
plt.title('Proportion of Adenocarcinoma, NOS by Sex')
plt.ylim(0, 1)
plt.show()
  '''
