from fgames.libs import FDice

class FDiceDoWhere:
    def __init__(self):
        self.do_list = ["Kiss", "Lick", "Suck", "Nibble", "Tickle", "Massage"]
        self.where_list = ["My Chest", "Intimate parts", "My Back", "On Legs", "On Neck", "Face"]
        self.prompt = "Enter Q to quit, anything else to Roll: "

        self.do_dice = FDice.FDice(6)
        self.where_dice = FDice.FDice(6)

    def __newLines(self,numLines):
        for i in range(numLines): print("\n")

    def run(self):
        runFlag = True
        while runFlag:
            option = input(self.prompt)
            if option == "Q" or option == "q":
                runFlag = False
            else:
                do_i = self.do_dice.roll()
                where_i = self.where_dice.roll()

                # print(str(do_i) + " " + str(where_i))
                print(self.do_list[do_i - 1] + " " + self.where_list[where_i - 1])
                self.__newLines(6)

if __name__ == "__main__":
    doWhere = FDiceDoWhere()
    doWhere.run()
