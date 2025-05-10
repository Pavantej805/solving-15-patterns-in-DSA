#sliding window pattern to find the sum of the maximum value of the substring
def slidingWindow(k,arr):
    n=len(arr)
    if n==0 or k<=0 or k>n:
        return None
    max_sum=0
    sum=0
    for i in range(k):                               # looping upto the kth values and store the sum of the values in max_sum
        sum+=arr[i]
    max_sum=sum
    for i in range(n-k):
        sum-=arr[i]                                  #remove the first value
        sum+=arr[i+k]                                #adding the ending value
        max_sum=max(max_sum,sum)
    return max_sum
k=int(input("Enter Kth Values:"))                    # k is the length of the substring of the user wants
arr=list(map(int,input("Enter arr values:").split()))# Here taking the values into the array
print(slidingWindow(k,arr))