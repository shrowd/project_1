import numpy as np
import math
import matplotlib.pyplot as plt


def read(name):
    with open(name, "r") as file:
        points = []
        n = int(file.readline())
        for i in range(n):
            for line in file:
                if "3 3" in line:
                    break
                else:
                    x, y, z = line.split()
                    points.append((float(x), float(y), float(z)))
                    if len(points) == 16:
                        break
    file.close()
    return points


def Bezier(Punkty):
    curve = []
    for v in range(0, 1001):
        t = v / 1000
        Px = 0
        Py = 0
        Pz = 0
        for i in range(0, 4):
            for j in range(0, 4):
                B = Bernstein(i, 3, t) * Bernstein(j, 3, t)
                Px += Punkty[i * 4 + j][0] * B
                Py += Punkty[i * 4 + j][1] * B
                Pz += Punkty[i * 4 + j][2] * B
        curve.append((Px, Py, Pz))
    return curve


def Bernstein(i, n, t):
    return math.comb(n, i) * (t ** i) * ((1 - t) ** (n - i))


def plot(points):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    patches = []
    for i in range(4):
        for j in range(4):
            patch = Bezier([points[k] for k in range(i * 4 + j * 4 * 14, i * 4 + j * 4 * 14 + 16)])
            patches.append(patch)

    for patch in patches:
        x, y, z = zip(*patch)
        ax.plot(x, y, z)

    xx, yy, zz = np.array(patches).T
    ax.plot_surface(xx, yy, zz, cmap='Blues', alpha=0.5)

    plt.show()


def draw(name):
    points = read(name)
    plot(points)