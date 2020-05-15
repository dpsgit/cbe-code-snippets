#!/usr/bin/env python
# coding: utf-8

# In[4]:


"""
 ________  ________  _____ ______   _____ ______   ___  ___  ________   ___  _________    ___    ___                       
|\   ____\|\   __  \|\   _ \  _   \|\   _ \  _   \|\  \|\  \|\   ___  \|\  \|\___   ___\ |\  \  /  /|                      
\ \  \___|\ \  \|\  \ \  \\\__\ \  \ \  \\\__\ \  \ \  \\\  \ \  \\ \  \ \  \|___ \  \_| \ \  \/  / /                      
 \ \  \    \ \  \\\  \ \  \\|__| \  \ \  \\|__| \  \ \  \\\  \ \  \\ \  \ \  \   \ \  \   \ \    / /                       
  \ \  \____\ \  \\\  \ \  \    \ \  \ \  \    \ \  \ \  \\\  \ \  \\ \  \ \  \   \ \  \   \/  /  /                        
   \ \_______\ \_______\ \__\    \ \__\ \__\    \ \__\ \_______\ \__\\ \__\ \__\   \ \__\__/  / /                          
    \|_______|\|_______|\|__|     \|__|\|__|     \|__|\|_______|\|__| \|__|\|__|    \|__|\___/ /                           
                                                                                        \|___|/                            
                                                                                                                           
                                                                                                                           
              ________  ________  ________                ___      ________  ___  ___  _____ ______   ________             
             |\   __  \|\   ____\|\   ____\              /  /|    |\   __  \|\  \|\  \|\   _ \  _   \|\   ____\            
             \ \  \|\  \ \  \___|\ \  \___|_            /  //     \ \  \|\  \ \  \\\  \ \  \\\__\ \  \ \  \___|_           
              \ \   __  \ \  \    \ \_____  \          /  //       \ \   ____\ \  \\\  \ \  \\|__| \  \ \_____  \          
               \ \  \ \  \ \  \____\|____|\  \        /  //         \ \  \___|\ \  \\\  \ \  \    \ \  \|____|\  \         
                \ \__\ \__\ \_______\____\_\  \      /_ //           \ \__\    \ \_______\ \__\    \ \__\____\_\  \        
                 \|__|\|__|\|_______|\_________\    |__|/             \|__|     \|_______|\|__|     \|__|\_________\       
                                    \|_________|                                                        \|_________|       
                                                                                                                           
                                                                                                                           
                                              ________  ___  ___  ___  ________  _______                                           
                                             |\   ____\|\  \|\  \|\  \|\   ___ \|\  ___ \                                          
                                             \ \  \___|\ \  \\\  \ \  \ \  \_|\ \ \   __/|                                         
                                              \ \  \  __\ \  \\\  \ \  \ \  \ \\ \ \  \_|/__                                       
                                               \ \  \|\  \ \  \\\  \ \  \ \  \_\\ \ \  \_|\ \                                      
                                                \ \_______\ \_______\ \__\ \_______\ \_______\                                     
                                                 \|_______|\|_______|\|__|\|_______|\|_______|           
"""





#Hello and welcome to the 
#The American Community Survey (ACS) Public Use Microdata Sample (PUMS)
#data extraction/analysis guide!


#This guide covers using Python3 and the extremeley popular data science library Pandas!
#Feel free to scroll down into the code!



#Here are a few basics for getting started on PUMS and ACS data:

#To access these column names, follow the following steps:
"""
1) Paste this URL into your browser:
https://www.census.gov/programs-surveys/acs/data/pums.html

2) Under the "PUMS on data.census.gov" section click on any of the rows

3) You will see an interactive table on the bottom of the site

4) Type the class of the information you want to access (i.e. "income," "household size"). 
These are called "variables" in data science/data analysis. This guide refers to them as variables.
(Skip to step 5 for rest of the steps)

Note: This table will have data from both "person data" and "household data". 
You can infer which variable name relates to which data or you can simply run the following:

#CODE:
pData = pd.read_csv(p)
hData = pd.read_csv(h)
dfP = pData[['Variable Name to Test']]
dfH = pData[['Variable Name to Test']]

And see which one works (does not error when you run). 
If both fail, that variable name does not exist in PUMS data.

This is better than opening up large files and doing cntrl F/CMD F to search there, though this is another option.

Continuing...
5) Choose the appropriate data type, you can click "DETAILS" to access more info about the variable.

6) Take note of the names under the "Variable" column on the same row as your desired variable
— these are the variable names you may use in your program for accessing PUMS data. 
DO NOT use anything in the "Label," this won't work.

7) Enjoy data science! Keep a running list or define data in your research question of your variable names.
Remember — anyone can code!

Note: This guide does not cover how to use data retrieved from the interactive table. 
It's discouraged to use the table to select variables as it glitches considering it's in beta.
However, you can use the same code snippets covered in this guide to access data and analyze it.
"""

"""
1) If you'd like to go a step further and create clorophleths (i.e. maps) for data visualization, then make sure to
install geopandas with pip: https://geopandas.org/install.html

2) Then, head to the following site to download the shapes: https://www.census.gov/cgi-bin/geo/shapefiles/index.php

3) Under "Select year" select the desired year; it's best to download the most recent year if researching current trends.

4) Under "Select a layer type" select the desired layer. This guide covers the use of "Counties (and equivalent)."

5) Put it in the folder where you're storing all your research data.

6) Now, you can use the Geopandas library.
"""

#If you simply want to access the code, press cntrl F/CMD F (find word command) and search for "#CODE"

#Happy coding!


# In[71]:


# Importing relevant libraries
import pandas as pd
import numpy as np
import matplotlib as mt
import geopandas as gpd
import warnings


# In[22]:


#Not important: To suppress 'future warning'
warnings.simplefilter(action='ignore', category=FutureWarning)


# In[23]:


# Setting two variables 'p' and 'h' for my "person data" and my "household data," respectively.
p = 'psam_p06.csv'
h = 'hca.csv'


# In[24]:


pData = pd.read_csv(p)


# In[25]:


#Not important: Have this long line for "low_memory" bug, not important to actual data analysis.
hData = pd.read_csv(h, sep=',', error_bad_lines=False, index_col=False, dtype='unicode')


# In[26]:


# Question 1

"""
What is the geographic distribution of workers (i.e. their PUMA field) 
in the Petroleum Refining sector (i.e. have a NAICS code of 32411)
who work in Contra Costa County (i.e. their Place of Work PUMA is “01300”)? 
"""


# In[57]:


# Step 1) Get relevant rows:

#In this case, I'm looking for workers with the following characteristics:
"""
- Petroleum Refining sector --> NAICS code
- Contra Costa County --> Place of Work PUMA
"""
#For PUMS data, this means I have to access my "person data," so I use my "pData" table.
#Renaming is a good practice, I will rename "NAICSP" to "NAICS Code" and "POWPUMA" 
#as well as "POWPUMA" to "Place of Work PUMA"

#CODE:
dfPerson = pData[['NAICSP', 'POWPUMA']]
dfPerson = dfPerson.rename(columns={"NAICSP": "NAICS_Code", "POWPUMA": "Place_of_Work_PUMA"})


# In[58]:


#Verify we have the correct rows:

#CODE:
dfPerson


# In[59]:


# Step 2) If you need data with certain conditions 
# filter by relevant rows that answer your research question.

#In this case, I'm looking for workers with two constraints:
"""
- NAICS code of 32411
- Place of Work PUMA is “01300”
"""

#CODE:
dfPersonFiltered = dfPerson[(dfPerson.NAICS_Code == "32411") & (dfPerson.Place_of_Work_PUMA == 1300)]
#Note: NAICSP is a string, as I got by experimenting and the POWPUMA is a number; 
#sometimes experimenting(playing around a bit with the code) is necessary to see what works and what doesn't.


# In[74]:


#Verify we have the correct values:

#CODE:
dfPersonFiltered


# In[80]:


#We found the answer: dfPersonFiltered
#Now, a bunch of numbers in a table doesn't answer our question for a geographic distrubition
#If we want to visually represent the geographic distribution, then we need to use the Geopandas library.

#We import the data (the whole folder). Call read_file on .shp file, in folder, 
#but make sure the other files (.dbf, .shx, .prj etc...) are present.

#CODE:
dfGeoPolygons = "2019_us_county/tl_2019_us_county.shp"
dfGeo = gpd.read_file(dfGeoPolygons)


# In[82]:


#CODE:
numPersonPetroleumContraCosta = dfPersonFiltered.count()
numPersonPetroleumOthers = dfPerson[(dfPerson.NAICS_Code == "32411")].count()

ratioPersonPetroleumContraVersusOthers = (numPersonPetroleumContraCosta / numPersonPetroleumOthers) * 100

#QUite difficult geo pandas .... to be continued....


# In[ ]:





# In[67]:


# Question 2 

"""
What is the age, gender, race (for the workers), household income,
household size (for their households), breakdown of workers 
in the Petroleum Refining sector(i.e. have a NAICS code of 32411) in California? 
"""


# In[66]:


#Note: Descriptions from here will be shorter and more on-point

#This question involves merging tables (joining tables)

#Finding the age, gender, race variable names using the interactive table
#and filtering the table.
#There is no gender variable defined in PUMS data, only "SEX", so I use that here.

#Finally, I also filter for location (California) 

#CODE:
dfP = pData[['AGE', 'SEX', 'RAC1P']]


# In[15]:


dfH = hData[['SERIALNO', 'LANP',]]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




