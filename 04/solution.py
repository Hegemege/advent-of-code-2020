import functools


def part1(input_data):
    passports = functools.reduce(
        accumulate_passport_details,
        " ".join(input_data).split(" "),
        [{}],
    )

    return sum(map(valid_passport, passports))


def part2(input_data):
    pass


def accumulate_passport_details(a, b):
    if len(b) == 0:
        a.append({})
    else:
        key, value = b.split(":")
        a[-1][key] = value
    return a


def valid_passport(passport):
    required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for key in required_keys:
        if key not in passport:
            return False
    return True


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        print(part1(input_data))
        print(part2(input_data))
