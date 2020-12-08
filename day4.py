categories = ["byr" ,
"iyr",
"eyr",
"hgt",
"hcl",
"ecl",
"pid",
"cid"]

with open("input-day4", 'r') as f:
    num_valid = 0
    current_passport = ''
    for i, line in enumerate(f):
        if line == '\n':
            #stop and prcoess
            print(current_passport)


            passport_valid = True
            for cat in categories:
                if current_passport.count(cat) == 0 and cat != 'cid':
                    passport_valid = False
                    break

            if passport_valid:
                num_valid = num_valid +1

            current_passport = ''
        else:
            current_passport = current_passport + ' ' + line.strip()


print(f"Num valid = {num_valid}")
