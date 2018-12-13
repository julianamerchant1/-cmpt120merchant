#calc 5.py
# CMPT 120 Intro to Programming
# Project 5
# Author: Juliana Merchant

from graphics import *
# following line of code is asked for in textbook but outputs error
from button import Button
# import button.py, allowing placement of calc keys etc.
class Calculator:
# impliments simple GUI
    def __init__(self):
# create window for calc
        win = GraphWin("Calculator")
        win.setCoords(0,0,6,7)
        win.setBackground("blue")
        self.win = win
        self.__createButtons()
        self.display = self.__createDisplay()
        

    def __createButtons(self):
# create list of buttons, starting w standard
        bSpecs= [(2,1,'0'), (3,1,'.'),
                 (1,2,'1'), (2,2,'2'), (3,2,'3'), (4,2,'+'), (5,2,'-'),
                 (1,3,'4'), (2,3,'5'), (3,3,'6'), (4,3,'*'), (5,3,'/'),
                 (1,4,'7'), (2,4,'8'), (3,4,'9'), (4,4,'<-'), (5,4,'C')]
        self.buttons = []
        for (cx,cy,label) in bSpecs:
            self.buttons.append(Button(self.win,Point(cx,cy),.75,.75,label))
# make EQUAL button larger
        self.buttons.append(Button(self.win, Point(4.5,1),1.75,.75, "="))
# activate buttons
        for b in self.buttons:
            b.activate()
            
    def __createDisplay(self):
# background of top box, where input is shown, came up before fixing some seemingly unrelated lines, no longer appears
        bg = Rectangle(Point(.5,5.5), Point(5.5,6.5))
        bg.setFill('light blue')
        bg.draw(self.win)
        text = Text(Point(3,6), "")
        text.draw(self.win)
        text.setFace("courier")
        text.setStyle("bold")
        text.setSize(16)
        return text

    def getButton(self):
# waits for button to be clicked and returns label
        while True:
            p= self.win.getMouse()
            for b in self.buttons:
                if b.clicked(p):
                    return b.getLabel()
                
    def processButton(self,key):
# updates calc display
        if key == 'C':
            self.display.setText("")
        elif key =='<-':
            self.display.setText(self.display.getText()[:-1])
        elif key == '=':
            try:
                result = self.calculate()
            except: result = 'ERROR'
            self.display.setText(str(result))
        else:
            print(self.display.getText(), key)
            if key in ['+', '-', '*', '/']:
                key =' '+key+' '
            self.display.setText(self.display.getText()+key)

    def run(self):
        while True:
            key = self.getButton().getText()
            self.processButton(key)

    #if __name__ == '__main__':
        'create a calculator object'
        #theCalc = Calculator()
        #call run method
        theCalc.run()
        
    def calculate(self):
        equation = self.display.getText()
        list = equation.split(' ')
        print(equation, list)
        while len(list)>1:
            for i in range (1, len(list), 2):
            #Mult and Div
                if '*' in list or '/' in list:
                    #Mult
                    if list[i]=='*':
                        result = float(list[i-1])*float(list[i+1])
                        del list [i-1:1+2]
                        list.insert (i-1, result)
                        break
                    #Div
                    elif list[i] == '/':
                        result = float(list[i-1])/float(list[i+1])
                        del list [i-1:1+2]
                        list.insert (i-1, result)
                        break
                    #Add and Sub
                if '+' in list or '-' in list:
                    #Add
                    if list[i] == '+':
                        result = float(list[i-1])+float(list[i+1])
                        del list [i-1:1+2]
                        list.insert (i-1, result)
                        break
                #Sub
                elif list[i] == '-':
                    result = float(list[i-1])-float(list[i+1])
                    del list [i-1:1+2]
                    #list should have one object, print list
                    list.insert (i-1, result)
                    break
                #else option
                else:
                    print("error")
        print(list)
        return list[0]
    
# make recursive
#def recursiveSolve:
    #if "(" not in equation:
        #return [calculate(equation)]
    #else:
        #( = equation.index('(')
          #) = findEnd(equation[i])
        #return equation[:i] + recursiveSolve(equation
        
def main():
    theCalc = Calculator()
    theCalc.run()
        
main()


# If your code still has groups of statements that repeat throughout the code, create functions for those.
# Add the following memory functions to your calculator (the memory stores values, not equations):
# o M+: Add the last result to memory
# o M-: Subtract the last result from memory
# o MR: Recall the value from memory
# o MC: Clear the memory
