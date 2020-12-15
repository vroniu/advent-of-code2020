def allXPosibilities(assignedAdresses, adres, xMask, value):
    if "X" not in xMask:
        # Create a mask that will set the 1 bits
        newMaskToSet = int(xMask.translate({90: 48}), 2)
        # Create a mask that will clear the 0 bits
        newMaskToZero = int(xMask.translate({90: 49}), 2)
        # Apply the mask to the adres and add to dictionary
        assignedAdresses[(adres & newMaskToZero | newMaskToSet)] = value
    else:
        # Find the first X occurance and call the function with the first X changed
        firstXOccurance = xMask.find("X")
        allXPosibilities(assignedAdresses, adres, xMask[:firstXOccurance] + "1" + xMask[(firstXOccurance + 1):], value)
        allXPosibilities(assignedAdresses, adres, xMask[:firstXOccurance] + "0" + xMask[(firstXOccurance + 1):], value)


with open("data.txt", 'r') as inputFile:
    lines = [line.strip() for line in inputFile.readlines()]

    maskToZeroTranslation = {88: 49}    # change X to 1
    maskToSetTranslation = {88: 48}     # change X to 0

    setValues = {}

    # PART ONE

    for line in lines:
        if line.startswith("mask = "):
            # Set the masks
            maskToZero = int(line.replace("mask = ", "").translate(maskToZeroTranslation), 2)
            maskToSet = int(line.replace("mask = ", "").translate(maskToSetTranslation), 2)
        else:
            # Translation to remove square brackets
            translation = {91: None, 93: None}
            # Get the address and value
            adressAndValue = line.translate(translation).replace("mem", "").split(" = ")
            memAdress = int(adressAndValue[0])
            memValue = int(adressAndValue[1])
            # Apply the mask to value and add to dictionary
            setValues[memAdress] = (memValue & maskToZero | maskToSet)

    print(sum(setValues.values()))

    # PART TWO

    setValues = {}

    maskToXTranslation = {48: 90, 49: 90}

    for line in lines:
        if line.startswith("mask = "):
            # Get the mask with just the ones
            maskToSet = int(line.replace("mask = ", "").translate({88: 48}), 2)
            # Get the mask with Xs - Z in place of any other digits
            maskToX = line.replace("mask = ", "").translate({48: 90, 49: 90})
        else:
            # Get the starting adress and value
            translation = {91: None, 93: None}
            adressAndValue = line.translate(translation).replace("mem", "").split(" = ")
            memAdress = int(adressAndValue[0])
            memValue = int(adressAndValue[1])
            # Apply the first mask to adress
            memAdress = (memAdress | maskToSet)
            # Call the function to get all the possible X values
            allXPosibilities(setValues, memAdress, maskToX, memValue)

    print(sum(setValues.values()))
