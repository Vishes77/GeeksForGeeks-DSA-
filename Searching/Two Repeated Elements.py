import math

def twoRepeated(arr, N):
    virtual = [0]*(N+1)
    for i in range(N+2):
        virtual[arr[i]] += 1
        if(virtual[arr[i]]== 2):
            print(arr[i],end=" ")




def main():
    T = int(input())
    while (T > 0):
        N = int(input())

        A = [int(x) for x in input().strip().split()]

        twoRepeated(A, N)
        print()

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends