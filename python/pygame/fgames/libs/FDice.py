import random

class FDice:
    def __init__(self, faces):
        random.seed()
        self.faces = range(1, faces + 1)
        self.rolled = False

    def __str__(self):
        dice_string = "A " + str(max(self.faces)) + "-sided dice."
        if self.rolled:
            return dice_string + " You rolled " + str(self.roll_value) + "."
        else:
            return dice_string

    def roll(self):
        self.rolled = True
        self.roll_value = random.choice(self.faces)
        return self.roll_value

if __name__ == "__main__":
    dice = FDice(24)
    print(dice.roll())