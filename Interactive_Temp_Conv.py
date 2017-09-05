#SOPHIA INTRO TO CS MODULE 6 ASSIGNMENT TWO
option = ""
temp = ""
while option != "exit":
    option = input("Enter 'C' for celsius to fahrenheit, \nEnter 'F' for fahrenheit to celsius, \nor type Exit: ")
    temp = input("Enter the temperature: ")
    try:
        temp = float(temp)
        print(temp)
        if option.lower() == "c":
            temp = temp * 1.8 + 32
            print("Your temperature in fahrenheit is: ", temp,'\n')
        elif option.lower() == "f":
            temp = temp - 32 / 1.8
            print("Your temperature in celsius is: ", temp,'\n')
        elif option.lower() == "exit":           
            option = option.lower()
            print("Goodbye\n")
        else:
            print('You did not pick the right option.\n')
    except ValueError:
            print("I don't understand. Try again.\n")
    
    
