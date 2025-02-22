# Discord Bot Token Selector
Created by [Milopan](https://github.com/khan-milopan) with teeny-tiny help from [TheGamer29](https://github.com/lowtiercompsci).

This Python script reads the contents of `bot_tokens.json` containing a list of bot names and their tokens, then prompts you to select one and returns the chosen bot's token.

If using Pycord, you would place the `bot_select.py` and `bot_tokens.json` into the same folder as your `main.py` (or whichever file you're running your bot from) and you'd add the following:
```python
import bot_select
bot.run(bot_select.select())
```

You can add or remove bots and their tokens by editing `bot_tokens.json` where you would create a new object with the key being the name of your Discord bot while the value being that bot's token.
Example:
```json
{"Bot's name": "Bot's token... blah blah blah"},
{"Another bot's name": "Another token... 69 420 Big Chungus"}
```

## "*force*" and "*which_bot*" parameters
These two parameters make your process of choosing a bot token quicker.
- The `force` parameter is a boolean and by default set to `false`, it skips the `You have selected X, is this the right choice?` question.
- The `which_bot` parameter is an integer and by default set to `-1`, it automatically selects a bot from the list.

I hope you find this useful <3 - Milopan
