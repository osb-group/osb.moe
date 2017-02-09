from collections import namedtuple
from math import sqrt
from PIL import Image
import random

# Name the tuples
Point = namedtuple('Point', ('coordinates', 'n', 'count'))
Cluster = namedtuple('Cluster', ('points', 'center', 'n'))

def get_average_colors(filename, n=3):
    img = Image.open(filename)
    img.thumbnail((200, 200))
    w, h = img.size

    points = get_points(img)
    clusters = kmeans(points, n, 1)
    rgbs = [map(int, c.center.coordinates) for c in clusters]
    rtoh = lambda rgb: '#%s' % ''.join(('%02x' % p for p in rgb))
    return map(rtoh, rgbs)

def get_points(image):
    points = []
    width, height = image.size
    for count, color in image.getcolors(width * height):
        points.append(Point(color, 3, count))
    return points

def euclidean(p1, p2):
    return sqrt(sum([
                        (p1.coordinates[i] - p2.coordinates[i]) ** 2 for i in range(p1.n)
                        ]))

def calculate_center(points, n):
    vals = [0.0 for i in range(n)]
    plen = 0
    for p in points:
        plen += p.count
        for i in range(n):
            vals[i] += (p.coordinates[i] * p.count)
    return Point([(v / plen) for v in vals], n, 1)

def kmeans(points, k, min_diff):
    clusters = [Cluster([p], p, p.n) for p in random.sample(points, k)]

    while 1:
        plists = [[] for i in range(k)]

        for p in points:
            smallest_distance = float('Inf')
            idx = 0
            for i in range(k):
                distance = euclidean(p, clusters[i].center)
                if distance < smallest_distance:
                    smallest_distance = distance
                    idx = i
            plists[idx].append(p)

        diff = 0
        for i in range(k):
            old = clusters[i]
            center = calculate_center(plists[i], old.n)
            new = Cluster(plists[i], center, old.n)
            clusters[i] = new
            diff = max(diff, euclidean(old.center, new.center))

        if diff < min_diff:
            break

    return clusters