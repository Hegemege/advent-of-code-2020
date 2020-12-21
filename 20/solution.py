import functools
import re
from itertools import combinations
import collections
import math


class Tile:
    def __init__(self, ID, data):
        self.ID = ID
        self.data = data
        self.neighbors = set()

    def get_orientations(self):
        forward = range(len(self.data))
        backward = forward[::-1]
        # Yields every possible orientation to loop the image
        # Topleft corner
        yield [x for x in self.data]
        yield ["".join([self.data[j][i] for j in forward]) for i in forward]

        # Topright corner
        yield [x[::-1] for x in self.data]
        yield ["".join([self.data[j][i] for j in forward]) for i in backward]

        # Bottomleft corner
        yield ["".join([self.data[i][j] for j in forward]) for i in backward]
        yield ["".join([self.data[j][i] for j in backward]) for i in forward]

        # Bottomright corner
        yield ["".join([self.data[i][j] for j in backward]) for i in backward]
        yield ["".join([self.data[j][i] for j in backward]) for i in backward]


def part1_part2(input_data):
    data = parse_input(input_data)
    image_size = 12  # tiles per axis

    # Run a counter for how many other tiles
    # the current tile can border with
    # The only tiles that interface with exactly two tiles for any given orientation must be the corners
    corners = set()
    edges = set()
    centers = set()
    for tile in data:
        fits = 0
        # We only need to check the edges of each tile, not the edges of each tiles
        # every permutation (we don't care about the actual final
        # global orientation of the resulting image)
        for edge in get_edges(tile.data):
            for other_tile in data:
                dobreak = False
                if other_tile.ID == tile.ID:
                    continue
                for other_orientation in other_tile.get_orientations():
                    if edge == other_orientation[0]:
                        fits += 1
                        tile.neighbors.add(other_tile.ID)
                        dobreak = True
                        break
                if dobreak:
                    break
        if fits == 2:
            corners.add(tile.ID)
        elif fits == 3:
            edges.add(tile.ID)
        elif fits == 4:
            centers.add(tile.ID)

    print(functools.reduce(lambda a, b: a * b, list(corners), 1))

    image = [[None for i in range(image_size)] for j in range(image_size)]

    # Place one corner, and fill the rest by looping through all neighbor tiles
    # and fitting them to empty slots in the image

    all_tiles = {x.ID: x for x in data}

    initial = list(corners)[0]
    image[0][0] = all_tiles[initial]
    del all_tiles[initial]

    # while len(all_tiles) > 0:
    #    pass

    # Then, remove the corners from all tiles
    # and reduce the image from tiles to one 2d image

    # Finally, look for sea monsters!


def get_edges(orientation):
    yield orientation[0]
    yield orientation[-1]
    yield "".join([x[0] for x in orientation])
    yield "".join([x[-1] for x in orientation])


def parse_input(input_data):
    parts = "\n".join(input_data).split("\n\n")
    parts = list(map(lambda x: x.split("\n"), parts))
    return [Tile(int(x[0][5:-1]), x[1:]) for x in parts]


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        part1_part2(input_data)
