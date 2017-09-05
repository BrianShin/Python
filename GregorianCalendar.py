year = "" # setting intial value for year variable

while year!= "exit": # while loop
    year = input("Enter a Year or type Exit: ") # input
    if year.isnumeric(): # checks to see if the input are numbers
        year = int(year) # converts input into integers
        if year%4 != 0:
            print(year, "is a not leap year.")
            print(year, "is not divisible by 4.\n")
        else:
            if year%100 != 0:
                print(year, "is a leap year.")
                print(year, "is divisible by 4 but not by 100.\n")
            else:
                if year%400 == 0:
                    print(year, "is a leap year.")
                    print(year, "is divisibl by 4, 100, and 400.\n")
                else:
                    print(year, "is not a leap year.")
                    print(year, "is divisible by 4 and 100, but not by 400.\n")
    else: 
        if year.lower() == "exit": #if input is exit then exits
            year = year.lower()
            print("Goodbye.")
        else: # if the input are not numbers prints this
            print("I don't understand. Try again.\n")
