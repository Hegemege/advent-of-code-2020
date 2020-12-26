import functools
import re
from itertools import combinations
import collections
import math


class Tile:
    def __init__(self, ID, data):
        self.ID = ID
        self.data = data
        self.neighbors = {}

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
    image_size = int(math.sqrt(len(data)))  # tiles per axis
    tile_size = 10

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
                        tile.neighbors[other_tile.ID] = other_tile
                        other_tile.neighbors[tile.ID] = tile
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

    # Take the first corner and rotate it such that it has two fitting neighbors on the right and bottom side

    initial = list(corners)[0]
    for orientation in all_tiles[initial].get_orientations():
        fits_right = False
        fits_below = False
        right_edge = list(get_edges(orientation))[3]
        bottom_edge = list(get_edges(orientation))[1]
        for _, v in all_tiles[initial].neighbors.items():
            for neighbor_orientation in v.get_orientations():
                left_edge = list(get_edges(neighbor_orientation))[2]
                top_edge = list(get_edges(neighbor_orientation))[0]
                if right_edge == left_edge:
                    fits_right = True
                    break
                if bottom_edge == top_edge:
                    fits_below = True
                    break

        if fits_below and fits_right:
            image[0][0] = orientation
            break

    del all_tiles[initial]

    keys = list(all_tiles.keys())

    while len(all_tiles) > 0:
        tile_id = keys.pop(0)
        tile = all_tiles[tile_id]
        dobreak = False
        for j in range(image_size):
            for i in range(image_size):
                if image[j][i] is not None:
                    continue

                # Check the neighbor before on the row and the one in the previous row.
                # If either fits, the piece fits
                for orientation in tile.get_orientations():
                    fits = False
                    tile_edges = list(get_edges(orientation))
                    if image[j][i - 1] is not None and i > 0:
                        neighbor_edges = list(get_edges(image[j][i - 1]))
                        if tile_edges[2] == neighbor_edges[3]:
                            fits = True
                    if image[j - 1][i] is not None and j > 0:
                        neighbor_edges = list(get_edges(image[j - 1][i]))
                        if tile_edges[0] == neighbor_edges[1]:
                            fits = True

                    if fits:
                        del all_tiles[tile.ID]
                        image[j][i] = orientation
                        dobreak = True
                        break
                if dobreak:
                    break
            if dobreak:
                break
        if not dobreak:
            keys.append(tile_id)

    # Then, remove edges corners from the data in the image
    # and reduce the image from tiles to one 2d image
    image = [
        [cell[j][i] for cell in row for i in range(1, tile_size - 1)]
        for row in image
        for j in range(1, tile_size - 1)
    ]

    monster = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]

    image = Tile(0, image)
    has_monster = False
    for orientation in image.get_orientations():
        orientation = [list(x) for x in orientation]
        for j in range(len(orientation) - len(monster) + 1):
            for i in range(len(orientation[j]) - len(monster[0]) + 1):
                dobreak = False
                for mj in range(len(monster)):
                    for mi in range(len(monster[mj])):
                        if monster[mj][mi] == " ":
                            continue
                        if monster[mj][mi] != orientation[j + mj][i + mi]:
                            dobreak = True
                            break
                    if dobreak:
                        break
                if not dobreak:
                    has_monster = True
                    for mj in range(len(monster)):
                        for mi in range(len(monster[mj])):
                            if monster[mj][mi] == " ":
                                continue
                            orientation[j + mj][i + mi] = "O"
        if has_monster:
            print(sum(map(lambda x: sum(map(lambda y: y == "#", x)), orientation)))
            return


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
