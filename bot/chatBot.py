# Chat Bot
# Bot will read the message and pick out something to comment on.
# Requires the `BOT_NAME` environment variable to be set to the name of your bot.
# Requires chatbot config files:
#   - Keys (ex: uniquekeyname) can be anything you want, as long as both files have a
#       matching entry. (The bot will never print the key.)
#   - Depending on the messaging platform, images (urls) in the response may appear as URL's, an actual image, or both.
#   - Using the same trigger words for multiple entries may cause issues, depending on whether they written are earlier or later in the file.
#       For example, if "hello"->"Hiya! is written in the file before than "hello there"->"General Kenobi!", then if the user sends
#       "hello there, fellow jedi", the bot will respond with "Hiya!" because the bot matched "hello" before it could match "hello there".
#       A solution might be to list more complicated triggers earlier in the file.
#
#   - '/module_config/chatBot_trigger_config.json' config file scheme:
#       {
#           "triggerWords2switch_dict": {
#               "uniquekeyname": ["text2search4", "text to search for 2"]
#           }
#       }
#
#   - '/module_config/chatBot_response_config.json' config file scheme:
#       {
#           "switch2response_dict": {
#               "uniquekeyname": ["Bot Response 1", "Alternate Response"]
#           }
#       }


import random
import os
import sys
import json


class ChatBot:
    # ========== Static Members ==========
    # The name of your bot
    bot_name = os.getenv("BOT_NAME")
    bot_name = "a bot" if bot_name is None else str(bot_name)

    # These two dictionaries work together to form an enhanced dictionary/key-value paring, where a group of keys are matched with a group of values.
    # triggerWords2switch_dict's values act as the multiple "keys", and switch2response_dict's values act as the multiple "values".
    # The matching keys in triggerWords2switch_dict and switch2response_dict provide the link between the two dictionaries.

    # The bot will look for any of the "trigger words" (from triggerWords2switch_dict) in the message,
    #   and respond with any of the "possible responses" (from switch2response_dict).

    __triggerWords2switch_dict = {
        # Format    "switch"    : ["trigger_word_1", "trigger_word_2"]
        "starwars_kenobi": ["hello there", "general kenobi", "bold one"],
        "bot_greetings": ["hello", "hi", "howdy", "how are you", "whats up", "greetings", "hiya", "bot"],

    }

    __switch2response_dict = {
        # Format    "switch" : ["possible_response_1", "possible_response_2"]
        "starwars_kenobi": ["General Kenobi!", "You are a bold one!"],
        "bot_greetings": ["Hello!", "Hi!", "Howdy!", "How are you?", "What's up?", "Greetings!", "Hiya!", "Hi, I'm "+bot_name+"!"],
    }

    # Load additional triggers/responses from file
    trigger_config_filename = './module_config/chatBot_trigger_config.json'
    response_config_filename = './module_config/chatBot_response_config.json'
    try:
        with open(trigger_config_filename, encoding="utf-8") as config_file:
            config_data = json.load(config_file)
            __triggerWords2switch_dict.update(
                config_data["triggerWords2switch_dict"])
    except:
        sys.stderr.write(
            "ChatBot: Error loading triggers from "+trigger_config_filename+".\n")
    try:
        with open(response_config_filename, encoding="utf-8") as config_file:
            config_data = json.load(config_file)
            __switch2response_dict.update(config_data["switch2response_dict"])
    except:
        sys.stderr.write(
            "ChatBot: Error loading responses from "+response_config_filename+".\n")

    # ========== Functions ==========

    # Given a message, returns the bot's response
    # @param msg - String - (Group Chat User's) input message
    #
    # @returns - None or String - The bot's response
    def respond(self, msg):
        switch = self.__msg2sw(msg)
        if switch is None or not switch in self.__switch2response_dict:
            # Switch not found or chatBot_response_config.json is missing the response
            return None
        return self.__switch2response(switch)

    # Message to Switch
    # Converts a user's message to a Switch
    # @param msg - String - (Group Chat User's) input message
    #
    # @returns Switch - identified from the message / `None` - if none found
    def __msg2sw(self, msg):
        # A list of all switches
        all_switches = list(self.__triggerWords2switch_dict.keys())
        for sw in all_switches:
            if self.__if_uses_switch(msg, sw):
                return sw
        return None

    # Indicates if the Switch applies to the message
    #  - Switch's trigger words WITHOUT spaces WILL NOT match substrings in the message
    #  - Switch's trigger words WITH    spaces WILL     match substrings in the message
    # @param msg - String - (Group Chat User's) input message
    # @param sw - Switch to get trigger_words from
    #
    # @returns Boolean - if `msg` contains any of the trigger words in `sw`
    def __if_uses_switch(self, msg, sw):
        # for each of sw's trigger words
        for trigger_word in self.__triggerWords2switch_dict[sw]:
            if " " in trigger_word:
                if trigger_word in msg:
                    return True
            else:
                # Match full words, not substrings
                # ` "hi" in "think" ` returns True. We DON'T want this to happen
                splitted_msg = msg.split(" ")
                for word in splitted_msg:
                    if trigger_word == word:
                        return True
        return False

    # Switch to Response
    # Uses a switch to generate a response
    # @param sw - A switch from above (String)
    #
    # @returns - String - A random response based on the switch
    def __switch2response(self, sw):
        list_of_responses = self.__switch2response_dict[sw]
        return random.choice(list_of_responses)
