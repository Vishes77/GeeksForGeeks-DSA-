
def maxWater(height, n):
    maximum = 0
    i=0
    j=n-1

    while(i<j):
        if(height[i]<height[j]):
            maximum = max(maximum,(j-i-1)*height[i])
            i += 1
        elif(height[j]<height[i]):
            maximum = max(maximum,(j-i-1)*height[j])
        else:
            maximum = max(maximum,(j-i-1)*height[i])
            i += 1
            j -= 1
    return maximum



def main():
    t = int(input())
    while (t > 0):
        n = int(input())
        height = [int(x) for x in input().strip().split()]
        print(maxWater(height, n));
        t -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends