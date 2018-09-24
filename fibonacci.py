# fibonacci.py

def main ():

    n=int(input("Add value for fibonacci equivalent: "))
    fib1=1
    fib2=1
    fib=fib1+fib2
    for i in range (n-2):
        fib = fib1 + fib2
        fib1 = fib2
        fib2 = fib
    print("Your number is: ",fib ) 
main()
