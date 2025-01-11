import json

def select():
    with open("bot_tokens.json", "r") as bot_tokens_file:
        raw_tokens = json.load(bot_tokens_file)
    botName = [list(obj.keys())[0] for obj in raw_tokens]
    botToken = [list(obj.values())[0] for obj in raw_tokens]
    botList=""
    botCount=-1
    for name in botName:
        botCount += 1
        botList += f'{name}({botCount})'
        if name == botName[-1]:
            botList += "?"
        else:
            botList += ", "
    while True:
        try:
            print(f"Which bot to select: {botList}")
            answer = int(input("(Enter the number): "))
            if 0 <= answer < len(raw_tokens):
                answerConfirm = input(f'You have selected "{botName[answer]}", do I select it? (Y/N) ')
                if answerConfirm.lower() == "y":
                    chosenToken = f"{botToken[answer]}"
                    return chosenToken
                elif answerConfirm.lower() == "n":
                    continue
                else:
                    print("Invalid answer.")
                    continue
        except ValueError:
            print("No bot goes by that number.")

# By Milopan (and TheGamer29/jacopicic)
# https://github.com/khan-milopan/Discord-Bot-Token-Selector