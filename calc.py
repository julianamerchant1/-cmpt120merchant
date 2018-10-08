# CMPT 120 Intro to Programming
# Calculator Project
# Author: Juliana Merchant
# Created: 2018/3/10

def main():
#take user input for equation
    equation=input("Input an equation: ")
    #Split equation to do operations
    list = equation.split(' ')
    while len(list)>1:
        for i in range (1, len(list), 2):
            #Mult and Div
            if '*' in list or '/' in list:
                #Mult
                if list[i]=='*':
                    result = float(list[i-1])*float(list[i+1])
                    del list [i-1:i+2]
                    list.insert (i-1, result)
                    break
                #Div
                elif list[i] == '/':
                    result = float(list[i-1])/float(list[i+1])
                    del list [i-1:i+2]
                    list.insert (i-1, result)
                    break
                #Add and Sub
            elif '+' in list or '-' in list:
                #Add
                if list[i] == '+':
                    result = float(list[i-1])+float(list[i+1])
                    del list [i-1:i+2]
                    list.insert (i-1, result)
                    break
                #Sub
                elif list[i] == '-':
                    result = float(list[i-1])-float(list[i+1])
                    del list [i-1:i+2]
                    list.insert (i-1, result)
                    break
                #else option
            else:
                print("error")

#output answer
    print(list[0])
  #?????
  #return result ?
  #print result ?

main()
