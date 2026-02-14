n=int(input("n= "))

prime_number=[]
for number in range(2,n+1):
    is_prime=True
    for devisor in range(2,number):
        if number%devisor ==0:
            is_prime=False
    if is_prime:
        prime_number.append(number)
        
print(*prime_number)
