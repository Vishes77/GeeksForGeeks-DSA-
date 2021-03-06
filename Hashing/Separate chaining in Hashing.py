# User function Template for python3

# Complete this code
def separateChaining(hashSize, arr, sizeOfArray):
    hashTable = [0] * hashSize
    for i in range(hashSize):
        hashTable[i]=[]
    for i in range(sizeOfArray):
        #pushing element arr[i] in the list hashtable at position arr[i]%hashsize
        hashTable[arr[i]%hashSize.append(arr[i])]
    return hashTable

def main():
    T = int(input())
    while (T > 0):

        hashSize = int(input())
        sizeOfArray = int(input())
        arr = input().strip()
        arr = arr.split()
        arr = list(map(int, arr))

        hashTable = separateChaining(hashSize, arr, sizeOfArray)

        for i in range(len(hashTable)):
            if len(hashTable[i]) > 0:
                print(str(i) + "->", end="")
                for j in range(len(hashTable[i]) - 1):
                    print(str(hashTable[i][j]) + "->", end="")
                print(hashTable[i][len(hashTable[i]) - 1], end="")
                print()
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends