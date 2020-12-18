import functools
import re
from itertools import combinations
import collections
import math


def part1(input_data):
    return sum(map(evaluate, input_data))


def part2(input_data):
    return sum(map(evaluate_part2, input_data))


def evaluate(expression):
    while "(" in expression:
        expression = split_expression(expression, evaluate)

    terms = re.split(r"(\W)", expression)
    current = int(terms[0])
    for i in range(1, len(terms), 2):
        operator = terms[i]
        operant = int(terms[i + 1])
        current = eval(f"{current}{operator}{operant}")
    return current


def evaluate_part2(expression):
    while "(" in expression:
        expression = split_expression(expression, evaluate_part2)

    if "*" not in expression:
        return eval(expression)
    if "+" not in expression:
        return eval(expression)

    # Inject parenthesis to force the order
    terms = re.split(r"(\W)", expression)
    index = terms.index("+")
    terms.insert(index + 2, ")")
    terms.insert(index - 1, "(")
    return evaluate_part2("".join(terms))


def split_expression(expression, evaluator):
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
        + str(evaluator(expression[beginning + 1 : end]))
        + expression[end + 1 :]
    )


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(
            map(lambda x: x.strip().replace(" ", ""), input_file.readlines())
        )
        print(part1(input_data))
        print(part2(input_data))
