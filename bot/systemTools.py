# System Tools
# Requires a `/module_config/systemTools_help.txt` help file.
#   - Help file scheme: N/A. Entire file will be printed out. No need for string escape sequences.
#
# Publicly available functions:
#   def normalizeText(text)
#   def check_usage(cmds, input)

class SystemTools:

    # Commands that trigger the help message
    cmds = [
        '!help',
        '!command',
        '!commands',
        '!cmd',
        '!cmds',
        '!bot',
        '/help',
        '/command',
        '/commands',
        '/cmd',
        '/cmds',
        '/bot',
    ]

    # ========== Functions ==========

    # Normalizes text:
    #  - Removes special characters (except !, replace with a space)
    #  - Adds a space before a '!'
    #  - Converts all text to lowercase
    # @param text - String - text to process
    #
    # @returns String - processed text
    def normalizeText(self, text):
        text = text.replace("~", " ")
        text = text.replace("@", " ")
        text = text.replace("#", " ")
        text = text.replace("$", " ")
        text = text.replace("%", " ")
        text = text.replace("^", " ")
        text = text.replace("&", " ")
        text = text.replace("*", " ")
        text = text.replace("(", " ")
        text = text.replace(")", " ")
        text = text.replace("_", " ")
        text = text.replace("+", " ")
        text = text.replace("`", " ")
        text = text.replace("{", " ")
        text = text.replace("}", " ")
        text = text.replace("|", " ")
        text = text.replace("[", " ")
        text = text.replace("]", " ")
        text = text.replace("\\", " ")
        text = text.replace(";", " ")
        text = text.replace("'", " ")
        text = text.replace(":", " ")
        text = text.replace("\"", " ")
        text = text.replace("<", " ")
        text = text.replace(">", " ")
        text = text.replace("?", " ")
        text = text.replace(",", " ")
        text = text.replace(".", " ")
        text = text.replace("/", " ")
        text = text.replace("\n", " ")
        text = text.replace("!", " !")
        text = text.lower()

        return text

    # Checks if the input uses any of the given commands
    # @param cmds - String Array - List of commands to search for
    # @param input - String - (Group Chat User's) input message
    #
    # @returns - Boolean
    def check_usage(self, cmds, input):
        for word in input.split(" "):
            if word in cmds:
                return True
        return False

    # Bot's response when help is requested
    #
    # @returns String - Contents of "systemTools_help.txt" or Error message
    def respond(self):
        response = "Unknown error has occurred. Contact admin for help."
        try:
            help_file = open("./module_config/systemTools_help.txt")
            response = help_file.read()
            help_file.close()
        except:
            response = "Error, Help Command Response file was not found. Contact admin for help."
        return response
