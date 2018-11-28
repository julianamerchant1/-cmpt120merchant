# Calc 4.py
# CMPT 120 Intro to Programming
# Project 4
# Author: Juliana Merchant

# 1: Errors are thrown.
# 2: If your code still has groups of statements that repeat throughout the
# code, create functions for those. (I believe I already have)
# later addressed below
# 3: later addressed below, "Use the Button class that we created in class for your calculator buttons"
# 4: Display class is created.
# 5: theCalc is intended to be the calculator class
# 6: I believe this is cohesive, and the hashes explain any issues with specific
# possible solutions, as well as addressing exact points bulleted
# Calculator box came up before these changes, on Calculator/Project 3 
# Unable to work off of correct code from Project 3
# ^ as it still has not been graded for me.


from graphics import *
# "No module named 'graphics'", unknown why
# following line of code is asked for in textbook but outputs error
from button import Button
# "No module named 'button'" error as well, when 'graphics' error is hashed.
# again, unknown why
# Hinders bullet 3: "Use the Button class that we created in class for your calculator buttons"
class Calculator:
# impliments simple GUI
    def __init__(self):
# create window for calc
        #self.win = GraphWin("Calculator", 400, 600)
# Error when previous errors above are hashed (without 'self.' before 'win'): 'GraphWin is not defined"
# GraphWin being defined above.
# I cannot go further in the program to properly check errors for the lines below


# Attempted to implement code given as class example, these are the hashed out lines following/below this
        #self.display = Display(self.win)
        #self.keypad = Keypad(self.win)
        #self.keypad.getKey(click)

    def getKey(self, p):
        for button in self.buttons:
            if button.clicked(p):
                return button.getLabel()

# Attempted to implement code given as class example, these are the hashed out lines before/above this
# Keypad created below already

        win.setCoords(0,0,6,7)
        win.setBackground("blue")
        self.win = win
        self.__createButtons()
        
# 4: createButtons is a class to create display I believe
    def __createButtons(self):
# create list of buttons, starting w standard
        bSpecs= [(2,1,'0'), (3,1,'.'),
                 (1,2,'1'), (2,2,'2'), (3,2,'3'), (4,2,'+'), (5,2,'-'),
                 (1,3,'4'), (2,3,'5'), (3,3,'6'), (4,3,'*'), (5,3,'/'),
                 (1,4,'7'), (2,4,'8'), (3,4,'9'), (4,4,'<-'), (5,4,'C')]
# use data.groupby([columns list]) for this to group, for point 2?
# alternatively, perhaps group_keys=True (?)
        self.buttons = []
        for (cx,cy,label) in bSpecs:
            self.buttons.append(Button(self.win,Point(cx,cy),.75,.75,label))                           
# intended to make EQUAL button larger
        self.buttons.append(Button(self.win, Point(4.5,1),1.75,.75, "="))
# activate buttons
        for b in self.buttons:
            b.activate()

# Attempted to implement code given as class example, these are the hashed out lines following/below this
#from button import*
#class KeyPad:
    #def __init__(self, win):
        #self.buttons = [
            #Button(win, Point(1,1), .75, .75, '-/+')
            #Button(win, Point(1.75,1), .75, .75, '0')
            #Button(win, Point(1.75,1), .75, .75, '0')
            #]

    #def getKey(self, p):
        #for button in self.buttons:
            #if button.clicked(p):
                #return button.getLabel()
# Attempted to implement code given as class example, these are the hashed out lines before/above this
# Button points already created above

# Attempted to implement code given as class example, these are the hashed out lines following       
#from display import *
#from keypad import *
#from keypad import *
#from calculatorengine import *
#def run(self)
    #while True:
        #click = self.win.getMouse()
        # Get the key hat was pressed
        #key = self.keypad.getKey(click)
        #process the key and get the result
        #result = self.calcEngine.process(key)
        # Display the result
        #self.display.update(result)
# Again, attempted to implement code given as class example, hashed above/before this
# I believe that display for buttons and output when clicked is addressed below.

            
# 4: The following is a createdisplay class.            
    def __createDisplay(self):
# background of top box, where input is shown, came up before fixing some code, no longer appears
        bg = Rectangle(Point(.5,5.5), Point(5.5,6.5))
        bg.setFill('light blue')
        bg.draw(self.win)
        text = Text(Point(3,6), "")
        text.draw(self.win)
        text.setFace("courier")
        text.setstyle("bold")
        text.setsize(16)
# begin lines from lab/lecture (deactivate, activate, and clicked)        
    def deactivate(self):
        self.label.setFill('dark grey')
        self.rect.setwidth(1)
        self.active = false
# tried to activate above with b.activate() method                           
    def activate(self):
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True
                          
    def clicked(self,p):
        return self.active and \
        self.xmin <= p.getV() <= self.xmax and \
        self.ymin <= p.gety() <= self.ymax
# end of lines from the lab / lecture

    def getButton(self):
# waits for button to be clicked and returns label
# Identify True to group with Boolean
# True below, therefore I believe it is already grouped. 
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
 # point 2: groupby() for text input and output? Unsure how, if so.
 # I believe it is taken care of below (?)
    def run(self):
        while True:
            key = self.getButton()
            self.processbutton(key)

            
# Attempted to implement code given as class example, these are the hashed out lines following       
#from display import *
#class CalculatorApp:
    #def __init__(self):
        #self.win = GraphWin("Calculator", 400, 600)
        #self.display = Display(self.win)
        #self.keypad = Keypad(self.win)
        #self.calcEngine = CalculatorEngine()
    #def run(self):
        #while True:
            #click = self.win.getMouse()
            # Get the key that was pressed
            #key = self.keypad.getKey(click)
            #print(key)
            # Process the key and get result
            #result = self.calcEngine.process(key)
            # Display the result
            #self.display.update(result)
#def main():
    #calc = CalculatorApp
    #calc.run()
# Again, attempted to implement code given as class example, hashed above/before this
# I believe I did this below, however.


# 5: theCalc is intended to be the calculator class
    if __name__ == '__main__':
# 'create a calculator object'
        theCalc = Calculator()
# call run method
        theCalc.run()
        
def main():
    theCalc = Calculator()
    theCalc.run()
        
main()

