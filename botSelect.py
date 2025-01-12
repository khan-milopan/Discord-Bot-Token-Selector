import json

def select():
    try:
        with open("botTokens.json", "r") as bot_tokens_file: # Check camelCase first
            raw_tokens = json.load(bot_tokens_file)
    except FileNotFoundError:
        with open("bot_tokens.json", "r") as bot_tokens_file: # Only if no camelCase check snake_case (Because backwards compatibility blah blah)
            raw_tokens = json.load(bot_tokens_file)
    
    botName = [list(obj.keys())[0] for obj in raw_tokens]
    botToken = [list(obj.values())[0] for obj in raw_tokens]

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

# By Milopan (and TheGamer29/jacopicic)
# https://github.com/khan-milopan/Discord-Bot-Token-Selector