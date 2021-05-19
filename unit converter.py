import time

print("------------------UNIT CONVERSION-----------------")
print("    1.LENGTH ")
print("    2.WEIGHT")
print("    3.TIME")
print("    4.TEMPERATURE")
A = int(input("Option you want to convert: "))
if A == 1:
    print("1.  KM to M")
    print("2.  M to KM")
    L = int(input("Option you want to convert: "))
    if L == 1:
        kilometer = float(input("Enter valve: "))
        conv_fac =  1000
        meter = kilometer * conv_fac
        print(str(kilometer) + "km is equal to " + str(meter) + "m.")
    elif L == 2:
        meter = float(input("Enter valve: "))
        conv_fac =  0.001
        kilometer = meter * conv_fac
        print (str(meter) + "m is equal to " + str(kilometer) + "km.")
    else:
        print("Error")    
        
    
#=======
elif A == 2:
    print("1.  KG to G")
    print("2.  G to KG")
    W = int(input("Option you want to convert: "))
    if W == 1:
        kilogram = float(input("Enter valve: "))
        conv_fac =  1000
        gram = kilogram * conv_fac
        print (str(kilogram) + "km is equal to " + str(gram) + "m.")
    elif W == 2:
        gram = float(input("Enter valve: "))
        conv_fac =  0.001
        kilogram = gram * conv_fac
        print (str(gram) + "m is equal to " + str(kilogram) + "km.")
    else:
        print("Error")     
#=======    
elif A == 3:
    print("1.  MINUTE to SECOND")
    print("2.  SECOND to MINUTE")
    T = int(input("Option you want to convert: "))
    if T == 1:
        minute = float(input("Enter valve: "))
        conv_fac =  60
        second = minute * conv_fac
        print (str(minute) + "min is equal to " + str(second) + "sec.")
    elif T == 2:
        second = float(input("Enter valve: "))
        conv_fac =  0.0166667
        minute = second * conv_fac
        print (str(second) + "sec is equal to " + str(minute) + "min.")
    else:
        print("Error") 
#=======    
elif A == 4:
    print("1.  CELCIUS to FARENHEIT")
    print("2.  FARENHEIT to CELCIUS")
    TEM = int(input("Option you want to convert: "))
    if TEM == 1:
        celcius = float(input("Enter valve: "))
        farenheit = (celcius * 9/5)+32
        print (str(celcius) + "°C is equal to " + str(farenheit) + "°f.")
    elif TEM == 2:
        farenheit = float(input("Enter valve: "))
        celcius = (farenheit - 32)*5/9
        print (str(farenheit) + "°f is equal to " + str(celcius) + "°C.")
    else:
        print("Error") 

else:
    print("Error")

time.sleep(10)
