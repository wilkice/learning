from random import choice
import matplotlib.pyplot as plt


class RandomWalk():
    def __init__(self, times=5000):
        self.times = times  # the dots' num is 5000
        self.x = [0]  # a list to store x value of the graph
        self.y = [0]

    def fill_random_walk(self):
        while len(self.x) < self.times:
            self.x_direction = choice([0, 1])  # decide forward or backforward
            self.x_step = choice([0, 1, 2, 3, 4])  # decide the step
            self.x_point = self.x[
                               -1] + self.x_direction * self.x_step  # get location of new dot
            self.x.append(self.x_point)

            self.y_direction = choice([0, 1])
            self.y_step = choice([0, 1, 2, 3, 4])
            self.y_point = self.y[-1] + self.y_direction * self.y_step
            self.y.append(self.y_point)


random_walk1 = RandomWalk()
random_walk1.fill_random_walk()
plt.scatter(random_walk1.x, random_walk1.y, s=15)
plt.show()
