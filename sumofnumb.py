a = int(input("Enter a number: "))
sum_digits = 0  

while a > 0:
    rem = a % 10 
    sum_digits += rem  
    a //= 10  

print("Sum of digits:", sum_digits)
