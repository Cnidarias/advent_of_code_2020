def main():
    with open("../input.txt", "r") as f:
        content = f.read()
        groups = [g.split() for g in content.split("\n\n")]
        answers = []
        for group in groups:
            yes_questions = set(list(group[0]))
            for idx in range(1, len(group), 1):
                yes_questions = yes_questions.intersection(set(list(group[idx])))
            answers.append(len(yes_questions))
        print(sum(answers))


if __name__ == "__main__":
    main()
