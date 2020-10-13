""" Algo - 
let a be from rod , b be to rod , c be aux rod          
n-1 disk from a to c using b                            - step -1
move 1 disk from a to b                                 - step -2
move n-1 disk from c to b using a                       - step -3
"""

class GlobalData:
    numOfSteps = 0

def toh(numOfDisk , fromBar = "A" , toBar = "B" , auxBar = "C"):

    # step 2
    if(numOfDisk == 1):
        print("Move disk 1 from {} to {}".format(fromBar , toBar))

        GlobalData.numOfSteps += 1

        return GlobalData.numOfSteps

    else:
        # step 1
        toh(numOfDisk-1 , fromBar , auxBar , toBar)

        print("Move disk {} from {} to {}".format(numOfDisk , fromBar , toBar))

        GlobalData.numOfSteps += 1

        # step 3
        toh(numOfDisk-1 , auxBar , toBar , fromBar)

        return GlobalData.numOfSteps






if __name__ == "__main__":
    print("steps taken = " , toh(1))
