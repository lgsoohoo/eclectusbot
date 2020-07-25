# Magic 8 Ball
# @Help_File:
#   '!magic', '!magic8', '!m8' - Ask the Magic 8 ball a question!

import random


class Magic8Ball:
    # ========== Static Members ==========

    # List of commands
    cmds = [
        '!magic',
        '!magic8',
        '!m8',
    ]

    # Responses to commands
    __magic8_responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes – definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful.",
    ]

    # ========== Functions ==========

    # @returns - String, or None
    def respond(self):
        return random.choice(self.__magic8_responses)
