
month_number = int(input("Enter a number between 1 and 12: "))
month_switch = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

if month_number in month_switch:
    print(f"The month is {month_switch[month_number]}")
else:
    print("Invalid input! Please enter a number between 1 and 12.")
    
          
            
            
        
