n=int(input("Nechta son kiritasiz: "))

first_number = int(input("birinchi sonni kiriting: "))


max = first_number
min = first_number

for _ in range (n-1):
    
    current_number= int(input("keyingi sonni kiriting: "))
    
    if current_number>max:
        max = current_number
    if current_number<min:
        min = current_number
        
    print(f"eng kichik son : {min} va eng katta son {max}" )


























