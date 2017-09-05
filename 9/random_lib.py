from random import randint


class Die():
    """randint test"""

    def __init__(self, slides=6):
        self.slides = slides

    def roll_die(self):
        print("The random num is " + str(randint(1, self.slides)))


def cir_roll_die(total, instance):
    cnt = 0
    while True:
        if cnt == total:
            break
        instance.roll_die()
        cnt += 1


die_one = Die()
cir_roll_die(10, die_one)
print("\n")

die_two = Die(10)
cir_roll_die(10, die_two)
print("\n")

die_three = Die(20)
cir_roll_die(10, die_three)