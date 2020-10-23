# User function Template for python3

# Insert all the element of array arr[] (size N)
# fill the hash table hash[] (size hashSize)
def QuadraticProbing(hash, hashSize, arr, N):
    for i in range(N):  # Iterating over array
        if (hash[arr[i] % hashSize] == -1):  # If the place is empty then we insert arr[i] at that place
            hash[arr[i] % hashSize] = arr[i]
        else:
            k = arr[i] % hashSize
            power = 1
            while (hash[(k + power * power) % hashSize] != -1):
                power += 1
            hash[(k + power * power) % hashSize] = arr[i]  # Insert arr[i] after finding the empty position



def main():
    T = int(input())

    while (T > 0):

        hashSize = int(input())
        sizeOfArray = int(input())
        arr = [int(x) for x in input().strip().split()]

        hash = [-1] * hashSize
        QuadraticProbing(hash, hashSize, arr, sizeOfArray)

        for i in hash:
            print(i, end=" ")
        print()
        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends