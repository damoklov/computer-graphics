from math import sin, cosh, sinh
from matplotlib import pyplot as plt


def main():
    t = 1
    max_t = 20
    h = 0.01

    x_axis = list()
    y_axis = list()

    while t <= max_t:
        x_axis.append(x(t))
        y_axis.append(y(t))
        t += h

    plot = plt.figure(figsize=(5, 5)).gca()
    plot.plot(x_axis, y_axis)
    plot.set_xlabel('X')
    plot.set_ylabel('F(X)')
    plt.show()


def y(t):
    return 3 * (cosh(t) + t * sinh(t)) - 40 * sin(t) ** 5


def x(t):
    return 3 * (cosh(t) - t * sinh(t)) - 40 * cosh(t) ** 5


if __name__ == '__main__':
    main()
