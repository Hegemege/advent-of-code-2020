import functools
import re


def part1(input_data):
    all_bags = {}
    for line in input_data:
        bag = parse_input_line(line)
        bag["children"] = []
        bag["parents"] = []
        all_bags[bag["id"]] = bag

    # Link the graph
    for k, v in all_bags.items():
        for child in v["contents"]:
            v["children"].append(all_bags[child[1]])
            all_bags[child[1]]["parents"].append(v)

    unique_bags = set()
    get_parent_count(unique_bags, all_bags, "shiny gold")
    return len(unique_bags)


def part2(input_data):
    all_bags = {}
    for line in input_data:
        bag = parse_input_line(line)
        bag["children"] = {}
        all_bags[bag["id"]] = bag

    # Link the graph
    for k, v in all_bags.items():
        for child in v["contents"]:
            child_count, child_id = child
            v["children"][child_id] = child_count

    return get_child_count(all_bags, "shiny gold")


def get_parent_count(unique_bags, all_bags, bag_id):
    for parent in all_bags[bag_id]["parents"]:
        unique_bags.add(parent["id"])
        get_parent_count(unique_bags, all_bags, parent["id"])


def get_child_count(all_bags, bag_id):
    bag = all_bags[bag_id]
    total = 0
    for k, v in bag["children"].items():
        total += v * (1 + get_child_count(all_bags, k))
    return total


def parse_input_line(line):
    # First two words is the ID of the bag
    bag_id, contents_raw = line.split(" bags contain ")
    if contents_raw == "no other bags.":
        return {"id": bag_id, "contents": []}

    contents = contents_raw.split(", ")
    contents = list(
        map(
            lambda x: x.replace(".", "").replace("bags", "").replace("bag", ""),
            contents,
        )
    )
    contents = list(
        map(
            lambda x: (
                int(x.split(" ")[0]),
                " ".join(x.split(" ")[1:]).strip(),
            ),
            contents,
        )
    )
    return {"id": bag_id, "contents": contents}


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        print(part1(input_data))
        print(part2(input_data))
