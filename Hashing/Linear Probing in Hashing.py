# User function Template for python3

def linearProbing(hashSize, arr, N):
    hash = [-1]*hashSize
    for i in range(N):
        if(hash[arr[i]%hashSize] == -1):
            hash[arr[i] % hashSize] = arr[i]
        else:
            k = (1 + arr[i]) % hashSize
            counter = 0
            while (counter < hashSize and hash[k] != -1):
                k = (1 + k) % hashSize;
                counter += 1
            if (counter < hashSize):  # If we find a position where arr[i] can be inserted then we insert
                hash[k] = arr[i]
        return hash
def main():
    T = int(input())

    while (T > 0):

        hashSize = int(input())
        sizeOfArray = int(input())
        arr = [int(x) for x in input().strip().split()]

        hash = linearProbing(hashSize, arr, sizeOfArray)

        for i in hash:
            print(i, end=" ")
        print()
        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends