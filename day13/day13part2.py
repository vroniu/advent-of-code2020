data = open("data.txt", 'r').readlines()[1].split(",")

justNumbers = [int(d) for d in data if d != "x"]

# Fancy recursive-lambda version
func = lambda i, it, nums: i if not nums else func(i + it, it, nums) if (i + data.index(str(nums[0]))) % nums[0] != 0 else func(i, it * nums[0], nums[1:])
print(func(1, 1, justNumbers))

# Normal version
i = 1  # the result number
it = 1  # amount you can iterate that number bpart1.py
# iterate through every bus id
while len(justNumbers) != 0:
    # its not even needed to get the max, you can get just the first number
    maxNum = max(justNumbers)
    justNumbers.remove(maxNum)
    # find the index (it indicates the offset from the result number in which the bus will depart)
    maxNumIndex = data.index(str(maxNum))

    # iterate by it to find a number that is divisable by maxNum
    while (i + maxNumIndex) % maxNum != 0:
        i += it

    # increase the iteration amount
    it = it * maxNum

print(i)
