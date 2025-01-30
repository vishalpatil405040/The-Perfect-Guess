import random
n= random.randint(1,100)
guess=0
a=-1
while(a!=n):
    
    a=int(input("Guess the number: "))
    guess+=1 
    if(a>n):
        print("Lower no please")
        
    elif(a<n):    
        print("Higher no please")
           
print(f"You have guess  no {n} corrct no in {guess}attempt")
