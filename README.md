# Discord Bot Token Selector
Created by [Milopan](https://github.com/khan-milopan) with tiny tiny help from [TheGamer29](https://github.com/jacopicic).

This is a python script that when ran reads the contents of `bot_tokens.json` containting the names and tokens of your Discord bots, after which it asks you which one you wanna choose and it returns the token of the bot that you chose.

If using Pycord, you would place the `botSelect.py` and `bot_tokens.json` into the same folder as your `main.py` (or whichever file you're running your bot from) and you'd add this the following:
```python
import botSelect
bot.run(botSelect.select())
```

You can add or remove bots and their tokens by editing `bot_tokens.json` where you would create a new object with the key being the name of your Discord bot while the value being that bot's token.
Example:
```json
{"Bot's name": "Bot's token... blah blah blah"},
{"Another bot's name": "Another token... 69 420 Big Chungus"}
```

I hope you find this useful <3 - Milopan