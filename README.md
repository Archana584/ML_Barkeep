# Project 3
### Team Members:
Archana, Allison, Jacky

### ML_Barkeep
Using machine learning to create new cocktails

## Datasets Used:
Use over 500 cocktail recipes from the cocktail db on Kaggle.com


## Breakdown of Tasks:
1. Use RNN (Recurrent Neural Network) with LTSM (Long Short Term Model) to “learn” the data and produce new recipes
2. Used Colaboratory notebook on the Google Cloud platform to run python code. This allowed us to process the code using TensorFlow on a   GPU for speed.
3. Utilized Textgenrnn library to help set parameters for the model
4. Once new cocktails are generated, plot before and after data in Tableau
5. Build Alexa Skill to ask for a new cocktail recipe
6. Used Alexa Skills Developer and AWS Lambda to build the Alexa skill

## RNN AND LTSM
You are able to use RNN and LTSM a huge check of text and ask it to model the probability distribution of the next item in the sequence
It tries to emulate the way humans learn.
We don’t read one word and forget it. It can keep previous information to simulate learning context. IT is a network with loops in them that allows previous information to persist.
LTSM is a special kind of RNN that is capable of learning long term dependencies.
Consists of memory containing cell, input gate, and output gate
Input gate tries to learn the weights of the connections in the data. Keeps the relevant data as memory and drops the non-important.




## Obervation.

# Visualization of data in Tableau
![Alt text](/../tableau_MLbarkeep/after drink.png
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

