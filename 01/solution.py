def part1(input_data):
    # Assumes that input contains no duplicates and not the exact half
    # of the sum, i.e. 1010
    input_lookup = set(input_data)

    for item in input_data:
        if 2020 - item in input_lookup:
            return (2020 - item) * item


def part2(input_data):
    input_lookup = set(input_data)

    for j in range(len(input_data)):
        for i in range(j, len(input_data)):
            if 2020 - input_data[i] - input_data[j] in input_lookup:
                return (
                    (2020 - input_data[i] - input_data[j])
                    * input_data[i]
                    * input_data[j]
                )


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        input_data = list(map(int, input_data))
        print(part1(input_data))
        print(part2(input_data))
