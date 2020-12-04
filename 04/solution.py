import functools
import re


def part1(input_data):
    passports = functools.reduce(
        accumulate_passport_details,
        " ".join(input_data).split(" "),
        [{}],
    )

    return sum(map(valid_passport_part1, passports))


def part2(input_data):
    passports = functools.reduce(
        accumulate_passport_details,
        " ".join(input_data).split(" "),
        [{}],
    )

    return sum(map(valid_passport_part2, passports))


def accumulate_passport_details(a, b):
    if len(b) == 0:
        a.append({})
    else:
        key, value = b.split(":")
        a[-1][key] = value
    return a


def valid_passport_part1(passport):
    required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for key in required_keys:
        if key not in passport:
            return False
    return True


def valid_passport_part2(passport):
    valid = valid_passport_part1(passport)
    if not valid:
        return False

    birthYear = int(passport["byr"])
    if birthYear < 1920 or birthYear > 2002:
        return False

    issueYear = int(passport["iyr"])
    if issueYear < 2010 or issueYear > 2020:
        return False

    expirationYear = int(passport["eyr"])
    if expirationYear < 2020 or expirationYear > 2030:
        return False

    heightUnit = passport["hgt"][-2:]
    if heightUnit != "cm" and heightUnit != "in":
        return False

    heightvalue = int(passport["hgt"][:-2])
    if heightUnit == "cm" and (heightvalue < 150 or heightvalue > 193):
        return False
    elif heightUnit == "in" and (heightvalue < 59 or heightvalue > 76):
        return False

    if re.search("^#[0-9a-f]{6}$", passport["hcl"]) is None:
        return False

    if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False

    if not passport["pid"].isalnum() or len(passport["pid"]) != 9:
        return False

    return True


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        print(part1(input_data))
        print(part2(input_data))
