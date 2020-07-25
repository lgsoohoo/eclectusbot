# Meme Commands
# Commands with return a static image/gif response
# Requires a `/module_config/memeCommand_config.json` config file.
#   - Animations (gifs) are expected to have the substring
#       "gif" in the link, and pictures should not have "gif" in the link.
#   - GroupMe requires images to be sent though their image service before a bot can post them.
#       The simplest way is to post them in a private group chat first, and then add the GroupMe URL
#       to the config file. This is unnecessary if the bot is not going to be used on GroupMe.
#   - Config file scheme:
#       {
#           "cmd_responses": {
#               "!pictureCmd": "https://i.groupme.com/800x450.jpeg.a1234567890.large",
#               "!animationCmd": "https://i.groupme.com/320x320.gif.a123456789"
#           }
#       }

import sys
import json


class MemeCommand:
    # ========== Static Members ==========
    # List of commands
    cmds = []

    # Responses to commands
    __cmd_responses = {}

    # Load commands from file
    config_filename = './module_config/memeCommand_config.json'
    try:
        with open(config_filename, encoding="utf-8") as config_file:
            config_data = json.load(config_file)
            __cmd_responses = config_data["cmd_responses"]
            cmds = list(__cmd_responses.keys())
    except:
        sys.stderr.write(
            "MemeCommand: Error loading commands from "+config_filename+".\n")

    # ========== Functions ==========

    # @param input - String - (Group Chat User's) input message
    #
    # @returns - None, or String - link to an image
    def respond(self, input):
        for word in input.split(" "):
            for cmd in self.cmds:
                if word == cmd:
                    return self.__cmd_responses[word]

        return None
