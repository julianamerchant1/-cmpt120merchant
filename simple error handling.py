# Arithmetic engine.py

# CMPT 120 - Lab #6
# JULIANA MERCHANT
# 10-17-13

def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n")
    
def showOutro():
    print("\nThank you for using the Arithmetic Engine…")
    print("\nPlease come back again soon!")
def doLoop():
    while True:
            cmd = input("What computation do you want to perform? ")   
#if capatalized, can be changed with 'lower'.
            cmd = cmd.lower
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
#up to this point works, from here on the loop continues asking for commands and numbers, rather than beginning 'try'
#if given invalid numeral input, results in error- due to loop not iterating
#Error message --> "ValueError: invalid literal for int() with base 10: 'sub'"
#Attempt at reformatting by adding or removing indentation blocks does not seem to help
            try:
                cmd=="add"
                #cmd equals statements and colons inconcise, not sure what to change. likely the main issue of program
                #if 'except' is changed to 'else', program will not even begin to run
                result = num1 + num2 
            except cmd == "sub":
                result = num1 - num2
            except cmd == "mult":
                result = num1 * num2
            except cmd == "div":
                result = num1 // num2
            except cmd == "quit":
                break
        #allow user to terminate program
#unsupported command should reiterate the program, after outputting an error message   
#unable to figure out what is causing invalid commands to show program errors, rather than intended output
            except:
                print(cmd," is not a valid command.")
                return
            #should the 'except' be a 'finally'?
def main():
    showIntro()
    doLoop()
    showOutro()
main()
