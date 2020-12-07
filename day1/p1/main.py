def main():
    with open("../input.txt") as f:
        costs = [int(c) for c in f.readlines()]

    for idx, val in enumerate(costs):
        for i in range(idx + 1, len(costs), 1):
            for j in range(i + 1, len(costs), 1):
                if val + costs[i] + costs[j] == 2020:
                    print(val, costs[i], costs[j], val * costs[i] * costs[j])
                    return


if __name__ == "__main__":
    main()
