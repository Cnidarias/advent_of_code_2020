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
        # sample_input = [
        #     16,
        #     10,
        #     15,
        #     5,
        #     1,
        #     11,
        #     7,
        #     19,
        #     6,
        #     12,
        #     4,
        # ]
        numbers = sorted(sample_input)
        numbers = sorted(int(l) for l in f.readlines())

        numbers.append(numbers[-1] + 3)
        data = {0: 1}
        for number in numbers:
            data[number] = data.get(number - 3, 0) + data.get(number - 2, 0) + data.get(number - 1, 0)
        print(data[numbers[-1]])


if __name__ == "__main__":
    main()
