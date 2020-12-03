import functools


def part1(input_data):
    # Going down one step means we can just go line-by-line
    return count_trees(input_data, (3, 1))


def part2(input_data):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return functools.reduce(lambda a, b: a * count_trees(input_data, b), slopes, 1)


def count_trees(input_data, slope):
    slope_x, slope_y = slope
    trees = 0
    index = 0
    height = len(input_data)
    width = len(input_data[0])
    for line_index in range(0, height, slope_y):
        line = input_data[line_index]
        # Check
        if line[index] == "#":
            trees += 1
        # Step
        index = (index + slope_x) % width
    return trees


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        print(part1(input_data))
        print(part2(input_data))
