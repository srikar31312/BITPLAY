# Program to find the number of zero bits and one bits in a number

# Functions taking our number as input
def numberOfBits(n):
    ones=0
    zeros=0

    # while our number is greater than zero check the last bit and right shift
    while(n):

        # use AND operator to check if the last bit is 1 or 0
        if(n&1==1):
            ones+=1
        else:
            zeros+=1
        # Right shift the number remove the last bit that we just checked above
        n>>=1
        print("\n\Ones =",ones,"\nZeros ",zeros)

number = int(input("Enter your number : "))
numberOfBits(number)  