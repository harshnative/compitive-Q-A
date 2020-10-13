# function to calculate the length of string using recursion
def lenString(string):

    if(string == ""):
        return 0
    else:
        return 1 + lenString(string[1:])


# testing
if __name__ == "__main__":
    print(lenString("hello"))
