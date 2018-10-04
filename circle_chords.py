from complex import *
import matplotlib.pyplot as plt
from math import sqrt, isclose
from operator import mul
from functools import reduce
import sys



def get_unity_roots(n):
    """
    Finds the nth roots of unity
    :param n:  
    :return: 
    """

    z = Complex(1)

    return roots(n, z)

def plot_circle():
    """
    Plots a unit circle
    :return: 
    """

    fig = plt.figure(figsize=(8, 8))
    plt.xticks([-1, 1])
    plt.yticks([-1, 1])
    ax = fig.add_subplot(1, 1, 1)

    # I used this: https://stackoverflow.com/questions/2409774/how-can-i-produce-student-style-graphs-using-matplotlib
    # for some of the formatting
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    ax.set_facecolor('xkcd:light gray')
    circ = plt.Circle((0, 0), radius=1, edgecolor='black', facecolor='None')
    ax.add_patch(circ)
    plt.axis('scaled')


    return fig, ax

def plot_roots(unity, ax):
    """
    Plots the roots of unity and converts roots of unity from polar to rectangular form
    :param unity: roots of unity
    :param ax: axes for the figure used for plotting
    :return: 
    """

    roots_rect = []
    for root in unity:
        z = rect(root[0], root[1])
        roots_rect.append(z)
        ax.plot(z.re, z.im, 'ro')


    return roots_rect

def plot_chords(roots_rect, ax):
    """
    Plots the chords from (1,0) to the other n-1 roots of unity
    :param roots_rect: roots of unity in rectangular form
    :param ax: 
    :return: list of lengths of the n-1 chords
    """
    base = roots_rect[0]
    lengths = []
    for root in roots_rect[1:]:
        ax.plot([base.re, root.re], [base.im, root.im], 'r')

        length = sqrt((base.re - root.re) ** 2 + (base.im - root.im) ** 2)
        lengths.append(length)


    return lengths

if __name__ == '__main__':

    n = int(sys.argv[1])

    unity = get_unity_roots(n)

    fig, ax = plot_circle()

    roots_rect = plot_roots(unity, ax)

    lengths = plot_chords(roots_rect, ax)

    prod = reduce(mul, lengths)

    final_str = 'The product of the lengths of the chords is {} and n is {}'.format(prod, n)

    print(final_str)
    plt.show()





