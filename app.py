import os
import sys
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, request

from bot.systemTools import SystemTools
from bot.textCommand import TextCommand
from bot.memeCommand import MemeCommand
from bot.chatBot import ChatBot
from bot.tabletopRPG import TabletopRPG
from bot.magic8Ball import Magic8Ball

app = Flask(__name__)
bot_systemTools = SystemTools()
bot_chatBot = ChatBot()

# Log messages to console for debug
# @param msg - string to log
def log(msg):
    print(str(msg)+'\n')
    sys.stdout.flush()

# HTTP POSTs a message to the group chat
# @param json_data - dictionary - containing the data to POST
# @param bot_url - string - url to POST
def send_message(json_data, bot_url):
    # Supposedly these two codes do the same thing, but each only work in 1 platform.
    # It's kinda late, we'll figure out why later
    if "telegram" in bot_url:
        url = bot_url
        request = Request(url, urlencode(json_data).encode())
        res = urlopen(request).read().decode()
        log(res)
    else: # groupme
        # https://stackoverflow.com/a/7469725
        payload = json.dumps(json_data).encode('utf-8')
        url = bot_url
        post_req = Request(url, payload)
        res = urlopen(post_req).read().decode()
        log(res)

# Takes a raw message and sends back the bot's response
# @param sender - String - name of sender
# @param user_input_raw - String - raw message sent by sender
#
# @returns - Dictionary - Bot's response, either under the "text" or "picture_url"
def msg2bot_response(sender, user_input_raw):
    user_input_normalized = bot_systemTools.normalizeText(user_input_raw)

    # The bot's response (text or image attachment)
    response = {}

    # Help Commands
    if bot_systemTools.check_usage(bot_systemTools.cmds, user_input_raw):
        response["text"] = bot_systemTools.respond()

    # Text Commands
    elif bot_systemTools.check_usage(TextCommand().cmds, user_input_normalized):
        response["text"] = TextCommand().respond(user_input_normalized)

    # Meme Commands
    elif bot_systemTools.check_usage(MemeCommand().cmds, user_input_normalized):
        response["picture_url"] = MemeCommand().respond(user_input_normalized)

    # Tabletop RPG Commands
    elif bot_systemTools.check_usage(TabletopRPG().cmds, user_input_normalized):
        response["text"] = TabletopRPG().respond(user_input_raw, sender) 
        # Raw input is sent to include parenthesis in original message

    # Magic 8 Ball RPG Commands
    elif bot_systemTools.check_usage(Magic8Ball().cmds, user_input_normalized):
        response["text"] = Magic8Ball().respond()

    # ChatBot Comments
    else:
        response["text"] = ChatBot().respond(user_input_normalized)

    return response

# ========== Messaging Platforms Webhooks ==========

groupme_primary_token = os.getenv('GM_DEV_BOT_ID')
if not groupme_primary_token is None:
    @app.route('/groupme', methods=['POST'])
    def groupme_webhook():
        # === The Setup ===
        data = request.get_json()
        log('Groupme - Received {}\n'.format(data))

        # Check if it is from the primary group chat or the devroom, then choose which BOT_ID to use
        bot_id = 0
        gm_primary_group = os.getenv('gm_primary_group')
        gm_dev_group = os.getenv('gm_dev_group')
        if not gm_dev_group is None and int(data['group_id']) == int(gm_dev_group):
            bot_id = os.getenv('GM_DEV_BOT_ID')
        elif not gm_primary_group is None and int(data['group_id']) == int(gm_primary_group):
            bot_id = os.getenv('GM_PRIMARY_BOT_ID')
        else:
            return "Groupme - Error: Unknown groupme group id ("+data['group_id']+").", 200

        bot_response = msg2bot_response(data['name'], data['text'])

        # === Exit if bot is not needed ===
        if not "picture_url" in bot_response.keys() and bot_response["text"] is None:
            return "Groupme - Ok: Didn't need bot.", 200

        # === Should we send messages? ===
        # Only send message if we have the system environment variable (we're on Heroku)
        if bot_id is None:
            # Local Debug mode:
            log("Groupme - Debug mode: "+str(bot_response))

        elif data['sender_type'] != "bot":
            # Production mode
            # Don't respond to (ourself and other) bots. Make sure we have an id.
            log("Groupme - Production mode: "+str(bot_response))

            bot_response["bot_id"] = bot_id

            send_message(bot_response, 'https://api.groupme.com/v3/bots/post')
        else:
            # Another bot
            log("Groupme - Another bot. Msg not sent:"+str(bot_response))

        return "Groupme - Ok:"+str(bot_response), 200


telegram_token = os.getenv('telegram_token')
if not telegram_token is None:
    @app.route('/telegram', methods=['POST'])

    def telegram_webhook():
        # === The Setup ===
        data = request.get_json()
        log('Telegram - Received {}\n'.format(data))

        user_message = {}
        if 'message' in data:
            user_message = data['message']
        elif 'edited_message' in data:
            user_message = data['edited_message']

        if not 'text' in user_message:
            return "Telegram - No 'text' field:"+str(data), 200

        bot_response = msg2bot_response(user_message['from']['first_name'], user_message['text'])

        # === Exit if bot is not needed ===
        if not "picture_url" in bot_response.keys() and bot_response["text"] is None:
            return "Telegram - Ok: Didn't need bot.", 200

        # === Should we send messages? ===
        if not user_message['from']['is_bot']:
            # Don't respond to (ourself and other) bots.
            # Telegram doesn't forward msg's from bots to other bots anyways,
            #  but we'll just check anyway.
            log("Telegram - Production mode: "+str(bot_response))

            # What to POST back
            json_data = {
                "chat_id": user_message['chat']['id'],
                "disable_notification": True,
            }

            if "picture_url" in bot_response.keys():
                imageurl = bot_response['picture_url']

                if "gif" in imageurl:   # Gif
                    json_data.update({
                        'animation': imageurl,
                        # 'caption':'Check it out!'
                    })

                    send_message(json_data, 'https://api.telegram.org/bot' +
                                telegram_token+'/sendAnimation')
                
                else:   # Picture
                    json_data.update({
                        'photo': imageurl,
                        # 'caption':'Check it out!'
                    })

                    send_message(json_data, 'https://api.telegram.org/bot' +
                                telegram_token+'/sendPhoto')

            else:  # Text
                json_data.update({'text': bot_response['text']})
                send_message(json_data, 'https://api.telegram.org/bot' +
                            telegram_token+'/sendMessage')
        else:
            # Another bot
            log("Telegram - Another bot. Msg not sent:"+str(bot_response))

        return "Telegram - Ok:"+str(bot_response), 200

# ========== Main ==========

if __name__ == "__main__":
    print("Bot is ready. Press Ctrl+C to exit.")
    text_msg = 'Hello there'
    while not text_msg == 'q' and not text_msg == 'exit':
        text_msg = input("\tChat > ")
        res = msg2bot_response("Dev", text_msg)
        print("\t\t"+str(res))
