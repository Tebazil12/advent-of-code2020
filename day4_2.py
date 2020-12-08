import string



categories = ["byr" ,
"iyr",
"eyr",
"hgt",
"hcl",
"ecl",
"pid",
"cid"]


def validate_cat(cat, value):
    if cat == "byr":
        #four digits; at least 1920 and at most 2002.
        if int(value) >= 1920 and int(value) <= 2002:
            return True
        else:
            return False
    elif cat == "iyr":
        #four digits; at least 2010 and at most 2020.
        if int(value) >= 2010 and int(value) <= 2020:
            return True
        else:
            return False
    elif cat == "eyr":
        #four digits; at least 2020 and at most 2030
        if int(value) >= 2020 and int(value) <= 2030:
            return True
        else:
            return False

    elif cat == "hgt":
        last_two_chs = value[-2] + value[-1]
        # print(last_two_chs)
        if last_two_chs == "cm":
            #the number must be at least 150 and at most 193
            num = value.split("cm")[0]
            if int(num) >= 150 and int(num) <= 193:
                return True
            else:
                return False

        elif last_two_chs == "in":
            #the number must be at least 59 and at most 76.
            num = value.split("in")[0]
            if int(num) >= 59 and int(num) <= 76:
                return True
            else:
                return False

        else:
            return False

    elif cat == "hcl":
        # followed by exactly six characters 0-9 or a-f.
        if value[0] != "#":
            return False
        if len(value) != 7:
            return False

        ascii = set(string.hexdigits)
        # print(ascii)

        if all(x in ascii for x in value[1:]):
            # my_string1 is all ascii
            return True
        else:
            return False

    elif cat == "ecl":
        #exactly one of: amb blu brn gry grn hzl oth.
        colours = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
        if value in colours:
            return True
        else:
            return False

    elif cat == "pid":
        #a nine-digit number, including leading zeroes
        if len(value) != 9:
            return False

        ascii = set(string.digits)
        if all(x in ascii for x in value):
            # my_string1 is all ascii
            return True
        else:
            return False
    elif cat == "cid":
        return True # doesn't need checking
    else:
        raise NameError("category not recognised")

    # return True


with open("input-day4", 'r') as f:
    num_valid = 0
    current_passport = ''
    for i, line in enumerate(f):
        if line == '\n':
            #stop and prcoess
            # print(current_passport)
            passport_valid = True
            for cat in categories:
                if current_passport.count(cat) == 0 and cat != 'cid':
                    passport_valid = False
                    break

            if passport_valid:

                split_passport = current_passport.split()
                # print(split_passport)
                for item in split_passport:
                    split_item = item.split(':')

                    passport_valid = validate_cat(split_item[0],split_item[1])
                    if passport_valid is False:
                        break
                if passport_valid:
                    num_valid = num_valid +1




            current_passport = ''
        else:
            current_passport = current_passport + ' ' + line.strip()


print(f"Num valid = {num_valid}")
