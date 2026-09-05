year = int(input("What year is your truck? (Enter 0 to exit) ")) # priming read

while year != 0:
    if (year <= 2010) or (year >=2021):
        print ( "We only buy trucks manufactured between 2021 amd 2020.")
    elif year <= 2015:
        print("We will offer $15000 for your truck.")
    else:
        print("We will offer $22000 for your truck.")

    year = int(input("What year is your truck? (Enter 0 to exit) "))  # repeating read

print ("Thank you for using our truck purchasing service!")