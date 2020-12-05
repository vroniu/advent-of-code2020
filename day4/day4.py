with open("passtest_valid.txt", 'r') as input:

    lines = input.readlines()

    passport_data = []

    entry = ""
    for line in lines:
        if not line.strip():
            #if line is empty
            passport_data.append(entry.strip()) #strip the entry of whitespaces
            entry = ""
        else:
            #if line is not empty
            entry += line
    
    #add the last line
    passport_data.append(entry.strip())

    #PART ONE
    valid_passports = 0
    for ps in passport_data:
        #split into fields
        info = ps.split()
        #if fully valid
        if len(info) == 8:
            valid_passports += 1
        #if partialy valid
        if len(info) == 7 and not "cid" in ps:
            valid_passports += 1

    #PART TWO
    valid_data_passports = 0

    allowed_eye_colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

    for ps in passport_data:
        #split into fields
        fields = ps.split()
        #check if it has required fields
        if (len(fields) == 8) or (len(fields) == 7 and "cid" not in ps):
            valid = True
            for field in fields:
                if "byr" in field:
                    field = field.replace("byr:", "")
                    if not 1920 <= int(field) <= 2002:
                        print("bid invalid")
                        valid = False

                elif "iyr" in field:
                    field = field.replace("iyr:", "")
                    if not 2010 <= int(field) <= 2020:
                        print("iyr invalid")
                        valid = False

                elif "eyr" in field:
                    field = field.replace("eyr:", "")
                    if not 2020 <= int(field) <= 2030:
                        print("eyr invalid")
                        valid = False

                elif "hgt" in field:
                    field = field.replace("hgt:", "")
                    if "cm" in field:
                        field = field.replace("cm", "")
                        if not 150 <= int(field) <= 193:
                            valid = False
                    elif "in" in field:
                        field = field.replace("in", "")
                        if not 59 <= int(field) <= 76:
                            valid = False
                    else:
                        valid = False

                elif "hcl" in field:
                    field = field.replace("hcl:", "")
                    if not "#" in field:
                        valid = False
                    else:
                        for char in field.replace("#", ""):
                            if not (char.isdigit() or char not in "abcdef"):
                                valid = False
                
                elif "ecl" in field:
                    field = field.replace("ecl:", "")
                    if field not in allowed_eye_colors:
                        valid = False
                    
                elif "pid" in field:
                    field = field.replace("pid:", "")
                    if not len(field) == 9:
                        valid = False
                    else:
                        for char in field:
                            if not char.isdigit():
                                valid = False
            if valid:
                print("VALID")
            else:
                print("INVALID")
            valid_data_passports += valid
                    
                        



    print(valid_passports)
    print(valid_data_passports)
    input.close()