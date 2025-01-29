import json

defaultJson = [
    {"Bot Name 1": "Token 0"},
    {"Bot Name 2": "Token 1"},
    {"These are just": "Token 2"},
    {"bot names that": "Token 3"},
    {"only you see": "Token 4"},
    {"from your terminal": "Token 5"},
    {"can be anything": "Token 6"}
]

def confirm(botNumber:int, botName:list):
    answerConfirm = input(f'You have selected "{botName[botNumber]}", is this the right choice? (Y/N) ')
    if answerConfirm.lower() == "y":
        return True
    elif answerConfirm.lower() == "n":
        return False
    else:
        print("Invalid answer.")

def askWhichBot(botCount:int, botList:str):
    errorNoBot = f"\nNo bot goes by that number!\n"
    while True:
        try:
            print(f"Which bot to select:\n{botList}")
            botNumber = int(input("Enter the number: "))
            if (botNumber > -1) and (botNumber < botCount+1):
                return botNumber
            else:
                print(errorNoBot)
        except ValueError:
            print(errorNoBot)

def select(force:bool=False, whichBot:int=-1):

    try:
        with open("botTokens.json", "r") as botTokensFile: # Check camelCase first
            rawTokens = json.load(botTokensFile)
    except FileNotFoundError:
        try:
            with open("bot_tokens.json", "r") as botTokensFile: # Only if no camelCase check snake_case (Because backwards compatibility blah blah)
                rawTokens = json.load(botTokensFile)
        except FileNotFoundError:
            with open("botTokens.json", "w") as botTokensFile:
                json.dump(defaultJson, botTokensFile, indent=4)
                raise SystemExit('"botTokens.json" file was created. Please place your tokens in there and try again.')
                
    botName = [list(obj.keys())[0] for obj in rawTokens]
    botToken = [list(obj.values())[0] for obj in rawTokens]

    botList=""
    botCount=-1
    for name in botName:
        botCount += 1
        botList += f'   ({botCount}) "{name}"'
        if name == botName[-1]:
            botList += "?"
        else:
            botList += f", \n"

    if whichBot < -1 and whichBot > botCount:
        raise SystemExit(f"Invalid bot number. Please select a bot from 0 to {botCount}.")
    elif force == False and whichBot == -1:
        while True:
            botNumber = askWhichBot(botCount, botList)
            if confirm(botNumber, botName):
                return f"{botToken[botNumber]}"
    elif force == False and whichBot != -1:
        while True:
            confirmBool=confirm(whichBot, botName)
            if confirmBool:
                return f"{botToken[whichBot]}"
            elif confirmBool == False:
                break
        while True:
            botNumber = askWhichBot(botCount, botList)
            if confirm(botNumber, botName):
                return f"{botToken[botNumber]}"
    elif force == True and whichBot != -1:
        return f"{botToken[whichBot]}"
    elif force == True and whichBot == -1:
        return f"{botToken[askWhichBot(botCount, botList)]}"
    else:
        raise SystemExit("Something went wrong.")

# By Milopan
# https://github.com/khan-milopan/Discord-Bot-Token-Selector