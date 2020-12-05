def validateInteger(integer, minValue, maxValue):
    if minValue <= integer <= maxValue:
        return True

def validateHexadecimal(hexString):
    if "#" not in hexString:
        return False
    if len(hexString.replace("#", "")) != 6:
        return False
    for char in hexString.replace("#", ""):
        if not (char.isdigit() or char in "abcdef"):
            return False
    return True

def validateEyeColor(colorCode):
    allowed_eye_colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    if colorCode in allowed_eye_colors:
        return True

def validateNumberLen(numberString, allowedLen):
    if len(numberString) != allowedLen:
        return False
    for char in numberString:
        if not char.isdigit():
            return False
    return True


with open("data.txt", 'r') as input:

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

    for ps in passport_data:
        #split into fields
        fields = ps.split()
        #check if it has required fields
        if (len(fields) == 8) or (len(fields) == 7 and "cid" not in ps):
            valid = True
            for field in fields:
                if "byr" in field:
                    if not validateInteger(int(field.replace("byr:", "")), 1920, 2002):
                        valid = False

                elif "iyr" in field:
                    if not validateInteger(int(field.replace("iyr:", "")), 2010, 2020):
                        valid = False

                elif "eyr" in field:
                    if not validateInteger(int(field.replace("eyr:","")), 2020, 2030):
                        valid = False

                elif "hgt" in field:
                    if "cm" in field.replace("hgt:", ""):
                        if not validateInteger(int (field.replace("hgt:", "").replace("cm", "")), 150, 193):
                            valid = False
                    elif "in" in field.replace("hgt:", ""):
                        if not validateInteger(int(field.replace("hgt:", "").replace("in", "")), 59, 76):
                            valid = False
                    else:
                        valid = False

                elif "hcl" in field:
                    if not validateHexadecimal(field.replace("hcl:", "")):
                        valid = False
                
                elif "ecl" in field:
                    if not validateEyeColor(field.replace("ecl:", "")):
                        valid = False
                    
                elif "pid" in field:
                    if not validateNumberLen(field.replace("pid:", ""), 9):
                        valid = False
            if valid:
                print("VALID")
            else:
                print("INVALID")
            valid_data_passports += valid                  
            
    print("Here are the results!")
    print(valid_passports)
    print(valid_data_passports)
    input.close()