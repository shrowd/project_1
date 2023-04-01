import matplotlib.pyplot as plt

points = [(225, 83), (223, 83), (293, 81), (293, 80),
          (321, 88), (321, 164), (292, 174), (293, 173),
          (223, 192), (223, 192), (224, 193), (305, 176),
          (290, 173), (311, 167), (304, 264), (275, 267),
          (275, 267), (224, 282), (223, 282), (223, 282),
          (225, 83), (223, 82), (224, 82), (103, 81),
          (103, 81), (103, 82), (106, 286), (106, 286),
          (106, 287), (124, 285), (124, 285), (124, 285),
          (124, 210), (123, 210), (124, 212), (184, 274),
          (184, 273), (185, 274), (196, 261), (197, 260),
          (196, 261), (131, 189), (131, 189), (120, 199),
          (197, 129), (195, 129), (195, 129), (186, 115),
          (186, 116), (186, 115), (122, 176), (122, 176),
          (121, 176), (122, 60), (121, 60), (120, 75)]


def bezier_curve(points, t):
    p0, p1, p2, p3 = points
    return (1 - t) ** 3 * p0 + 3 * (1 - t) ** 2 * t * p1 + 3 * (1 - t) * t ** 2 * p2 + t ** 3 * p3


curvePoints = []
for i in range(0, len(points), 4):
    remainingPoints = len(points) - i
    if remainingPoints >= 4:
        p0, p1, p2, p3 = points[i:i + 4]
        for t in range(101):
            x = bezier_curve((p0[0], p1[0], p2[0], p3[0]), t / 100)
            y = bezier_curve((p0[1], p1[1], p2[1], p3[1]), t / 100)
            curvePoints.append((x, y))


def draw():
    xCoords = [point[0] for point in curvePoints]
    yCoords = [point[1] for point in curvePoints]
    plt.plot(xCoords, yCoords)
    plt.show()
