# Telegram Bot

A low-requirements Telegram-API-wrapper for your bot to respond to messages

<img src="https://raw.githubusercontent.com/slovanos/images/master/joeybot.jpg" width=300>

https://github.com/slovanos/tgbot

**The current sample implementation returns wikipedia summary information**

## Requirements:

- requests>=2.31.0
- wikipedia==(1, 4, 0)

The wikipedia module is only necessary for the sample reaction implementation, not necessary for the actual bot.


## Usage:

- Create/Fill parameters.py with the necessary IDs from your bot and required constants on the main file.

### Run the sample implementation:

- Create/Fill ./data/rtas.txt with the alternative answers. One answer per line.

Run:

```shell
$ python3 tgbot.py
```

### Import the bot wrapper for your own usage:

```python
from botwrapper import TelegramBot
```

### Bye
