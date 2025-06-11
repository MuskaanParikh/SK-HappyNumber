userInput=int(input("Enter a number to see if it is happy or depressed: "))

temp=userInput
counter=1

while(temp>9 and counter<5):
    sum=0
    
    while(temp>0):
        r=temp%10
        sum=sum+r**2
        temp=temp//10
        
    temp=sum
    counter=counter+1

if(temp==1): 
    print(userInput, " is a happy number")
else: 
    print(userInput, " is severly depressed")
