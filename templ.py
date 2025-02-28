temp=int (input("enter one for celcius to farenheit; enter two for farenheit to celcius "))
if (temp == 1):
    c = float (input(" enter temperature in celcius: "))
    f = (c* (9/5)) +32
    print(" farenheit = ", f)
elif (temp == 2):
    f = float (input(" enter temperature in farenheit: "))
    c = (f - 32) * (5/9)
    print(" celcius = ", c)
else:
    print ("enter only one or two")
