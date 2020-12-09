def main():
    with open("../input.txt", "r") as f:
        numbers = [
            "35",
            "20",
            "15",
            "25",
            "47",
            "40",
            "62",
            "55",
            "65",
            "95",
            "102",
            "117",
            "150",
            "182",
            "127",
            "219",
            "299",
            "277",
            "309",
            "576",
        ]
        numbers = [int(n) for n in numbers]
        numbers = [int(l.strip()) for l in f.readlines()]
        result = get_first_invalid_number(numbers, window_size=25, start_idx=0)
        print(result)
        pass


def get_first_invalid_number(elements: [int], window_size: int = 25, start_idx: int = 0) -> int:
    numbers_to_pick_from = elements[start_idx:start_idx+window_size]
    number_to_verify = elements[start_idx + window_size]
    for idx, number in enumerate(numbers_to_pick_from):
        for i in range(idx + 1, len(numbers_to_pick_from), 1):
            if number + numbers_to_pick_from[i] == number_to_verify:
                return get_first_invalid_number(elements, window_size, start_idx + 1)
    return number_to_verify




if __name__ == "__main__":
    main()
