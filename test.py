import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json
import requests


with open('clinical.project-fm-ad.2025-04-27.json', 'r') as file:
 data = json.load(file)

x = []
for i in range(len(data)):
 x.append(data[i]["primary_site"])

plt.scatter(x, range(len(x)))
plt.show()
