# Discord Bot Token Selector
Created by [Milopan](https://github.com/khan-milopan) with teeny-tiny help from [TheGamer29](https://github.com/jacopicic).

This Python script reads the contents of `botTokens.json` containing the names and tokens of your Discord bots, after which it asks you which one you wanna choose and it returns the token of the bot that you chose.

If using Pycord, you would place the `botSelect.py` and `botTokens.json` into the same folder as your `main.py` (or whichever file you're running your bot from) and you'd add the following:
```python
import botSelect
bot.run(botSelect.select())
```

You can add or remove bots and their tokens by editing `botTokens.json` where you would create a new object with the key being the name of your Discord bot while the value being that bot's token.
Example:
```json
{"Bot's name": "Bot's token... blah blah blah"},
{"Another bot's name": "Another token... 69 420 Big Chungus"}
```

I hope you find this useful <3 - Milopan