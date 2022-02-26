import os
from fgames.libs import FDice, FTimer
from fgames.resources import action_time_list

class FDiceAction:
    def __init__(self):
        self.action_time_list = action_time_list.action_time_list
        self.sound_file=F"..{os.sep}resources{os.sep}boxing_bell.wav"
        self.prompt = "Enter Q to quit, anything else to Roll: "

        self.dice = FDice.FDice(16)
        self.timer = FTimer.FTimer(soundFile=self.sound_file)

        self.timer.count_down(0, "When you hear this sound, stop")

    def __newLines(self,numLines):
        for i in range(numLines): print("\n")

    def run(self):
        previous_entries = []
        option = None
        showPromptFlag = True

        getAactionFlag = True
        while getAactionFlag:
            self.__newLines(10)
            if showPromptFlag:
                option = input(self.prompt)
                self.__newLines(5)
            showPromptFlag = True

            if option == "Q" or option == "q":
                getAactionFlag = False
            else:
                startActionFlag = True
                while startActionFlag:
                    do_i = self.dice.roll()
                    if do_i not in previous_entries:
                        startActionFlag = False
                        previous_entries.append(do_i)
                        if len(previous_entries) > len(self.action_time_list)//2:
                            previous_entries.pop(0)

                        action = action_time_list[do_i - 1][0]
                        how_long = action_time_list[do_i - 1][1]

                        print("For " + self.timer.secs_to_printable(how_long) + ": " + action)
                        self.__newLines(2)
                        skip_option = input(".......Press Enter to START or S to skip or Q to quit: ")
                        if skip_option == "S" or skip_option == "s":
                            showPromptFlag = False
                        elif skip_option == "Q" or skip_option == "q":
                            startActionFlag = True
                            getAactionFlag = True
                        else:
                            self.timer.count_down(how_long)

if __name__ == "__main__":
    diceAction = FDiceAction()
    diceAction.run()