import itertools
# 181 is too low
def main():
    all_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid_count = 0
    with open("../input.txt", "r") as f:
        everything = f.read()
        passports = everything.split("\n\n")

        for passport in passports:
            if verify_passport_has_fields(passport, required_fields):
                valid_count += 1
    print(valid_count)

def verify_passport_has_fields(passport, required_fields):
    parts =passport.split("\n")
    all_parts = [p.split(" ") for p in parts if len(p) > 1]
    flat_list= list(itertools.chain(*all_parts))
    fields = [r.split(":")[0] for r in flat_list]
    values = [r.split(":")[1] for r in flat_list]
    print("---")
    print(passport)
    print(flat_list)
    print(fields, values)
    print("---")

    for rf in required_fields:
        if rf not in fields:
            return False
    return True



if __name__ == "__main__":
    main()
