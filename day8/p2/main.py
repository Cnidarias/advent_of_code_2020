import copy


def main():
    with open("../input.txt", "r") as f:
        code = [
            "nop +0",
            "acc +1",
            "jmp +4",
            "acc +3",
            "jmp -3",
            "acc -99",
            "acc +1",
            "jmp -4",
            "acc +6",
        ]
        code = f.readlines()
        code = [c.split(" ") for c in code]
        for idx, code_line in enumerate(code):
            if code_line[0] == "jmp" or code_line[0] == "nop":
                new_code = copy.deepcopy(code)
                if code_line[0] == "jmp":
                    new_instruction = "nop"
                else:
                    new_instruction = "jmp"
                new_code[idx] = (new_instruction, code_line[1])
                success, value = execute_code(new_code)
                if success:
                    print(value)
                    return


def execute_code(code):
    executed_lines = []
    acc = 0
    idx = 0
    while True:
        if idx in executed_lines:
            return False, acc
        if idx == len(code):
            return True, acc
        executed_lines.append(idx)
        instruction, number = code[idx]
        if instruction == "nop":
            idx += 1
        elif instruction == "acc":
            acc += int(number)
            idx += 1
        elif instruction == "jmp":
            idx += int(number)


if __name__ == "__main__":
    main()
