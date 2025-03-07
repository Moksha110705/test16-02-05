customer_range = int(input(" enter the range below 2 lakhs "))
if customer_range >=  120000 and customer_range <= 200000:
    print (" TVS Apache RTR 160 -- 1,20,000 - 1,30,000 ")
elif customer_range > 75000 and customer_range < 120000:
    print(" TVS StaR City+ -- 75,541 and  TVS Jupiter -- 87,472")
elif customer_range >= 50000 and  customer_range <= 75000:
    print("TVS Scooty Pep+ -- 50,473 ")
else:
    print("no vehicle available for your budget")
    
    
    

