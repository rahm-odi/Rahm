# Importing the main method
import method


# Defining Test Conditions
def test():
    # List of paths
    testVariable = [
        "path/to/file/1",
        "path/to/file/2",
        "path/to/file/3",
        "path/to/file/4",
        "path/to/file/5",
        "path/to/file/6",
        "path/to/file/7",
        "path/to/file/8",
        "path/to/file/9",
        "path/to/file/10",
        "path/to/file/11",
        "path/to/file/12",
        "path/to/file/13",
        "path/to/file/14",
        "path/to/file/15",
        "path/to/file/16",
        "path/to/file/17",
        "path/to/file/18",
        "path/to/file/19",
        "path/to/file/20",
    ]

    # Results of the function
    result = method.splitListIntoVariableParts(testVariable, 4.6)

    # Printing groups of paths
    counter = 0
    for chunk in result:
        print("Key " + str(counter) + ":")

        for path in chunk:
            print("     " + path)

        counter += 1


# Calling Test Function
test()
