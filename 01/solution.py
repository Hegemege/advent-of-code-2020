def part1(input_data):
    for j in range(len(input_data)):
        for i in range(j, len(input_data)):
            if input_data[j] + input_data[i] == 2020:
                print(input_data[j] * input_data[i])
                return


def part2(input_data):
    for k in range(len(input_data)):
        for j in range(k, len(input_data)):
            for i in range(j, len(input_data)):
                if input_data[k] + input_data[j] + input_data[i] == 2020:
                    print(input_data[k] * input_data[j] * input_data[i])
                    return


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        input_data = list(map(int, input_data))
        part1(input_data)
        part2(input_data)