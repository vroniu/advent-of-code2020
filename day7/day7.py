from string import digits

class Bag:

    def __init__(self, initializationString):
        #Translation to remove new line symbols, dots, spaces
        removeTranslation = {10 : None, 46 : None, 32 : None}
        #Also remove the words "bag", "bags" and split the string 
        nameAndContents = initializationString.translate(removeTranslation).replace("bags", "").replace("bag", "").split("contain")
        #This variable is used in the first part
        self.canContainYourBag = False
        self.bagColor = nameAndContents[0]
        self.containedBags = []
        if not nameAndContents[1] == "noother":
            self.containedBags = nameAndContents[1].split(",")

def findBagByColor(bagColor, allBags):
    for bag in allBags:
        if bag.bagColor == bagColor:
            return bag

def calcBagsInBag(bagColor, allBags):
    bag = findBagByColor(bagColor, allBags)
    if len(bag.containedBags)==0:
        return 1
    else:
        sum = 1
        for insideBag in bag.containedBags:
            #Because insideBags contains both the color and the number of occurances, I need to filter the digits
            sum +=  int(''.join(filter(str.isdigit, insideBag))) * calcBagsInBag(insideBag.translate(str.maketrans('', '', digits)), allBags)
        return sum
 
with open("data.txt", 'r') as inputFile:

    bagsStringData = inputFile.readlines()
    inputFile.close()

    bags = []
    for bagString in bagsStringData:
        bags.append(Bag(bagString))

    #Part one - calculating the result using a queue
    #Im adding bags to queue and searching through the list for bags that can contain the bag from front of the queue
    allowedBags = 0
    queue = []
    queue.append("shinygold")
    while(len(queue) != 0):
        currColor = queue.pop()
        print("Searching for color:"+currColor)
        for bag in bags:
            #The variable canContainYourBag is used so bags arent added multiple times
            if not bag.canContainYourBag:
                for insideBag in bag.containedBags:
                    if insideBag.translate(str.maketrans('', '', digits)) == currColor:
                        allowedBags += 1
                        bag.canContainYourBag = True
                        #If the bag can contain the bag I got from the queue, I need to search which bags can also contain that bag
                        queue.append(bag.bagColor)


    print(allowedBags)
    #Subtract 1 from result (because sum is set to one in the algorithm, so it thinks that shinygold can contain shinygold)
    print(calcBagsInBag("shinygold", bags)-1)