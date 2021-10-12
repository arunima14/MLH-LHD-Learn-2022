# -*- coding: utf-8 -*-
import numpy as np # linear algebra
import pandas as pd 

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

"""The cell above imports the necessary libaries and programs."""

import pandas as pd
CO2 = "/co2_emission.csv"
table = pd.read_csv(CO2)
table

"""Importing the CO2 emissions data set, which is sorted by country for various year, and assigning it to "table"."""

tble = table[table['Entity'] == 'United States']
tble

"""Isolating the CO2 emissions data in table format only for the United States and assigning it to "tble"."""

# Commented out IPython magic to ensure Python compatibility.
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
print("Setup Complete")

"""Importing the libraries necessary for plotting graphs."""

plt.figure(figsize=(150,100))
plt.title("Annual CO2 Emissions in the USA", fontsize = 400)
sns.barplot(x=tble['Year'], y=tble['Annual CO₂ emissions (tonnes )'])
plt.ylabel("Annual CO₂ emissions (tonnes )", fontsize = 250)
plt.xlabel("Year", fontsize = 250)

"""Plotting the isolated CO2 emissions data for the United States from the previous code cell labeled "tble". The coloration is random and has no significance."""

tina = table[table['Entity'] == 'China']
tina

"""Isolating the CO2 emissions data in table format only for China and assigning it to "tina"."""

plt.figure(figsize=(150,100))
plt.title("Annual CO2 Emissions in China", fontsize = 400)
sns.barplot(x=tina['Year'], y=tina['Annual CO₂ emissions (tonnes )'])
plt.ylabel("Annual CO₂ emissions (tonnes )", fontsize = 250)
plt.xlabel("Year", fontsize = 250)

"""Plotting the isolated CO2 emissions data for China from the previous code cell labeled "tina". The coloration is random and has no significance."""

toby = table[table['Entity'] == 'EU-28']
toby

"""Isolating the CO2 emissions data in table format only for the EU-28 and assigning it to "toby"."""

plt.figure(figsize=(150,100))
plt.title("Annual CO2 Emissions in the EU-28", fontsize = 400)
sns.barplot(x=toby['Year'], y=toby['Annual CO₂ emissions (tonnes )'])
plt.ylabel("Annual CO₂ emissions (tonnes )", fontsize = 250)
plt.xlabel("Year", fontsize = 250)

"""Plotting the isolated CO2 emissions data for the EU-28 from the previous code cell labeled "toby". The coloration is random and has no significance."""

tbl = table[table['Year'] == 2017].sort_values(by='Annual CO₂ emissions (tonnes )', ascending=False).drop(index = 20619, columns= ['Code','Year'])
tbl.head(12)

"""Isolating the CO2 emissions data for 2017 in table format, and sorting it by 'Annual CO2 emissions (tonnes)' in descedning order. I assigned this to 'tbl'. Now there is only one row for each entity whereas before, there were multple rows for each entity. This condenses the data to just one year, but allows us to visuzlize the largest CO2 emitters."""

tbl['Annual CO₂ emissions (tonnes )'].value_counts().head(10).plot.pie()
plt.axis('equal')

"""A visualization of the largest CO2 emitters in 2017. I used the table from the previous code cell titled 'tbl'."""

tbl['Annual CO₂ emissions (tonnes )'].value_counts().head(10).plot.pie()
plt.legend(labels= tbl['Entity'], loc= 'best')