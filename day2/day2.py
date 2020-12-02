def xor(bool1, bool2):
    if bool1 + bool2 == 1:
        return True
    else:
        return False

with open("data.txt", 'r') as inputFile:
    result_one = 0
    result_two = 0

    lines = inputFile.readlines()
    for line in lines:
        tab = line.split(" ")
        nums = tab[0].split("-")
        key = tab[1].replace(":", "")
        password = tab[2]

        count = 0
        for char in password:
            if char == key:
                count += 1
        
        if(count >= int(nums[0]) and count <= int(nums[1])):
            result_one += 1

        if( xor (password[int(nums[0]) - 1] == key, password[int(nums[1]) - 1] == key) ):
            result_two += 1



        print("nums=" + nums[0] + " " + nums[1] + " key=" + key + " pass=" + password)

    print("Here are the results!")
    print(result_one) 
    print(result_two)


    