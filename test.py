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
        "path/to/file/10"
    ]

    # Results of the function
    result = method.splitListIntoVariableParts(testVariable, 5)

    # Printing groups of paths
    counter = 0
    for chunk in result:
        print("Key " + str(counter) + ":")

        for path in chunk:
            print("     " + path)

        counter += 1


# Calling Test Function
test()
