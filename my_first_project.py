
name = input ("what is your name: ")
print("hii",name,"I am a simple converter that can help you convert Length, weight & temperature")


def converter_length():
    original_unit = int(input("what is your length in cm "))
    return original_unit * 0.393701

def converter_weight():
    org_weight = int(input("what is your weight in kg "))
    return org_weight * 2.20462

def converter_tempratur():
    org_temp = int(input("what is the temperature in degrees celcius"))
    return org_temp * (9/5) + 32

def show_options(number):
    if number == 1:
        print("your lenth is " ,converter_length() ,"in inches")
    elif number == 2:
        print (" your weight is" ,converter_weight(),"in lbs")
    elif number == 3:
        print ("your temperature in farenheit is", converter_tempratur(), )

number = int(input("would you like to convert 1. Length 2. Weight or 3. Temperature "))

while(number not in [1,2,3]):
    print("please choose a number- 1,2, or 3")
    number = int(input("would you like to convert 1. Length 2. Weight or 3. Temperature "))

show_options(number)
