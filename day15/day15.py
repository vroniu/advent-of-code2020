userInput = input()

numbers = [int(num) for num in userInput.split(",")]
print(numbers)

numbersSpoken = {}
index = 1

for n in numbers:
    numbersSpoken[n] = (None, index)
    recentlySpokenNumber = n
    index += 1

# There is probably some optimalization possible, this takes like 3 mins to calculate the second part
while index <= 30000000:
    if recentlySpokenNumber not in numbersSpoken:
        # a new number
        recentlySpokenNumber = 0
        numbersSpoken[recentlySpokenNumber] = (None, index)
    elif None not in numbersSpoken[recentlySpokenNumber]:
        # a number that appeared before
        recentlySpokenNumber = numbersSpoken[recentlySpokenNumber][1] - numbersSpoken[recentlySpokenNumber][0]
        # check if entry for this number already exists
        if recentlySpokenNumber in numbersSpoken:
            numbersSpoken[recentlySpokenNumber] = (numbersSpoken[recentlySpokenNumber][1], index)
        else:
            numbersSpoken[recentlySpokenNumber] = (None, index)
    else:
        # a number that appeared for the first time
        recentlySpokenNumber = 0
        numbersSpoken[recentlySpokenNumber] = (numbersSpoken[recentlySpokenNumber][1], index)

    print(str(index) + ":" + str(recentlySpokenNumber) + " " + str(numbersSpoken[recentlySpokenNumber]))
    index += 1
print(recentlySpokenNumber)