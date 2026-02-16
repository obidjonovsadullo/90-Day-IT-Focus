number=int(input("n:"))

digit_sum=0
digit_count=0


while number>0:
    digit_sum+=number%10
    number=number//10
    digit_count+= 1
    
    
print(digit_count,digit_sum)















