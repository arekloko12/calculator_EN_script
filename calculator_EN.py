import datetime

print("---------------------")
print("Script - Calculator")
print("---------------------")


def addition():
    result = 0
    while(True):
        x = input("Enter the number of numbers you want to add\n> ")
        if (x.isdigit()):
            x = int(x)
            for i in range(x):
                while(True):
                    number = input("Enter "+str(i+1)+" number: ")
                    if (number.isdigit()):
                        number = int(number)
                        result = result + number
                        break
                    else:
                        print("----------------------------")
                        print("Invalid value! Try again")
                        print("----------------------------")
                        continue
            break
        else:
            print("----------------------------")
            print("Invalid value! Try again")
            print("----------------------------")
            continue

    print("The result is: "+str(result))
    while (True):
        save_opt = input("Do you want to save the result? Y / N\n> ")
        if (save_opt == "y" or save_opt == "Y"):
            date = datetime.datetime.now()
            file = open("..\\results_of_activities.txt", "a")
            file.write("\n---------------------------------------\nAction of the day: "+date.strftime("%Y-%m-%d %H:%M:%S")+"\nThe result is: "+str(result))
            break
        elif (save_opt == "n" or save_opt == "N"):
            break
        else:
            print("----------------------------")
            print("Invalid value! Try again")
            print("----------------------------")
            continue
    exit()
    
def subtraction():
    result = 0
    while(True):
        x = input("Enter the number of numbers you want to add\n> ")
        if (x.isdigit()):
            x = int(x)
            for i in range(x):
                while(True):
                    number = input("Enter "+str(i+1)+" number: ")
                    if (number.isdigit()):
                        number = int(number)
                        if(i > 0):
                            result = result - number
                        else:
                            result = number

                        break
                    else:
                        print("----------------------------")
                        print("Invalid value! Try again")
                        print("----------------------------")
                        continue
            break
        else:
            print("----------------------------")
            print("Invalid value! Try again")
            print("----------------------------")
            continue

    print("The result is: "+str(result))
    while (True):
        save_opt = input("Do you want to save the result? Y / N\n> ")
        if (save_opt == "y" or save_opt == "Y"):
            date = datetime.datetime.now()
            file = open("..\\results_of_activities.txt", "a")
            file.write("\n---------------------------------------\nAction of the day: "+date.strftime("%Y-%m-%d %H:%M:%S")+"\nThe result is: "+str(result))
            break
        elif (save_opt == "n" or save_opt == "N"):
            break
        else:
            print("----------------------------")
            print("Invalid value! Try again")
            print("----------------------------")
            continue

    exit()

def division():
    while(True):
        number_a = input("Enter the first number: ")
        if (number_a.isdigit()):
            number_a = int(number_a)
            if (number_a == 0):
                print("--------------------------")
                print("Cannot be divided by 0")
                print("--------------------------")
                continue
            elif (number_a != 0):
                break
        else:
            print("----------------------------")
            print("Invalid value! Try again")
            print("----------------------------")
            continue
            
    while(True):
        number_b = input("Enter the second number: ")
        if (number_b.isdigit()):
            number_b = int(number_b)
            if (number_b == 0):
                print("--------------------------")
                print("Cannot be divided by 0")
                print("--------------------------")
                continue
            elif (number_b != 0):
                break
        else:
            print("----------------------------")
            print("Invalid value! Try again")
            print("----------------------------")
            continue


    result = number_a / number_b
    print("The result is: "+str(result))
    while (True):
        save_opt = input("Do you want to save the result? Y / N\n> ")
        if (save_opt == "y" or save_opt == "Y"):
            date = datetime.datetime.now()
            file = open("..\\results_of_activities.txt", "a")
            file.write("\n---------------------------------------\nAction of the day: "+date.strftime("%Y-%m-%d %H:%M:%S")+"\nThe result is: "+str(result))
            break
        elif (save_opt == "n" or save_opt == "N"):
            break
        else:
            print("----------------------------")
            print("Invalid value! Try again")
            print("----------------------------")
            continue
    
    exit()

def multiplication():
    result = 0
    while(True):
        x = input("Enter the number of numbers you want to multiply\n> ")
        if (x.isdigit()):
            x = int(x)
            for i in range(x):
                while(True):
                    number = input("Enter "+str(i+1)+" number: ")
                    if (number.isdigit()):
                        number = int(number)
                        if(i > 0):
                            result = result * number
                        else:
                            result = number

                        break
                    else:
                        print("----------------------------")
                        print("Invalid value! Try again")
                        print("----------------------------")
                        continue
            break
        else:
            print("----------------------------")
            print("Invalid value! Try again")
            print("----------------------------")
            continue

    print("The result is: "+str(result))
    while (True):
        save_opt = input("Do you want to save the result? Y / N\n> ")
        if (save_opt == "y" or save_opt == "Y"):
            date = datetime.datetime.now()
            file = open("..\\results_of_activities.txt", "a")
            file.write("\n---------------------------------------\nAction of the day: "+date.strftime("%Y-%m-%d %H:%M:%S")+"\nThe result is: "+str(result))
            break
        elif (save_opt == "n" or save_opt == "N"):
            break
        else:
            print("----------------------------")
            print("Invalid value! Try again")
            print("----------------------------")
            continue

    exit()

# Options menu

while (True):
    option = input("1 - Addition\n2 - Subtraction\n3 - Division\n4 - Multiplication\n> ")
    if (option.isdigit()):
        option = int(option)
        if (option == 1):  
            addition()
        elif (option == 2):
            subtraction()
        elif (option == 3):
            division()
        elif (option == 4):
            multiplication()
        else:
            print("Unknown option")
            continue
    else:
        print("----------------------------")
        print("Invalid value! Try again")
        print("----------------------------")
        continue