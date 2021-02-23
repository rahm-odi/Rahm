# Main Function
def splitListIntoVariableParts(pathList, chunkSize):
    # Initializing Variables
    index = 0
    map = []

    # Calculating number of chunks
    numberOfChunks = round(len(pathList) / chunkSize)

    if (0 != len(pathList) % chunkSize):
        numberOfChunks += 1

    # Algorithm
    for counter in range(numberOfChunks):
        try:
            # Inserting chunks into the map
            map.append(pathList[index:index + chunkSize])
            index += chunkSize
        except IndexError:
            # Inserting chunk with leftover paths into the map
            map.append(pathList[index: len(pathList)])

    # Returning the map
    return map
