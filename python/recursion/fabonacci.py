# function to find the fabonacci series using recursion
def fabo(num):
    if(num <= 1):
        return num
    else:
        return fabo(num-1) + fabo(num-2)


# function to print the series
def findSeries(tillNum , sperator = " "):

    result = ""

    # no fabo for negative nums 
    if(tillNum < 0):
        raise ValueError("num passed cannot be negative")

    # adding the summed numbers to result
    for i in range(tillNum):
        result = result + str(fabo(i)) + sperator

    # removing the last substractor added
    result = result[:(len(sperator) * -1)]

    return result





# testing
if __name__ == "__main__":
    print(findSeries(1))
    print(findSeries(2))
    print(findSeries(3))
    print(findSeries(5))
    print(findSeries(10))


# output -
# 0
# 0 1
# 0 1 1
# 0 1 1 2 3
# 0 1 1 2 3 5 8 13 21 34
