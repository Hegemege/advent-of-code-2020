import functools
import re
from itertools import combinations
import collections
import math


def part1(input_data):
    return sum(map(evaluate, input_data))


def part2(input_data):
    pass


def evaluate(expression):
    while "(" in expression:
        expression = split_expression(expression)

    terms = re.split(r"(\W)", expression)
    current = int(terms[0])
    for i in range(1, len(terms), 2):
        operator = terms[i]
        operant = int(terms[i + 1])
        current = eval(f"{current}{operator}{operant}")
    return current


def split_expression(expression):
    # Find the first parenthesis and it's matching counterpart
    beginning = expression.index("(")
    end = len(expression) - 1
    counter = 0
    for i in range(beginning + 1, len(expression)):
        if expression[i] == ")" and counter == 0:
            end = i
            break
        elif expression[i] == "(":
            counter += 1
        elif expression[i] == ")":
            counter -= 1

    return (
        expression[:beginning]
        + str(evaluate(expression[beginning + 1 : end]))
        + expression[end + 1 :]
    )


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(
            map(lambda x: x.strip().replace(" ", ""), input_file.readlines())
        )
        print(part1(input_data))
        print(part2(input_data))
