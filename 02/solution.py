def part1(input_data):
    return sum(map(password_valid, input_data))


def part2(input_data):
    pass


def password_valid(line):
    rule, password = line.split(": ")
    rule_range, rule_symbol = rule.split(" ")
    rule_range_start, rule_range_end = tuple(map(int, rule_range.split("-")))
    symbol_lookup = {}
    symbol_lookup[rule_symbol] = 0  # Make sure the rule symbol exists in the lookup

    for symbol in password:
        if symbol not in symbol_lookup:
            symbol_lookup[symbol] = 0
        symbol_lookup[symbol] += 1

    return (
        symbol_lookup[rule_symbol] >= rule_range_start
        and symbol_lookup[rule_symbol] <= rule_range_end
    )


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        print(part1(input_data))
        print(part2(input_data))
