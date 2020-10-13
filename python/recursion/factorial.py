# function to find the factorial of a number using recursion
def facto(num):

    # no factorial of negative number
    if(num < 0):
        raise ValueError("number cannot be negative")

    # facto of 0 is 1 
    if(num == 0):
        return 1

    # facto of 1 is 1 (exit statement)
    if(num == 1):
        return 1

    else:
        return num * facto(num-1)

    

# testing
if __name__ == "__main__":
    print(facto(0))
    print(facto(1))
    print(facto(2))
    print(facto(3))
    print(facto(4))


# output - 
# 1
# 1
# 2
# 6
# 24