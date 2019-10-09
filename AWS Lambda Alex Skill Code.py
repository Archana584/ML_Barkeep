#------------------------------Part1--------------------------------
# In this part we define a list that contains the alcohol
alcohol_LIST = ["rum", "vodka", "gin", "tequila", "beer", "specialty"]

cocktail_LIST = {"rum":["In a highball glass, mix 1 1/2 ounces light rum, 1 ounce pineapple juice, 1/2 teaspoon maraschino liqueur, and 1/2 teaspoon grenadine, 1 maraschino cherry, and juice of 1 orange",
"In an old-fashioned glass, mix 1 1/2 ounce light rum, 1 ounce apricot brandy, 1 teaspoon lemon juice, 1/2 teaspoon grenadine, and juice of 1/4 lemon",
"In a highball glass, combine 1 1/2 ounces light rum, 3 ounces triple sec, and 1 1/2 ounce sweet and sour, and 1 cherry",
"In a highball glass, 1 1/2 ounce light rum, 1 ounce pineapple juice, 1/2 teaspoon grenadine, 1 maraschino cherry, and 1 splash orange juice",
"In a champagne flute, combine 1 1/2 ounce light rum, 1 ounce pineapple juice, 1/2 teaspoon maraschino liqueur, and 1 teaspoon grenadine",
"In a highball glass, 1 1/2 ounce light rum, 1 ounce apricot brandy, and 1 teaspoon lemon juice",
"In a collins glass, mix 1 ounce light rum, 1 ounce pineapple juice, 1/2 teaspoon grenadine, 1 dash orange bitters, and 1 cherry",
"In a glass, mix 2 ounces bacardi 151 proof rum, 1 ounce dark creme de cacao, 1 oz cointreau, 3 ounces milk, 1 ounce coconut liqueur, and 1 cup vanilla cream over ice",
"In a champagne flute, mix 1 1/2 oz light rum, 1 oz pineapple juice, 1/2 tsp maraschino liqueur, 1/2 tsp grenadine, 1 maraschino cherry, 1 splash orange juice",
"In a collins glass, combine 1 oz campari, 1 oz light rum, 1 oz blue curacao, 1 oz lemon juice, and 1 splash sprite",
"In a highball glass, mix 1 1/2 oz light rum, 1 oz apricot brandy, 1 tsp lemon juice, 1/2 tsp grenadine, and 1 egg white",
"In a highball glass, mix 1 part malibu rum, 1 part creme de cassis, and 1 part lemon juice"],

"vodka":["In a highball glass, mix 1 ounce vodka, 1 oz blue curacao, a spash of lemonade, and 1 cherry",
"In a shot glass, combine 1/3 ounce vodka, 1/3 ounce midori melon liqueur, and 1/3 ounce sweet and sour",
"In a white wine glass, mix 1 ounce vodka, 2 ounce amaretto, and 1 ounce orange juice",
"In a punch bowl, combine 1 fifth everclear, 1 fifth smirnoff, 1 liter rum, 4 mountain dews, and l surge 1",
"In a shot glass, 1/3 ounce vodka, 1/3 ounce midori melon liqueur, 1/3 ounce sweet and sour",
"In a collins glass, 1 1/2 ounce absolut citron, 3/4 ounce sweet and sour, 1 twist lemon, and a splash lemon juice",
"In a collins glass, mix 1 1/2 ounce absolut vodka, 3/4 ounce cranberry juice, 1/4 ounce pineapple juice",
"In a collins glass, 1 1/2 oz absolut vodka, 3/4 oz cranberry juice, 1/4 oz pineapple juice"],

"gin":["In a cocktail glass, mix 1 1/2 oz Gin, 1/2 oz Triple sec, 1 oz Chambord raspberry liqueur, and 1 oz Cranberry juice.",
"In a collins glass, combine 1/2 ounce dry vermouth, 1 ounce gin, 1/4 teaspoon anis, 2 dashes orange bitters, and 1 maraschino cherry",
"In a cocktail glass, mix 1 1/2 ounce gin, 1 ounce ginger ale, 1 teaspoon benedictine",
"In a collins glass, mix 1 1/2 ounce gin, 2 teaspoon superfine sugar, 1 1/2 ounce lemon juice, 4 ounces chilled champagne, 1 splash orange juice, and 1 maraschino cherry",
"In a collins glass, mix 1 1/2 ounce gin, 2 teaspoons superfine sugar, 1 ounce club soda, 1 splash lemon, and 2 ounces grenadine",
"In a cocktail glass, 1 1/2 ounce gin, 2 teaspoon superfine sugar, 1 ounce club soda, 1 lemon wedge, 1/2 ounce maraschino liqueur, 1/2 ounce cherry brandy",
"In an old-fashioned glass, 1 1/2 ounce gin, 1/4 ounce maraschino liqueur, 1/4 ounce grand marnier, 2 teaspoon lemon juice, and 1 twist of lemon peel",
"In a cocktail glass, mix 1 1/2 ounce gin, 1/2 ounce triple sec, and 1 tablespoon lemon juice",
"In a cocktail glass, mix 1 1/2 ounce gin, 1 ounce triple sec, 1 ounce chambord raspberry liqueur, 1 ounce midori melon liqueur, and 1/2 ounce jägermeister, and 1/2 oz root beer",
"In a cocktail glass, mix 1 1/2 ounce gin, 1/2 ounce ginger wine, 1/2 ounce grenadine, 1/2 ounce triple sec, 1/2 ounce blue curacao, 1 dash bitters, 1 maraschino cherry, and 1 twist of lime",
"In a cocktail glass, mix 1 1/2 ounce gin, 1/2 ounce apricot brandy, 1/2 teaspoon lemon juice, 1 teaspoon grenadine, and powdered sugar",
"In a cocktail glass, 1 1/2 oz gin, 1/2 oz grand marnier, 2 tsp lemon juice, and 1 twist of lemon peel"],

"tequila":["In a shooter glass, mix 1/2 ounce tequila, 1/2 oz triple sec, 1 ounce lemon juice, 1 ounce strawberry scnapps, and salt the rim",
"In an old-fashioned glass, mix 4.5 ounces tequila, 1.5 ounces lime juice, and 2 spoons agave",
"In a highball glass, 1 ounce añejo, 1 ounce light rum, 1 ounce orange juice, 1/2 ounce lemon juice, 3 ounce ginger ale, and 1 twist of of peel",
"In a old-fashioned glass, 1 1/2 ounce añejo, 1/2 ounce cherry brandy, 1/2 ounce grenadine, 1 ounce light cream",
"In a collins glass, mix 1/2 oz tequila, 1/2 oz melon liqueur, and fill with mountain dew",
"In a glass, combine 1 1/2 oz tequila, 1 oz coconut liqueur, 1 oz sweet and sour, and 1 oz cherry"],

"beer":["In a beer mug, mix 1 bottle lager, and 1 1/2 ounces campari, and add a wedge of lime",
"In a pint glass, combine 1/2 pint lager, 1/2 pint sweet cider, and 1 ounce orange juice",
"In a pilsner glass, 1 corona and 1 shot bacardi limon",
"In a beer mug, combine 1 bottle lager, 1 1/2 ml campari, dash of cider, and splash of lime"],

"specialty":["In a highball glass, mix 1 ounce godiva liqueur, 1/2 ounce triple sec, 1/2 ounce vodka, and 1 ounce light cream",
"In a collins glass, mix 1/3 part kahlua, 1/3 part bailey's irish cream, 1/3 part frangelico",
"In a mason jar, mix 5 shots of Hot Damn!",
"In a shot glass, 1/2 ounce goldschlager and 1/2 ounce jägermeister",
"In a highball glass, 1 ounce southern comfort, 1 ounce amaretto, 1/2 ounce sloe gin, 1 ounce triple sec, 1 1/2 ounce chambord raspberry liqueur, and 1 ounce cranberry juice",
"In a highball glass, mix 2 ounces strawberry schnapps, 2 ounces orange juice, 2 ounces cranberry juice, and club soda",
"In a shot glass, mix 1/2 ounce jägermeister and 1/2 ounce root beer",
"In a shot glass, combine 1/2 ounce firewater, 1/2 ounce absolut peppar, and 1 dash tabasco sauce",
"In a collins glass, combine 1 oz campari, 1 oz light rum, 1 oz blue curacao, 1 oz lemon juice, and 1 splash sprite",
"In a old-fashioned glass, mix 6 ml prosecco, 4 ml campari, and a splash soda water",
"In a collins glass, mix 1/2 oz amaretto,  1/2 oz white creme de cacao, 2 oz light cream, and a dash nutmeg"]}
#------------------------------Part2--------------------------------
import random

# Here we define our Lambda function and configure what it does when 
# an event with a Launch, Intent and Session End Requests are sent. # The Lambda function responses to an event carrying a particular 
# Request are handled by functions such as on_launch(event) and 
# intent_scheme(event).
def lambda_handler(event, context):
    if event['session']['new']:
        on_start()
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event)
    elif event['request']['type'] == "IntentRequest":
        return intent_scheme(event)
    elif event['request']['type'] == "SessionEndedRequest":
        return on_end()
#------------------------------Part3--------------------------------
# Here we define the Request handler functions
def on_start():
    print("Session Started.")

def on_launch(event):
    onlunch_MSG = "Hi, welcome to the Machine Learning Barkeep. The types of alchohol we have are " + ', '.join(map(str, alcohol_LIST)) + ". "\
    "If you would like to hear a machine learning generated cocktail recipe, you could say for example: tell me a rum cocktail."
    reprompt_MSG = "Do you want to hear a cocktail recipe?"
    card_TEXT = "You can choose rum, vodka, gin, tequila, beer, or specialty."
    card_TITLE = "Choose an alcohol type."
    return output_json_builder_with_reprompt_and_card(onlunch_MSG, card_TEXT, card_TITLE, reprompt_MSG, False)

def on_end():
    print("Session Ended.")
#-----------------------------Part3.1-------------------------------
# The intent_scheme(event) function handles the Intent Request. 
# Since we have a few different intents in our skill, we need to 
# configure what this function will do upon receiving a particular 
# intent. This can be done by introducing the functions which handle 
# each of the intents.
def intent_scheme(event):
    
    intent_name = event['request']['intent']['name']

    if intent_name == "newCocktail":
        return new_cocktail(event)        
    elif intent_name in ["AMAZON.NoIntent", "AMAZON.StopIntent", "AMAZON.CancelIntent"]:
        return stop_the_skill(event)
    elif intent_name == "AMAZON.HelpIntent":
        return assistance(event)
    elif intent_name == "AMAZON.FallbackIntent":
        return fallback_call(event)
#---------------------------Part3.1.1-------------------------------
# Here we define the intent handler functions
def new_cocktail(event):
    name=event['request']['intent']['slots']['alcohol']['value']
    alcohol_list_lower=[w.lower() for w in alcohol_LIST]
    if name.lower() in alcohol_list_lower:
        reprompt_MSG = "Do you want to hear a cocktail from a type of alcohol?"
        card_TEXT = "You've picked " + name.lower()
        card_TITLE = "You've picked " + name.lower()
        return output_json_builder_with_reprompt_and_card(random.choice(cocktail_LIST[name.lower()]), card_TEXT, card_TITLE, reprompt_MSG, False)
    else:
        wrongname_MSG = "You haven't used an available type of alcohol. If you have forgotten which alcohol you can pick say help."
        reprompt_MSG = "Do you want to hear a cocktail from a type of alcohol?"
        card_TEXT = "Use the alcohol type."
        card_TITLE = "Wrong name."
        return output_json_builder_with_reprompt_and_card(wrongname_MSG, card_TEXT, card_TITLE, reprompt_MSG, False)
        
def stop_the_skill(event):
    stop_MSG = "Thank you for visiting. Drink Responsibly."
    reprompt_MSG = ""
    card_TEXT = "Bye."
    card_TITLE = "Bye Bye."
    return output_json_builder_with_reprompt_and_card(stop_MSG, card_TEXT, card_TITLE, reprompt_MSG, True)
    
def assistance(event):
    assistance_MSG = "You can choose among these alcohol types: " + ', '.join(map(str, alcohol_LIST)) + "."
    reprompt_MSG = "Do you want to hear a cocktail from a type of alcohol?"
    card_TEXT = "You've asked for help."
    card_TITLE = "Help"
    return output_json_builder_with_reprompt_and_card(assistance_MSG, card_TEXT, card_TITLE, reprompt_MSG, False)

def fallback_call(event):
    fallback_MSG = "I can't help you with that, try rephrasing the question or ask for help by saying HELP."
    reprompt_MSG = "Do you want to hear a cocktail from a type of alcohol?"
    card_TEXT = "You've asked a wrong question."
    card_TITLE = "Wrong question."
    return output_json_builder_with_reprompt_and_card(fallback_MSG, card_TEXT, card_TITLE, reprompt_MSG, False)
#------------------------------Part4--------------------------------
# The response of our Lambda function should be in a json format. 
# That is why in this part of the code we define the functions which 
# will build the response in the requested format. These functions
# are used by both the intent handlers and the request handlers to 
# build the output.
def plain_text_builder(text_body):
    text_dict = {}
    text_dict['type'] = 'PlainText'
    text_dict['text'] = text_body
    return text_dict

def reprompt_builder(repr_text):
    reprompt_dict = {}
    reprompt_dict['outputSpeech'] = plain_text_builder(repr_text)
    return reprompt_dict
    
def card_builder(c_text, c_title):
    card_dict = {}
    card_dict['type'] = "Simple"
    card_dict['title'] = c_title
    card_dict['content'] = c_text
    return card_dict    

def response_field_builder_with_reprompt_and_card(outputSpeach_text, card_text, card_title, reprompt_text, value):
    speech_dict = {}
    speech_dict['outputSpeech'] = plain_text_builder(outputSpeach_text)
    speech_dict['card'] = card_builder(card_text, card_title)
    speech_dict['reprompt'] = reprompt_builder(reprompt_text)
    speech_dict['shouldEndSession'] = value
    return speech_dict

def output_json_builder_with_reprompt_and_card(outputSpeach_text, card_text, card_title, reprompt_text, value):
    response_dict = {}
    response_dict['version'] = '1.0'
    response_dict['response'] = response_field_builder_with_reprompt_and_card(outputSpeach_text, card_text, card_title, reprompt_text, value)
    return response_dict