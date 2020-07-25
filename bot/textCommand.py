# Text Commands
# Commands which return a static Text response
# Requires a `/module_config/textCommand_config.json` config file.
#   - Config file scheme:
#       {
#           "cmd_responses": {
#               "!textCmd": "Static response"
#           }
#       }


import sys
import json


class TextCommand:
    # ========== Static Members ==========
    # List of commands
    cmds = []

    # Responses to commands
    __cmd_responses = {}

    # Load commands from file
    config_filename = './module_config/textCommand_config.json'
    try:
        with open(config_filename, encoding="utf-8") as config_file:
            config_data = json.load(config_file)
            __cmd_responses = config_data["cmd_responses"]
            cmds = list(__cmd_responses.keys())
    except:
        sys.stderr.write(
            "TextCommand: Error loading commands from "+config_filename+".\n")

    # ========== Functions ==========

    # @param input - String - (Group Chat User's) input message
    #
    # @returns - String, or None
    def respond(self, input):
        for word in input.split(" "):
            for cmd in self.cmds:
                if word == cmd:
                    return self.__cmd_responses[word]

        return None
