'''random ralk using matplotlib'''

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


if __name__ == '__main__':
    random_walk1 = RandomWalk(8000)
    random_walk1.fill_random_walk()
    # set the size of graph
    plt.figure(dpi=267, figsize=(9, 5))
    plt.scatter(random_walk1.x, random_walk1.y, s=3, c=random_walk1.y,
                cmap=plt.cm.Blues,
                edgecolors='none')  # s:size of dot; c=(0,0,0.8) 0-1 0 means more or c =list(color by the order it appears) for color fade in.cmap  color fade in
    plt.title('random walk', fontsize=10)
    plt.xlabel('times')
    # show the initial dot(red) and last dot(green)
    plt.scatter(random_walk1.x[0], random_walk1.y[0], c='red', s=20)
    plt.scatter(random_walk1.x[-1], random_walk1.y[-1], c='green', s=20)

    # hide the  x axis
    plt.axes().get_xaxis().set_visible(False)

    plt.show()
    # plt.savefig('3.png',
    #             bbox_inches='tight')  # use bbox_inches if the blank area isn't wanted
