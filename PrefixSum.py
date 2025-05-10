a=list(map(int,input("Enter numbers to add in list:").split()))
p_Sum=[]
total=0
for num in a:
    total+=num
    p_Sum.append(total)
print(p_Sum)
