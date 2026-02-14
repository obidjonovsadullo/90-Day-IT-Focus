x =int(input("1-sonni kiriting: "))
y =int(input("2-sonni kiriting:"))


min = (x+y)/2
max = 2*x*y


if x>y:
    x,y = max,min
elif x<y:
    y,x = max, min
    
print(f"{x}  {y}")    
