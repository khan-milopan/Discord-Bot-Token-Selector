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

def select():
    checkJsonLoaded = False

    try:
        with open("botTokens.json", "r") as botTokensFile: # Check camelCase first
            rawTokens = json.load(botTokensFile)
            checkJsonLoaded = True
    except FileNotFoundError:
        try:
            with open("bot_tokens.json", "r") as botTokensFile: # Only if no camelCase check snake_case (Because backwards compatibility blah blah)
                rawTokens = json.load(botTokensFile)
                checkJsonLoaded = True
        except FileNotFoundError:
            jsonQuestionCreate = input('There is no "botTokens.json", do you wish to create one? (Y/N) ')
            if jsonQuestionCreate.lower() == "y":
                with open("botTokens.json", "w") as botTokensFile:
                    json.dump(defaultJson, botTokensFile, indent=4)
                    print('"botTokens.json" file was created. Please place your tokens in there and try again.')
                
    if checkJsonLoaded:
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
        
        error=f"\nNO BOT GOES BY THAT NUMBER!!!\n"
        while True:
            try:
                print(f"Which bot to select:\n{botList}")
                answerNumber = int(input("Enter the number: "))
                if (answerNumber > -1) and (answerNumber < botCount+1):
                    answerConfirm = input(f'You have selected "{botName[answerNumber]}", is this the right choice? (Y/N) ')
                    if answerConfirm.lower() == "y":
                        chosenToken = f"{botToken[answerNumber]}"
                        return chosenToken
                    elif answerConfirm.lower() == "n":
                        continue
                    else:
                        print("Invalid answer.")
                        continue
                else:
                    print(error)
            except ValueError:
                print(error)

# By Milopan
# https://github.com/khan-milopan/Discord-Bot-Token-Selector