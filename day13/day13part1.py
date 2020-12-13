with open("data.txt", 'r') as input:
    timestamp = int(input.readline())
    buses = input.readline().split(",")

    i = timestamp
    takenBus = 0
    busTaken = False
    while not busTaken:
        for busNumber in [int(bus) for bus in buses if bus != "x"]:
            if i % busNumber == 0:
                busTaken = True
                takenBus = busNumber
                break
        i += 1

    print((i - 1 - timestamp) * takenBus)