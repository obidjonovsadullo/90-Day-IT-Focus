n=int(input("Nechta son kiritasiz: "))

first_number = int(input("birinchi sonni kiriting: "))

index=1
min = first_number

for i in range (2,n+1):
    
    current_number= int(input(f"{i}- sonni kiriting: "))
    
    if current_number<min:
        min = current_number
        index=i
        
        
    print(f"eng kichik son : {min} va u {i}-da joylashgan" )

