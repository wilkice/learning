from random import randint
import pygal


class Die():
    def __init__(self, num_sides):
        self.num_sides = num_sides  # the sides of Die

    def roll(self):
        return randint(1, self.num_sides)


die1 = Die(6)
die2 = Die(10)
results = []
for roll_times in range(10001):
    result = die1.roll() + die2.roll()
    results.append(result)

frequencies = []
for value in range(1, die1.num_sides + die2.num_sides + 2):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.title = 'result of roll Die'
hist.x_title = 'value'
hist.y_title = 'times'
hist.x_labels = list(range(1, die1.num_sides + die2.num_sides + 2))

hist.add('Die value times', frequencies)
hist.render_to_file('die_visual2.svg')  # open this file in web browser
