# power function
def power(base , exp):

    # any base raise to power 1 is base itself
    if(exp == 1):
        return base

    else:
        return base * power(base , exp-1)

    

# testing
if __name__ == "__main__":
    print(power(0 , 2))
    print(power(1 , 2))
    print(power(2 , 2))
    print(power(3 , 2))
    print(power(4 , 2))

# output - 
# 0
# 1
# 4
# 9
# 16