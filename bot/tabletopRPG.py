# Tabletop RPG
# Adds gaming/probability commands to the bot.
# @Note: Tabletop RPG's respond() requires the raw (non normalized) input
# @Help_File:
#   '!roll', '!roll(%d&)' - Rolls dice, where %=number of dice, and &=number of sides (default=1d6)
#   '!flip', '!coin' - Flips a fair, 2 sided coin
#   '!rng' - Generates a random number from 0-100, inclusive

from random import randint


class TabletopRPG:
    # ========== Static Members ==========

    # List of commands
    cmds = [
        '!roll',
        '!flip',
        '!coin',
        '!rng',
    ]

    # ========== Functions ==========

    # Generates the response to a command
    # @param input - String - (Group Chat User's) input message - RAW, not normalized
    # @param sender - String - Name of the message sender.
    #
    # @returns - String - response
    def respond(self, input, sender):
        splitted = input.lower().replace("!", " !").split(" ")

        if '!flip' in splitted or '!coin' in splitted:
            return self.__flip(sender)
        if '!rng' in splitted:
            return self.__rng()

        command = ''
        for word in splitted:
            if '!roll' in word:
                command = word
        if command == '' or command == "!roll":
            return self.__roll(sender)
        else:
            try:
                nums = command.split("!roll(")[1].split(")")[0]
                nums = nums.split("d")
                amt = 1 if nums[0] == '' else int(nums[0])
                sds = 6 if nums[1] == '' else int(nums[1])
                return self.__roll(sender, amt, sds)
            except:
                return self.__roll(sender)

    # Rolls multiple dice
    # @param sender - String - Name of the message sender.
    # @param amount - Number - number of dice
    # @param sides - Number - number of sides for each dice
    # @example - "3d12" -> roll(3,12)
    #
    # @returns - String - What they rolled in dice notation,
    #            the results of their roll(s), and the sum.
    def __roll(self, sender, amount=1, sides=6):
        results = []
        for die in range(amount):
            results.append(randint(1, sides))
        res = sender + " rolls a " + str(amount) + "d" + str(sides) + ". "
        res += "You got " + str(results) + ". "
        res += "Sum = " + str(sum(results)) + "."
        return res

    # Flips a fair, 2 sided coin
    #
    # @returns - String - "The coin landed on <heads/tails>!"
    def __flip(self, sender):
        side = ''
        if randint(0, 1) == 0:
            side = 'heads'
        else:
            side = 'tails'
        return sender + ' flips a coin. It landed on '+side+'!'

    # Generates a number response from 0-100
    #
    # @returns "RNG says: <# from 0-100>!"
    def __rng(self):
        return "RNG says: " + str(randint(0, 100)) + "!"
