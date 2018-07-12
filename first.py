def posorneg(n):
    if(n==0):
        return "Zero"
    elif(n>0):
        return "Positive"
    else:
        return "Negative"
n=int(input())
print(posorneg(n))
