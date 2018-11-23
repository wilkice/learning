from random import choice
import matplotlib.pyplot as plt


class RandomWalk():
    def __init__(self, times=5000):
        self.times = times  # the dots' num is 5000
        self.x = [0]  # a list to store x value of the graph
        self.y = [0]

    def fill_random_walk(self):
        while len(self.x) < self.times:
            x_direction = choice([-1, 1])  # decide forward or backforward
            x_step = choice([0, 1, 2, 3, 4])  # decide the step
            x_point = self.x[
                          -1] + x_direction * x_step  # get location of new dot
            self.x.append(x_point)

            y_direction = choice([-1, 1])
            y_step = choice([0, 1, 2, 3, 4])
            y_point = self.y[-1] + y_direction * y_step
            self.y.append(y_point)


random_walk1 = RandomWalk()
random_walk1.fill_random_walk()
plt.scatter(random_walk1.x, random_walk1.y, s=1, edgecolors='none')
plt.show()
