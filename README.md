# Eclectus Bot

**A free and customizable cross-platform chatbot!**

Eclectus Bot runs on a free Heroku account and currently works on these messaging platforms:

 - Telegram
 - GroupMe

Also, a shout out to [Apnorton](https://github.com/apnorton) and his [Bloom Bot tutorial](https://www.apnorton.com/blog/2017/02/28/How-I-wrote-a-Groupme-Chatbot-in-24-hours), from which this code is forked.

## Installation Process

[This video tutorial](https://youtu.be/WdL85GmZQFg) has been created to show how to set up the Heroku project, as well as the necessary config variables and bot config files.

Some useful resources:

- [Git Bash (Windows)](https://git-scm.com/download/win)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
- [Heroku](https://dashboard.heroku.com/apps)
- [JSON Validator](https://jsonlint.com/)

#### Telegram Specific Resources

 - [Setting up Telegram specific Config Variables](https://youtu.be/N33ggcuEyI0)
 - [Setting up the bot's webhook](https://medium.com/@xabaras/setting-your-telegram-bot-webhook-the-easy-way-c7577b2d6f72)
 - Webhook URL "Template": `https://api.telegram.org/bot{my_bot_token}/setWebhook?url={url_to_send_updates_to}`

#### GroupMe-Specific Resources

 - [Setting up GroupMe Config Variables](https://youtu.be/H5HyYMIg-bs)
 - [GroupMe Developer's Page](https://dev.groupme.com/bots)

## Required Heroku Environment Variables (Config Vars)

 - All platforms
    - `BOT_NAME` - The name of your bot

 - Telegram
    - `telegram_token` - API token for your bot (Format: XXXXXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX)

 - GroupMe
    - `gm_dev_group` - Group ID for the "Dev Room" chat (Format: XXXXXXXX)
    - `GM_DEV_BOT_ID` - Bot ID for the "Dev Room" chat (Format: XXXXXXXXXXXXXXXXXXXXXXXXXX)

    - `gm_primary_group` - Group ID for the chat group with your friends (Format: XXXXXXXX)
    - `GM_PRIMARY_BOT_ID` - Bot ID for the chat group with your friends (Format: XXXXXXXXXXXXXXXXXXXXXXXXXX)


## Local Testing

You can run `/app.py` to open a "chat prompt", simulate sending messages to Eclectus, and view its response. It doesn't simulate extracting the chat message from the data received by different messaging platforms, so this is mainly useful for testing your custom commands or new modules.

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

The avatar is a pixel art image of the bird, based on the [photo](https://en.wikipedia.org/wiki/Eclectus_parrot#/media/File:Eclectus_roratus-20030511.jpg) taken by [Doug Janson](https://commons.wikimedia.org/wiki/User:Dougjj). The Eclectus Bot avatar is available under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
