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

## ML barkeep TextGenRNN Code

![GitHub Logo](/ML%20Barkeep%20TextGenRNN%20code.PNG)

# Visualization of data in Tableau
![GitHub Logo](/before%20glass.PNG)

![GitHub Logo](/after%20glass.PNG)

![GitHub Logo](/Before%20drink.PNG)

![GitHub Logo](/after%20drink.PNG)

![GitHub Logo](/Alexa%20Skill%20Testing.png)

# Future State
1. Add more cocktails for different results
2. Add name generator to Alexa skill to come up with fun names on the fly
3. Build personalized recipes based on a person’s favorite cocktails
