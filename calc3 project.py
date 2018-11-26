#calc 3.py
# CMPT 120 Intro to Programming
# Project 3
# Author: Juliana Merchant
# edited on Nov 26, only changed hash format.

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
        text.setstyle("bold")
        text.setsize(16)

    def getButton(self):
# waits for button to be clicked and returns label
        while True:
            p= self.win.getMouse()
            for b in self.buttons:
                if b.clicked(p):
                    return b.getLabel()
                # ^ AttributeError: 'Button' object has no attribute 'getLabel' ?
                
    def processButton(self,key):
# updates calc display
        if key == 'C':
            self.display.setText("")
        elif key =='<-':
            self.display.setText(text[:-1])
        elif key == '=':
            try:
                result = eval(text)
            except: result = 'ERROR'
            self.display.setText(str(result))
        else:
            self.display.setText(text+key)

    def run(self):
        while True:
            key = self.getButton()
            self.processbutton(key)

    #if __name__ == '__main__':
        'create a calculator object'
        #theCalc = Calculator()
        #call run method
        theCalc.run()
        
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
