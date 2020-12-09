from typing import Dict


def main():
    bag_dict = {}
    with open("../input.txt", "r") as f:
        test_lines = [
            "light red bags contain 1 bright white bag, 2 muted yellow bags.",
            "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
            "bright white bags contain 1 shiny gold bag.",
            "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
            "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
            "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
            "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
            "faded blue bags contain no other bags.",
            "dotted black bags contain no other bags.",
        ]
        # for l in test_lines:
        for l in f.readlines():
            l = l.strip()
            bag, contents = l.split(" bags contain ")
            contents = contents.rstrip(".")
            content_bags = contents.split(", ")
            content_bags_result = [" ".join(c.split(" ")[1:-1]) for c in content_bags if c != "no other bags"]
            bag_dict[bag] = content_bags_result

    contains_gold = 0
    for key, value in bag_dict.items():
        if test_for_shiny_golden_content(bag_dict, value):
            contains_gold += 1
    print(contains_gold)


def test_for_shiny_golden_content(bag_dict: Dict[str, list], items: [str]):
    if "shiny gold" in items:
        return True
    elif len(items) == 0:
        return False
    else:
        return any([test_for_shiny_golden_content(bag_dict, bag_dict.get(c, [])) for c in items])


if __name__ == "__main__":
    main()
