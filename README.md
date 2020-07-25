# Eclectus Bot

**A cross-platform messaging service chatbot!**

Eclectus runs on Heroku and currently works on these messaging platforms:

 - GroupMe
 - Telegram

Also, a shout out to [Apnorton](https://github.com/apnorton) and his [Bloom Bot tutorial](https://www.apnorton.com/blog/2017/02/28/How-I-wrote-a-Groupme-Chatbot-in-24-hours), from which this code is forked.

## Required Heroku Environment Variables (Config Vars)

 - All platforms
    - `BOT_NAME` - The name of your bot
 - GroupMe
    - `gm_dev_group` - Group ID for the "Dev Room" chat (Format: XXXXXXXX)
    - `GM_DEV_BOT_ID` - Bot ID for the "Dev Room" chat (Format: XXXXXXXXXXXXXXXXXXXXXXXXXX)

    - `gm_primary_group` - Group ID for the chat group with your friends (Format: XXXXXXXX)
    - `GM_PRIMARY_BOT_ID` - Bot ID for the chat group with your friends (Format: XXXXXXXXXXXXXXXXXXXXXXXXXX)

 - Telegram
    - `telegram_token` - API token for your bot (Format: XXXXXXXXXX:XXXXXXXXX-XXXXXXXX-XXXXXXXXXXXXXXXX)

## Local Testing

You can run `/app.py` to open a "chat prompt", simulate sending messsages to Eclectus, and view its response. It doesn't simulate extracting the chat message from different messaging platforms, so it's mainly useful for testing your custom commands or new modules.

```
    $ python3 app.py 
    Bot is ready. Press Ctrl+C to exit.
        Chat > Hello World!
                {'text': 'Hiya!'}
        Chat > Hello Eclectus Bot!
                {'text': "Hi, I'm a bot!"}
        Chat > Lets !flip a coin
                {'text': 'Dev flips a coin. It landed on heads!'}
```

## What does "Eclectus" mean?

Eclectus Bot is named after the Eclectus Parrot. You can read more about them over on their [Wikipedia page](https://en.wikipedia.org/wiki/Eclectus_parrot).

The avatar is a pixel art version of the bird, based off of a [photo](https://en.wikipedia.org/wiki/Eclectus_parrot#/media/File:Eclectus_roratus-20030511.jpg) taken by [Doug Janson](https://commons.wikimedia.org/wiki/User:Dougjj). The avatar image is available under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).