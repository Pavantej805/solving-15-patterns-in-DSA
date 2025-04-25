#checking the given string is palindrome or not using two pointers
string=input()
left=0
right=len(string)-1
while left<=right:
    if string[left]!=string[right]:
        print("False")
    left+=1
    right-=1
print("True")
        