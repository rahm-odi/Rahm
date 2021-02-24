# Import
# Main Function
def splitListIntoVariableParts(pathList, chunkSize):
    # In case of decimal input
    chunkSize = round(chunkSize)

    # Initializing Variables
    index = 0
    map = []

    # If the chunkSize is less than or equal to zero...
    # return the pathList as is
    if chunkSize <= 0:
        map.append(pathList[index : len(pathList)])
    else:
        # Calculating number of chunks
        numberOfChunks = int(len(pathList) / chunkSize) + (
            len(pathList) % chunkSize > 0
        )

        # Algorithm
        for counter in range(numberOfChunks):
            try:
                # Inserting chunks into the map
                map.append(pathList[index : index + chunkSize])
                index += chunkSize
            except IndexError:
                # Inserting chunk with leftover paths into the map
                map.append(pathList[index : len(pathList)])

    # Returning the map
    return map
