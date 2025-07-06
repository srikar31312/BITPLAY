# Program to find position of first set bit from right
def getFirstSetBitPos(n):
    if n == 0:
        return 0

    position = 1
    while (n & 1) == 0:
        n = n >> 1
        position += 1
    return position

# Input from user
num = int(input("Enter number: "))

# Find and display position
pos = getFirstSetBitPos(num)
print(f"Position of the first set bit: {pos}")