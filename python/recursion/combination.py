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



def combination(n , r):
    return facto(n) / (facto(r) * (facto(n-r)) )


if __name__ == "__main__":
    print(combination(2 , 1))
    print(combination(3 , 2))
    print(combination(4 , 3))
    print(combination(5 , 4))
    print(combination(6 , 2))


# output - 
# 2.0
# 3.0
# 4.0
# 5.0
# 15.0