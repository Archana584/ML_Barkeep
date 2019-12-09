# Project 3
### Team Members:
Archana, Allison,Jacky

### ML_Barkeep
Used over 500 cocktail recipes from the cocktail database on Kaggle.com. Pandas and Excel used to clean data for model. Used RNN (Recurrent Neural Network) with LTSM (Long Short-Term Model) to “learn” the data and produce new recipes. Used Collaboratory notebook on the Google Cloud platform to run python code. This allowed to process the code using TensorFlow on a GPU for speed. Utilized text generator library to help set parameters for the model. Once new cocktails are generated, plot before and after data in Tableau. Build Alexa Skill to ask for a new cocktail recipe. 
Used Alexa Skills Developer and AWS Lambda to build the Alexa skill



## DATA ANALYSIS-Questions
1. What is the relationship between median household income, education level and ATM location/number?
2. What relationships between population density and ATM number?
3. Are there relationships between ATM use fees and demographic variables?
4. Are there significant relationships between a demographic area and the types of ATMs found in that area?
5. We wanted to examine the placement of ATM machines in today’s banking landscape.  We wanted to understand who owned them, where they were placed, and what strategies owners use to place ATM machines today.
6. Who uses them & who owns them?
7. What can we learn about ATMs?

## Datasets Used:
Use over 500 cocktail recipes from the cocktail db on Kaggle.com


## Breakdown of Tasks:
1. Use RNN (Recurrent Neural Network) with LTSM (Long Short Term Model) to “learn” the data and produce new recipes
2. Used Colaboratory notebook on the Google Cloud platform to run python code. This allowed us to process the code using TensorFlow on a   GPU for speed.
3. Utilized Textgenrnn library to help set parameters for the model
4. Once new cocktails are generated, plot before and after data in Tableau
5. Build Alexa Skill to ask for a new cocktail recipe
6. Used Alexa Skills Developer and AWS Lambda to build the Alexa skill

## ATM Data Search Method:
Pulled 1000 random latitudes and longitudes in the Richmond region
Used Latitude and Longitude with Google’s API “near by me” to generate ATM name & street addresses
Google search had a 60 item limit
Used ATM addresses and Google’s Geo mapping to retrieve zip codes
First pull was 30 miles – 60 ATMs
Second pull was 100 3 mile radius pulls – 67 ATMs after dups
3rd pull was 200 3 mile radius pulls – 67 ATMs (none new)
4th pull of 1000 (1000 meter) pulls – 147 ATMs – maxing the 60 ATM limit
Census, pulled 2013-2017 using the same keys, choose to use the most current census data (2017)
First merged ATM onto the census data ultimately showing numerous null values for missing data
Changed the join to add census data into the ATM file, thus eliminating null values

## Obervation.

# Majority of ATMs located in zip codes with larger HHI >$100K
![GitHub Logo](/Bar_HHI_ATM.png)
# 60 percent of ATM are in zip codes with populations greater than 40,000 residents
![GitHub Logo](/Bar_Population_ATM.png)
# ATMs located in zip codes with rent between $700-$1150
![GitHub Logo](/Bar_Rent_ATM.png)
# Owners of ATM in RVA
![GitHub Logo](/Bar_long_ATM.png)

# Other Observation
50/50 split between bank and non-bank ATMs.  Expect that we are missing more non-bank owed ATMs than bank owned ATMs.
There is a major ATM strategy difference between the big banks Wells Fargo vs Sun Trust vs. Capital One.
Wells Fargo has 18 ATMS in the RVA area, compared to 8 and 2 for Sun Trust Bank and Capital One, respectively.

# Learning and Limitations
Ensure the data is joined in the right order, eliminating unnecessary nulls.
Be flexible and change approach as needed, data was difficult to get; not convinced we have a complete universe of ATM data
More time to spend with Master Card and Visa; still convinced this is possible, just not within our time frame or ability at this point
Relied on ATMs listed in Google;  assume large organizations and a few small entities list their ATMs in google. 

