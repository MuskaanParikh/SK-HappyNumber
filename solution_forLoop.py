userInput=int(input("Enter a number to see if it is happy or depressed: "))

temp=userInput

for i in range(5):
    while(temp > 9):
        sum=0
    
        while(temp>0):
            r=temp%10
            sum=sum+r**2
            temp=temp//10
    
        temp=sum
    
if(temp==1): 
    print(userInput, " is a happy number")
else: 
    print(userInput, " is severly depressed")
