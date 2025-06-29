# Programm to check if the Nth bit is set or not
def setOrNot(number, n):

    #Make a mask variabe by left shifting 1 (k-1) times and check if (n AND mask) equals 1 or 0
    if number & (1 << (n-1)):
        print("\nSET")

    else:
        print("\nNOT SET")

number = int(input("enter number : "))
n =int(input("ENter bit number: "))
setOrNot(number, n)