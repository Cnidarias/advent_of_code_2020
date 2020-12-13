def main():
    with open("../input.txt", "r") as f:
        sample_input = [
            28,
            33,
            18,
            42,
            31,
            14,
            46,
            20,
            48,
            47,
            24,
            23,
            49,
            45,
            19,
            38,
            39,
            11,
            1,
            32,
            25,
            35,
            8,
            17,
            7,
            9,
            4,
            2,
            34,
            10,
            3,
        ]
        sample_input = [
            16,
            10,
            15,
            5,
            1,
            11,
            7,
            19,
            6,
            12,
            4,
        ]
        numbers = sorted(sample_input)
        numbers = sorted(int(l) for l in f.readlines())
        print(numbers)

        one_diff = 0
        three_diff = 1
        current = 0
        for idx, number in enumerate(numbers):
            if current + 3 >= number:
                diff = number - current
                if diff == 1:
                    one_diff += 1
                elif diff == 3:
                    three_diff += 1
                current = number

        print(one_diff, three_diff, one_diff * three_diff)


if __name__ == "__main__":
    main()
