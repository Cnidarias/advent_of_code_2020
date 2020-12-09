from typing import Dict, Tuple, List


def main():
    bag_dict = {}
    with open("../input.txt", "r") as f:
        test_lines = [
            # "light red bags contain 1 bright white bag, 2 muted yellow bags.",
            # "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
            # "bright white bags contain 1 shiny gold bag.",
            # "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
            # "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
            # "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
            # "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
            # "faded blue bags contain no other bags.",
            # "dotted black bags contain no other bags.",
            "shiny gold bags contain 2 dark red bags.",
            "dark red bags contain 2 dark orange bags.",
            "dark orange bags contain 2 dark yellow bags.",
            "dark yellow bags contain 2 dark green bags.",
            "dark green bags contain 2 dark blue bags.",
            "dark blue bags contain 2 dark violet bags.",
            "dark violet bags contain no other bags.",
        ]
        # for l in test_lines:
        for l in f.readlines():
            l = l.strip()
            bag, contents = l.split(" bags contain ")
            contents = contents.rstrip(".")
            content_bags = contents.split(", ")
            content_bags_result = []
            for c in content_bags:
                if c != "no other bags":
                    c = c.split(" ")
                    count = c[0]
                    bag_name = " ".join(c[1:-1])
                    content_bags_result.append((bag_name, int(count)))
            bag_dict[bag] = content_bags_result
        print(get_bag_count(bag_dict, bag_dict.get("shiny gold", [])))


def get_bag_count(bag_dict: Dict[str, List[Tuple[str, int]]], bag_items: List[Tuple[str, int]]) -> int:
    return sum([b[1] + b[1] * get_bag_count(bag_dict, bag_dict.get(b[0], [])) for b in bag_items])


if __name__ == "__main__":
    main()
