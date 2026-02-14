
n=int(input("n= "))

perfect_numbers=[]

def find_sum_of_devisor(num):
    total=0
    
    for i in range(1,num):
        if num%i==0:
            total+=i
    return total
for number in range (2,n+1):
    if number==find_sum_of_devisor(number):
        perfect_numbers.append(number)
        


print (*perfect_numbers)